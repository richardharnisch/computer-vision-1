# /// script
# dependencies = ["numpy>=1.26", "scipy>=1.11", "markdown-it-py>=3.0"]
# ///
"""Independently recompute numerical answers and check generated artifacts."""

from collections import Counter
import csv
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

import numpy as np
from scipy import ndimage, signal
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]


def check_rendered_prose(text):
    # Equations must not silently lose '*' or '_' through Markdown emphasis.
    from build import literal_prose
    rendered_tokens = MarkdownIt().parseInline(literal_prose(text))[0].children
    assert all(t.type == "text" for t in rendered_tokens), text
    assert "".join(t.content for t in rendered_tokens) == text, text


def check_computation_snippets(exams, values):
    completions = {
        "E1Q31": "Xc=R@(Xw-C)\nq=K@Xc\nanswer=q[0]/q[2]",
        "E1Q32": "answer=np.linalg.norm(np.linalg.lstsq(L,i,rcond=None)[0])",
        "E1Q39": "answer=np.linalg.lstsq(A,-It,rcond=None)[0][0]",
        "E2Q33": "answer=np.linalg.lstsq(L*w[:,None],i*w,rcond=None)[0][2]",
        "E2Q40": "answer=np.linalg.lstsq(A,-It,rcond=None)[0][1]",
        "E2Q41": "",
        "E3Q22": "answer=prediction",
        "E3Q32": "",
    }
    expected = dict(values, E3Q22=0)
    qs = {q["id"]: q for e in exams for q in e["questions"]}
    for question_id, completion in completions.items():
        block = re.search(r"```python\n(.*?)\n```", qs[question_id]["stem"], flags=re.S).group(1)
        env = {}
        # Only this pack's authored short NumPy snippets; no course notebook is executed.
        exec(block + "\n" + completion, env)
        assert np.isclose(env["answer"], expected[question_id], rtol=0, atol=1e-8), question_id
    return len(completions)


class RenderedText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.details = 0

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        if tag == "details":
            self.details += 1
            assert "open" not in dict(attrs), "Flashcard answers should start collapsed"


def check_markdown_export(text):
    # CommonMark + tables parses the pack's formatting and raw HTML details.
    markdown = MarkdownIt("commonmark", {"html": True}).enable("table")
    parser = RenderedText()
    parser.feed(markdown.render(text))
    return "".join(parser.text), parser.details


def heading_ids(text):
    # The pack's fragment links use plain topic headings; handle repeated slugs too.
    counts, ids = Counter(), set()
    for heading in re.findall(r"^#{1,6} (.+)$", text, flags=re.M):
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        ids.add(slug if not counts[slug] else f"{slug}-{counts[slug]}")
        counts[slug] += 1
    return ids


def affine_y():
    xy = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=float)
    target = np.array([[2, -1], [4, -1], [3, 2], [5, 3]], dtype=float)
    A = np.column_stack((xy, np.ones(4)))
    P = np.linalg.lstsq(A, target, rcond=None)[0]
    return (np.array([2, 3, 1]) @ P)[1]


def fitted_homography_x():
    A, rhs = [], []
    for (x, y), (u, v) in zip([(0, 0), (1, 0), (0, 1), (1, 1)],
                              [(1, 2), (3, 2), (1, 4), (3, 3)]):
        A.extend([[x, y, 1, 0, 0, 0, -u*x, -u*y],
                  [0, 0, 0, x, y, 1, -v*x, -v*y]])
        rhs.extend([u, v])
    assert np.linalg.matrix_rank(A) == 8
    h = np.linalg.solve(A, rhs)
    H = np.append(h, 1).reshape(3, 3)
    assert abs(np.linalg.det(H)) > 1e-9
    q = H @ [.5, .5, 1]
    return q[0] / q[2]


def nms_count():
    # Use only kept boxes, never a suppressed box, to suppress later candidates.
    # Derive the table from real rectangles instead of inventing incompatible IoUs.
    boxes = np.array([[0, 0, 4, 2], [1, 0, 5, 2], [2, 0, 6, 2], [3, 0, 7, 2]])
    iou = np.zeros((4, 4))
    for i, a in enumerate(boxes):
        for j, b in enumerate(boxes):
            overlap = np.maximum(0, np.minimum(a[2:], b[2:])-np.maximum(a[:2], b[:2])).prod()
            area_a, area_b = (a[2:]-a[:2]).prod(), (b[2:]-b[:2]).prod()
            iou[i, j] = overlap / (area_a+area_b-overlap)
    assert np.allclose(iou, [[1, 3/5, 1/3, 1/7], [3/5, 1, 3/5, 1/3],
                             [1/3, 3/5, 1, 3/5], [1/7, 1/3, 3/5, 1]])
    remaining = list(range(4))
    kept = []
    while remaining:
        best = remaining.pop(0)
        kept.append(best)
        remaining = [n for n in remaining if iou[best, n] <= .5]
    assert kept == [0, 2]
    return len(kept)


def interpolated_ap():
    tp = np.array([0, 1, 0, 1, 1])
    precision = np.cumsum(tp) / np.arange(1, 6)
    recall = np.cumsum(tp) / 4
    envelope = np.maximum.accumulate(precision[::-1])[::-1]
    return (np.diff(np.r_[0, recall]) * envelope).sum()


def checks():
    L = np.array([[0, 0, 1], [.8, 0, .6], [-.8, 0, .6], [0, .8, .6], [0, -.8, .6]])
    g = np.linalg.lstsq(L, [.70, .64, .16, .44, .36], rcond=None)[0]
    row = np.array([0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0])
    close = ndimage.binary_erosion(ndimage.binary_dilation(row, np.ones(3)), np.ones(3))
    I = np.array([[1, 2, 0], [3, -1, 4], [2, 1, 5]])
    K = np.array([[1, 0, 2], [0, -1, 0], [3, 0, -2]])
    A1 = np.array([[1, 0], [0, 1], [1, 1], [2, 0]])
    R = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    q = np.array([[800, 20, 320], [0, 600, 240], [0, 0, 1]]) @ R @ (np.array([3, 5, 4])-np.array([1, 2, 0]))
    Hq = np.array([[2, 0, 1], [0, 1, -2], [.1, 0, 1]]) @ [5, 4, 1]
    M = np.array([[9, 3], [3, 9]])
    conf1 = np.array([[18, 2, 0], [3, 12, 5], [1, 4, 15]])
    tp, fp, fn = conf1[1, 1], conf1[:, 1].sum()-conf1[1, 1], conf1[1].sum()-conf1[1, 1]
    values = {
        "E1Q31": q[0]/q[2], "E1Q32": np.linalg.norm(g), "E1Q33": 5-3+4*.5,
        "E1Q34": np.floor(3*np.cumsum([1, 3, 2, 2])[1]/8), "E1Q35": close.sum(),
        "E1Q36": signal.convolve2d(I, K, mode="valid").item(),
        "E1Q37": abs(np.fft.fft([1, 2, 3, 4])[1]),
        "E1Q38": np.linalg.det(M)-.04*np.trace(M)**2,
        "E1Q39": np.linalg.lstsq(A1, -np.array([-2, 1, -1, -5]), rcond=None)[0][0],
        "E1Q40": np.ceil(np.log(.01)/np.log1p(-.6**4)), "E1Q41": Hq[0]/Hq[2],
        "E1Q42": np.array([.75*.25, .25*.25, .75*.75, .25*.75]) @ [10, 30, 50, 90],
        "E1Q43": 2*tp/(2*tp+fp+fn), "E1Q44": (1+2/3+3/5)/4,
        "E1Q45": (4*3)/(6*4+6*4-4*3),
        "E1Q46": ((31+2-5)//2+1)*((29-3)//2+1)*8,
        "E1Q47": (5*3*3+1)*8, "E1Q48": (7*7*16+1)*10,
        "E1Q49": receptive_field([(3, 1), (2, 2), (3, 1)]),
        "E1Q50": abs(np.array([9, 9, 1]) @ (np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]]) @ [12, 7, 1])),
    }
    R2 = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    L2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])
    w = np.array([1, 1, 1, 2])
    grid = np.array([[1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1],
                     [0, 0, 0, 1, 0], [1, 0, 0, 0, 1]])
    count4 = ndimage.label(grid, ndimage.generate_binary_structure(2, 1))[1]
    count8 = ndimage.label(grid, np.ones((3, 3)))[1]
    A2 = np.array([[2, 1], [1, -1], [0, 2], [3, 0]])
    T = np.array([[1, 2], [3, 4]])
    P = np.array([[[2, 3], [4, 5]], [[1, 1], [3, 5]], [[2, 2], [2, 4]]])
    conf2 = np.array([[30, 10, 0], [5, 10, 5], [0, 2, 8]])
    values.update({
        "E2Q31": np.linalg.norm(-R2.T @ [-3, 2, 1]), "E2Q32": 30/40*np.mean([80, 40, 20]),
        "E2Q33": np.linalg.lstsq(L2*w[:, None], np.array([.2, .3, .6, 1.2])*w, rcond=None)[0][2],
        "E2Q34": .1+.6*.5+.8*.5**4, "E2Q35": (70-50)*255/(150-50),
        "E2Q36": count4-count8, "E2Q37": np.median([[0, 7, 8], [8, 255, 9], [10, 11, 0]]),
        "E2Q38": hog_bin(), "E2Q39": np.degrees(np.angle(-3-4j)),
        "E2Q40": np.linalg.lstsq(A2, -np.array([-5, -1, -3, -6]), rcond=None)[0][1],
        "E2Q41": np.argmin(((P-T)**2).sum(axis=(1, 2))), "E2Q42": affine_y(),
        "E2Q43": (np.array([.30, .40, .60, .20, .10])/np.array([.50, .50, 1, .21, .40]) < .75).sum(),
        "E2Q44": np.mean([0, 2, 3]), "E2Q45": np.mean(np.diag(conf2)/conf2.sum(axis=1)),
        "E2Q46": nms_count(), "E2Q47": weight_gradient(),
        "E2Q48": 8*5+5, "E2Q49": 7*7*(5*2+4), "E2Q50": 1200*.12/(414-390),
    })
    opening_input = np.zeros((9, 9), dtype=bool)
    opening_input[3:6, 3:6] = True
    opening_input[0, 0] = True
    magnitudes = np.array([[10, 6, 0, 0, 5, 5, 0], [0, 6, 0, 0, 0, 5, 0], [0, 6, 6, 0, 0, 0, 0]])
    retained = ndimage.binary_propagation(magnitudes >= 9, structure=np.ones((3, 3)), mask=magnitudes >= 4)
    gradients = np.array([[1, 0], [0, 2], [1, 1], [2, 0]])
    squared = np.array([[4, 9], [9, 16], [1, 4], [25, 36], [.25, 1]])
    accepted = np.sqrt(squared[:, 0]/squared[:, 1]) < .7
    descriptors = np.array([1, 3, 5, 7, 8, 9])
    bins = np.abs(descriptors[:, None]-np.array([0, 4, 8])).argmin(axis=1)
    y = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
    pred = np.array([.9, .8, .7, .6, .5, .4]) >= .6
    tp, fp, fn = (y & pred).sum(), (~y & pred).sum(), (y & ~pred).sum()
    values.update({
        "E3Q31": (600/2)*(1/2)+(240-20)/2, "E3Q32": normalized_red_mean(),
        "E3Q33": abs(2*2*3-3*2), "E3Q34": .75*np.dot([2/3, -1/3, 2/3], [0, .6, .8]),
        "E3Q35": ndimage.binary_opening(opening_input, np.ones((3, 3))).sum(),
        "E3Q36": np.median(np.array([0, 0, 10])+[0, 10, 0])-np.median([0, 0, 10])-np.median([0, 10, 0]),
        "E3Q37": np.fft.ifft(np.fft.fft([1, 0, 2, 0])*np.fft.fft([0, 1, 0, 1])).real[3],
        "E3Q38": retained.sum(), "E3Q39": np.linalg.eigvalsh(gradients.T @ gradients)[0],
        "E3Q40": np.linalg.norm(8*np.array([1.75, -.5])+[.25, .75]),
        "E3Q41": np.ceil(np.log(.001)/np.log1p(-.4**3)), "E3Q42": fitted_homography_x(),
        "E3Q43": np.sqrt(squared[accepted, 0]).max(), "E3Q44": (bins == 2).mean(),
        "E3Q45": 2*tp/(2*tp+fp+fn), "E3Q46": interpolated_ap(),
        "E3Q47": (64+1)*16+(9*16+1)*16+(16+1)*64, "E3Q48": (3**3*2+1)*5,
        "E3Q49": .75*.6*.8, "E3Q50": 900*.2/12**2*.25,
    })
    return values


def hog_bin():
    gx, gy = np.array([3, -3, 0, 2]), np.array([4, -4, 5, 0])
    angles = np.degrees(np.arctan2(gy, gx)) % 180
    magnitudes = np.hypot(gx, gy)
    # Histogram uses declared hard bins, not the solution's manual assignment.
    histogram, _ = np.histogram(angles, bins=np.arange(0, 181, 20), weights=magnitudes)
    return histogram[2]


def normalized_red_mean():
    # Recompute each pixel's ratio independently of the displayed broadcasting code.
    pixels = [(6, 1, 3), (2, 6, 2), (0, 0, 0), (1, 1, 2)]
    return np.mean([r/(r+g+b) if r+g+b else 0 for r, g, b in pixels])


def receptive_field(layers):
    r = j = 1
    for kernel, stride in layers:
        r += (kernel-1)*j
        j *= stride
    return r


def weight_gradient():
    # Independent central finite difference, rather than the answer's hand sum.
    image = np.array([[1, 3, 5], [2, -1, 4]])
    W = np.array([[1, 0], [-1, 2]], dtype=float)
    def loss(weights):
        return (signal.correlate2d(image, weights, mode="valid") * [2, -1]).sum()
    step = 1e-5
    plus, minus = W.copy(), W.copy()
    plus[1, 1] += step
    minus[1, 1] -= step
    return (loss(plus)-loss(minus))/(2*step)


def main():
    from build import literal_prose, prepare_exam, read_cards
    exams = json.loads((ROOT / "data/exams.json").read_text())
    assert exams == [prepare_exam(n) for n in (1, 2, 3)], "Generated exams are stale; run build.py"
    values = checks()
    failures = []
    ids = set()
    for exam in exams:
        qs = exam["questions"]
        assert len(qs) == 50
        assert Counter(q["kind"] for q in qs) == {"mc": 30, "num": 20}
        assert [q["number"] for q in qs] == list(range(1, 51))
        for q in qs:
            assert q["id"] not in ids
            ids.add(q["id"])
            assert q["source"] and q["explanation"]
            if q["kind"] == "mc":
                assert len(set(q["options"])) == 4
                assert q["options"]["ABCD".index(q["answer"])] == q["correct"]
            else:
                actual = float(values[q["id"]])
                if not np.isclose(actual, q["answer"], rtol=0, atol=1e-8):
                    failures.append(f'{q["id"]}: authored {q["answer"]}, computed {actual}')
                if q["integer"]:
                    assert actual.is_integer(), q["id"]
                else:
                    assert abs(float(q["display_answer"])-q["answer"]) <= .01+1e-12
        rendered = (ROOT / f'exams/exam-{exam["number"]}.md').read_text()
        assert len(re.findall(r"^### Q\d\d —", rendered, flags=re.M)) == 50
        assert "Unrounded reference" not in rendered and "Worked solutions" not in rendered
        solution = (ROOT / f'solutions/exam-{exam["number"]}-solutions.md').read_text()
        assert len(re.findall(r"^### Q\d\d —", solution, flags=re.M)) == 50
        for q in qs:
            assert literal_prose(q["stem"]) in rendered, q["id"]
            assert literal_prose(q["explanation"]) in solution, q["id"]
            assert f'### Q{q["number"]:02d} — {q["display_answer"]}\n' in solution, q["id"]
            if q["kind"] == "mc":
                for letter, option in zip("ABCD", q["options"]):
                    assert f'- **{letter}.** {literal_prose(option)}\n' in rendered, q["id"]
                assert f'**{q["answer"]}. {literal_prose(q["correct"])}**' in solution, q["id"]
        markdown = MarkdownIt()
        expected_fences = [token.content for q in qs for token in markdown.parse(q["stem"])
                           if token.type == "fence"]
        actual_fences = [token.content for token in markdown.parse(rendered) if token.type == "fence"]
        assert expected_fences == actual_fences, "A displayed code/data block was changed"
    assert set(values) == {q["id"] for e in exams for q in e["questions"] if q["kind"] == "num"}
    if failures:
        raise AssertionError("Numerical mismatches:\n"+"\n".join(failures))
    snippet_count = check_computation_snippets(exams, values)
    print("PASS: 150 questions, unique IDs, 30 MC + 20 numerical per exam, separate solutions.")
    print("PASS: all 60 numerical references independently recomputed, including finite-difference backprop.")
    print("PASS: NMS IoUs derived from real rectangles; generated exams and displayed code blocks match authoring sources.")
    print(f"PASS: {snippet_count} NumPy computation snippets executed, with supplied routine completion where needed.")
    if "--exams-only" not in sys.argv:
        cards = json.loads((ROOT / "data/flashcards.json").read_text())
        assert cards == read_cards(), "Generated flashcards are stale; run build.py"
        assert len({c["front"] for c in cards}) == len(cards), "Duplicate card fronts"
        assert len({c["id"] for c in cards}) == len(cards)
        assert all(c["priority"] in ("core", "breadth") and c["back"] and c["source"] for c in cards)
        for card in cards:
            check_rendered_prose(card["front"])
            check_rendered_prose(card["back"])
        with (ROOT / "flashcards-anki.tsv").open(newline="") as f:
            rows = list(csv.reader((line for line in f if not line.startswith("#")), delimiter="\t"))
        assert len(rows) == len(cards)
        assert all(len(row) == 3 for row in rows)
        for row, card in zip(rows, cards):
            assert row == [card["front"], f'{card["back"]} [Sources: {card["source"]}. ID: {card["id"]}]',
                           f'cv1 topic::{card["topic"]} priority::{card["priority"]}']
        md = (ROOT / "flashcards.md").read_text()
        assert md.count("<details>") == len(cards) == md.count("</details>")
        visible, details = check_markdown_export(md)
        assert details == len(cards)
        for card in cards:
            assert f'**{literal_prose(card["front"])}**' in md
            assert f'\n{literal_prose(card["back"])}\n' in md
            assert card["front"] in visible and card["back"] in visible, card["id"]
        print(f"PASS: {len(cards)} cards; unique prompts; complete source/priority tags; 3-column Anki export.")
        print("PASS: all card fronts/backs render to HTML with formula operators intact and answers initially collapsed.")
        print("Card priorities:", dict(Counter(c["priority"] for c in cards)))
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if target.startswith(("http", "mailto:")):
                    continue
                filename, _, fragment = target.partition("#")
                destination = path.parent / filename if filename else path
                assert destination.exists(), (path, target)
                if fragment:
                    assert fragment in heading_ids(destination.read_text()), (path, target)
        priorities = Counter(c["priority"] for c in cards)
        readme = (ROOT / "README.md").read_text()
        assert f'{len(cards)} flashcards' in readme
        assert f'{priorities["core"]} `core` cards' in readme
        assert f'{priorities["breadth"]} `breadth` cards' in readme
        assert f'{len({c["topic"] for c in cards})} topics' in readme
        print("PASS: local Markdown links and topic anchors resolve; README counts match the export.")


if __name__ == "__main__":
    main()
