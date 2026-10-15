"""Check the delivered notebook, then execute blank and solved copies in fresh CPU kernels.

Executed copies, figures and kernel configuration stay in /tmp/opencode.
Never writes answers or execution output into the learner notebook.
"""
from __future__ import annotations

import ast
import base64
import copy
import contextlib
import inspect
import io
import json
from pathlib import Path
import re
import tempfile

import nbformat as nbf
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

from build_notebook import HERE, digest, make_notebook, write_notebook
import solutions

REFERENCES = {
    "01": [solutions.colour_tools], "02": [solutions.recolour], "03": [solutions.photometric],
    "04": [solutions.integrate], "05": [solutions.gaussian1d], "06": [solutions.gradients],
    "07": [solutions.frequency_maps], "08": [solutions.structure_scores], "09": [solutions.lk_patch],
    "10": [solutions.ratio_matches], "11": [solutions.fit_affine, solutions.ransac_affine],
    "12": [solutions.inverse_warp, solutions.feather_blend], "13": [solutions.Sorter],
    "14": [solutions.train_step, solutions.evaluate], "15": [solutions.transfer_head], "16": [solutions.cam_map],
}


def execute(notebook, destination, kernel_root):
    manager = KernelManager(kernel_name="cv1-master-check", transport="ipc",
                            ip=str(kernel_root / f"ipc-{destination.stem}"),
                            connection_file=str(kernel_root / f"{destination.stem}.json"),
                            kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(kernel_root)]))
    client = NotebookClient(notebook, km=manager, timeout=120,
                            resources={"metadata": {"path": str(HERE)}})
    try:
        client.execute()
    finally:
        nbf.write(notebook, destination)
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
    errors = [o for c in notebook.cells if c.cell_type == "code" for o in c.outputs if o.output_type == "error"]
    assert not errors
    return notebook


def main():
    import sys
    root = Path(tempfile.mkdtemp(prefix="cv1-master-check-", dir="/tmp/opencode"))
    kernel_root = root / "kernels"
    kernel_dir = kernel_root / "cv1-master-check"
    kernel_dir.mkdir(parents=True)
    (kernel_dir / "kernel.json").write_text(json.dumps({
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": "CV1 isolated CPU check", "language": "python",
    }))
    delivered = nbf.read(HERE / "master-lab.ipynb", as_version=4)
    nbf.validate(delivered)
    assert digest(delivered) == digest(make_notebook()), "Template differs from authoring source; preserve learner edits."
    assert all(c.execution_count is None and not c.outputs for c in delivered.cells if c.cell_type == "code")
    exercises = [c for c in delivered.cells if "exercise_id" in c.metadata]
    assert [c.metadata.exercise_id for c in exercises] == list(REFERENCES)
    assert len(delivered.cells) == 68
    for cell in delivered.cells:
        if cell.cell_type == "code":
            ast.parse(cell.source)
    assert "import solutions" not in "\n".join(c.source for c in delivered.cells)

    html, _ = HTMLExporter().from_notebook_node(delivered)
    (root / "learner-render.html").write_text(html)
    for anchor in ("booth", "signal", "motion", "map", "sorter"):
        assert f'id="{anchor}"' in html, f"Missing rendered navigation target: {anchor}"
    hints = re.findall(r"<details>.*?</details>", html, flags=re.DOTALL)
    expected_hints = sum(c.source.count("<details>") for c in delivered.cells if c.cell_type == "markdown")
    assert len(hints) == expected_hints > 0
    assert all("<code>" in hint and "`" not in hint for hint in hints), "Hint markdown is not rendered; keep blank lines around HTML details content."
    print(f"Rendered notebook: five navigation targets and all {expected_hints} formatted expandable hints.")

    # A rebuild must refuse even a one-line learner change, rather than destroy it.
    protected = root / "learner-copy.ipynb"
    changed = copy.deepcopy(delivered)
    changed.cells[0].source += "\nMy own note."
    nbf.write(changed, protected)
    original_bytes = protected.read_bytes()
    try:
        write_notebook(protected, make_notebook())
    except SystemExit:
        pass
    else:
        raise AssertionError("Rebuild overwrote learner work.")
    assert protected.read_bytes() == original_bytes

    blank = copy.deepcopy(delivered)
    blank.cells.append(nbf.v4.new_code_cell("assert all(v == 'TODO' for v in mission.states.values())\n"
                                           "assert len(mission.states) == 16\nassert final_report is None"))
    execute(blank, root / "blank-executed.ipynb", kernel_root)
    print("Blank learner notebook: cold Run All succeeds; 16 honest TODOs, no substituted answers.")

    solved = copy.deepcopy(delivered)
    for cell in solved.cells:
        if "exercise_id" in cell.metadata:
            cell.source = "\n\n".join(inspect.getsource(fn) for fn in REFERENCES[cell.metadata.exercise_id])
        if "RUN_ABLATIONS = False" in cell.source:
            cell.source = cell.source.replace("RUN_ABLATIONS = False", "RUN_ABLATIONS = True")
        if "RUN_REAL_PHOTO = False" in cell.source:
            cell.source = cell.source.replace("RUN_REAL_PHOTO = False", "RUN_REAL_PHOTO = True")
    solved.cells.append(nbf.v4.new_code_cell("""
assert all(v == 'PASS' for v in mission.states.values()), mission.states
assert len(mission.states) == 16 and final_report is not None
assert final_report['test']['confusion'].sum() == 57
assert 0 <= final_report['test']['accuracy'] <= 1
assert np.isfinite(final_report['test']['loss'])
assert np.linalg.norm(final_report['motion']-packet['displacement']) < .3
assert final_report['consensus'] >= 5
assert len(comparisons) == 6
assert all(np.isfinite(hist).all() for hist in comparisons.values())
assert sum(p.numel() for p in router.parameters() if p.requires_grad) == 34
assert np.isfinite(belt_map).all() and belt_map.ndim == 3
assert heatmap.ndim == 2 and np.isfinite(heatmap).all()
print('REFERENCE AUDIT: 16/16, fresh final pipeline, six ablations, transfer and actual Grad-CAM.')
""".strip()))
    execute(solved, root / "reference-executed.ipynb", kernel_root)
    image_count = 0
    for i, cell in enumerate(solved.cells):
        for output in cell.get("outputs", []):
            if "image/png" in output.get("data", {}):
                image_count += 1
                (root / f"figure-{i:02}-{image_count:02}.png").write_bytes(base64.b64decode(output.data["image/png"]))
    assert image_count >= 16
    print(f"Reference notebook: 16/16 checks, all optional experiments; {image_count} rendered figures.")

    # Check that common plausible mistakes are rejected, not simply given green checks.
    import numpy as np
    import mission_support as support
    m = support.Mission()
    bad_gradients = lambda image: tuple(np.zeros_like(image, dtype=float) for _ in range(4))
    with contextlib.redirect_stdout(io.StringIO()):
        assert m.run("06", bad_gradients) is None and m.states["06"] == "CHECK FAILED"
        bad_lk = lambda *args, **kwargs: np.array([2., -1.])  # easy toy passes, aperture handling fails
        assert m.run("09", bad_lk) is None and m.states["09"] == "CHECK FAILED"
        bad_blend = lambda a, b, wa, wb: np.where(a == 0, b, a)
        assert m.run("12", (solutions.inverse_warp, bad_blend)) is None and m.states["12"] == "CHECK FAILED"
        bad_cam = lambda features, grads: np.ones(features.shape[-2:])
        assert m.run("16", bad_cam) is None and m.states["16"] == "CHECK FAILED"
    print("Common-wrong-answer checks reject zero gradients, unobservable flow, black-pixel masks and fake CAMs.")
    print(f"Execution artifacts and figures: {root}")
    print("No real-model weights downloaded; RAFT API is reading-only, not claimed as an inference test.")


if __name__ == "__main__":
    main()
