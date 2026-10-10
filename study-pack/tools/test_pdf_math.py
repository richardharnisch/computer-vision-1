# /// script
# dependencies = ["numpy>=1.26", "scipy>=1.11", "markdown-it-py>=3.0"]
# ///
"""Focused PDF-renderer checks; run with uv run --no-project <this file>."""

import ast
import json
import re
import unittest

from build_pdfs import ROOT, exam_document, inline, prose, solution_document
from pdf_math import MATH, chunks, numeric_array, text_grid
from build import prepare_exam
from verify import checks, check_computation_snippets


class PDFMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exams = json.loads((ROOT / "data/exams.json").read_text())

    def test_explicit_spans_are_current_and_emit_native_math(self):
        source = "\n".join(
            text for exam in self.exams for q in exam["questions"]
            for text in [q["stem"], q["explanation"], *q.get("options", [])]
        )
        for plain, latex in MATH.items():
            with self.subTest(plain=plain):
                self.assertIn(plain, source)
                display = r"\\" in latex or len(latex) > 110 or r"\frac{\text{" in latex
                expected = "\n\\[" + latex + "\\]\n" if display else r"\(" + latex + r"\)"
                self.assertEqual(inline(plain), expected)
                self.assertNotRegex(latex, r"[\x00-\x08\x0b\x0c\x0e-\x1f]")

    def test_no_authored_prose_is_dropped(self):
        for exam in self.exams:
            for q in exam["questions"]:
                for text in [q["stem"], q["explanation"], *q.get("options", [])]:
                    self.assertEqual("".join(source for source, _ in chunks(text)), text)

    def test_python_and_inline_code_stay_literal(self):
        for exam in self.exams:
            for q in exam["questions"]:
                for code in re.findall(r"```python\n(.*?)\n```", q["stem"], re.S):
                    self.assertIn("\\begin{Code}\n" + code + "\n\\end{Code}", prose(q["stem"]))
        self.assertEqual(inline("`a**2 + x_y`"), r"\texttt{a*\allowbreak{}*\allowbreak{}2 + x\_\allowbreak{}y}")
        self.assertIn(r"\texttt{", inline("I.mean(axis=(0,1), keepdims=True)"))

    def test_numeric_matrix_values_and_row_order(self):
        for source in ("[0,0,1]", "[[0,-1,0],[1,0,0],[0,0,1]]", "[[.6,.2],[0,.25]]"):
            latex = numeric_array(source)
            body = latex.removeprefix(r"\begin{bmatrix}").removesuffix(r"\end{bmatrix}")
            actual = [[float(v) for v in row.split("&")] for row in body.split(r"\\")]
            expected = ast.literal_eval(source)
            if not isinstance(expected[0], list):
                expected = [expected]
            self.assertEqual(actual, expected)
        self.assertIsNone(numeric_array("[__import__('os').system('false')]"))
        self.assertIsNone(numeric_array("[[1,2],[3]]"))

    def test_text_data_fences_are_native_math(self):
        count = 0
        for exam in self.exams:
            for q in exam["questions"]:
                for code in re.findall(r"```text\n(.*?)\n```", q["stem"], re.S):
                    math = text_grid(code)
                    self.assertIsNotNone(math, (q["id"], code))
                    self.assertIn("\\[\n" + math + "\n\\]", prose(q["stem"]))
                    count += 1
        self.assertEqual(count, 11)

    def test_all_six_documents_use_math_font(self):
        for exam in self.exams:
            for render in (exam_document, solution_document):
                latex = render(exam)
                self.assertIn(r"\setmathfont{TeX Gyre Pagella Math}", latex)
                self.assertGreater(latex.count(r"\("), 20)
                self.assertIn(r"\frac{", latex)
                self.assertIn(r"\begin{bmatrix}", latex)

    def test_numerical_answers_and_source_are_unchanged(self):
        self.assertEqual(self.exams, [prepare_exam(n) for n in (1, 2, 3)])
        values = checks()
        count = 0
        for exam in self.exams:
            for q in exam["questions"]:
                if q["kind"] == "num":
                    self.assertAlmostEqual(q["answer"], float(values[q["id"]]), delta=1e-8)
                    count += 1
        self.assertEqual(count, 60)
        self.assertEqual(check_computation_snippets(self.exams, values), 8)


if __name__ == "__main__":
    unittest.main()
