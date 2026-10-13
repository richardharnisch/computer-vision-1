# /// script
# dependencies = ["numpy"]
# ///
"""Build the six-page sheet; reject overflow, missing glyphs, and unsafe layout."""

from __future__ import annotations

from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from verify_math import verify


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "cv1-cheat-sheet.tex"
OUTPUT = HERE / "cv1-cheat-sheet.pdf"
NS = {"h": "http://www.w3.org/1999/xhtml"}
PAGE_MARKERS = [
    ["Coordinates", "Colour spaces", "Calibrated photometric"],
    ["Histograms", "Spatial filtering", "Fourier analysis", "NumPy shape"],
    ["Canny", "SIFT", "RANSAC", "Lucas", "tracking"],
    ["homographies", "epipolar", "disparity", "Structure from Motion"],
    ["k-means", "Visual-Words", "precision", "AP", "Adam"],
    ["CNN", "RPN", "YOLO", "ResNet", "U-Net", "Grad-CAM"],
]


def main():
    for command in ["latexmk", "pdflatex", "pdftotext"]:
        if not shutil.which(command):
            raise SystemExit(f"Required command not found: {command}")
    verify()
    folder = Path(tempfile.mkdtemp(prefix="cv1-cheat-", dir="/tmp/opencode"))
    # TeX font diagnostics can contain legacy 8-bit bytes: do not decode strictly.
    proc = subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
         f"-outdir={folder}", str(SOURCE)],
        cwd=HERE, text=True, encoding="utf-8", errors="replace", capture_output=True,
    )
    (folder / "build-output.txt").write_text(proc.stdout + proc.stderr)
    if proc.returncode:
        raise SystemExit(f"LaTeX compilation failed; see {folder / 'build-output.txt'}")
    log = (folder / "cv1-cheat-sheet.log").read_text(errors="replace")
    bad = re.findall(r"^.*(?:Overfull|Missing character|Undefined control sequence|"
                     r"Font Warning|undefined references).*$", log, re.M)
    if bad:
        raise SystemExit("Invalid LaTeX output:\n" + "\n".join(bad))

    maximum = float(re.search(r"CV1MAX\|([\d.]+)pt", log)[1])
    columns = [(int(p), int(c), float(h)) for p, c, h in
               re.findall(r"CV1COL\|(\d+)\|(\d+)\|([\d.]+)pt", log)]
    assert [(p, c) for p, c, _ in columns] == [(p, c) for p in range(1, 7) for c in range(1, 4)]
    for page, column, height in columns:
        assert .96*maximum <= height <= maximum, (page, column, height, maximum)

    pdf = folder / OUTPUT.name
    xml = subprocess.check_output(["pdftotext", "-bbox", str(pdf), "-"]).decode("utf-8")
    # Some TeX math delimiters extract as XML-forbidden control characters.
    # Remove these extraction artifacts for coordinate checks, not glyph checks.
    xml = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", xml)
    pages = ET.fromstring(xml).findall(".//h:page", NS)
    assert len(pages) == 6, f"Expected six sides, got {len(pages)}"
    for number, page in enumerate(pages, 1):
        width, height = float(page.attrib["width"]), float(page.attrib["height"])
        assert abs(width-595.276) < .05 and abs(height-841.890) < .05, "Not A4 portrait"
        words = page.findall("h:word", NS)
        assert len(words) > 2400, f"Unexpectedly sparse page {number}"
        text = " ".join(w.text or "" for w in words)
        for marker in PAGE_MARKERS[number - 1]:
            assert marker.casefold() in text.casefold(), (number, marker)
        # Geometry margins are 5 mm; optical punctuation can protrude <0.5 mm.
        safe = 4.5*72/25.4
        for word in words:
            x1, y1, x2, y2 = [float(word.attrib[k]) for k in ("xMin", "yMin", "xMax", "yMax")]
            assert safe <= x1 <= x2 <= width-safe, (number, "horizontal clipping", word.text)
            assert safe <= y1 <= y2 <= height-safe, (number, "vertical clipping", word.text)

    # Publish only after all checks pass; the .tex is the standalone authoring source.
    shutil.copyfile(pdf, OUTPUT)
    usage = [height/maximum*100 for _, _, height in columns]
    print(f"Built {OUTPUT}: 6 A4 portrait pages; no overflow or missing-glyph warnings.")
    print(f"Column-height use: {min(usage):.1f}--{max(usage):.1f}%, mean {sum(usage)/18:.1f}%.")
    print(f"Build log: {folder / 'cv1-cheat-sheet.log'}")


if __name__ == "__main__":
    main()
