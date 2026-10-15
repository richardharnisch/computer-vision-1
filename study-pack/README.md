# Computer Vision 1 — exam study pack

**Three original practice exams and 673 flashcards**, based on the supplied 2026 lectures, seminars, labs, exam guidance and relevant sections of both textbooks. Solutions are separate from questions.

## Start here

**[Six-page A4 cheat sheet](cheat-sheet/cv1-cheat-sheet.pdf)** · [LaTeX source](cheat-sheet/cv1-cheat-sheet.tex) · [Page map, printing and rebuild instructions](cheat-sheet/README.md). Print at 100%, double-sided, on three A4 sheets. It covers all 24 topic groups with dense formulas, definitions, method steps, code recipes and worked examples.

**[Condensed master lab: Night Shift](master-lab/master-lab.ipynb)** · [Setup and coverage](master-lab/README.md). Work through Labs 1–5 as one recycling-line inspection project: 16 coding checkpoints, generated data, CPU-only training and separate solutions.

**PDF versions (compiled with LaTeX):**

| Exam | Questions | Separate solutions |
|---|---|---|
| 1 | [PDF](exams/exam-1.pdf) | [Solutions PDF](exams/exam-1-solutions.pdf) |
| 2 | [PDF](exams/exam-2.pdf) | [Solutions PDF](exams/exam-2-solutions.pdf) |
| 3 | [PDF](exams/exam-3.pdf) | [Solutions PDF](exams/exam-3-solutions.pdf) |

The PDFs use native LaTeX math for equations, fractions, subscripts, powers and matrices. Python code remains literal. Standalone LaTeX sources are beside the PDFs in `study-pack/exams/`. To regenerate them, run `uv run --no-project study-pack/tools/build_pdfs.py` with XeLaTeX and `latexmk` installed. The build checks all 50 question headings, extracted prose/code and numeric data grids in each PDF, and rejects missing glyphs or overflowing boxes. Math-renderer tests are in `study-pack/tools/test_pdf_math.py`; text extraction alone cannot verify mathematical layout.

| Practice exam | Focus | Questions |
|---|---|---:|
| [Exam 1](exams/exam-1.pdf) | Foundations under pressure | 50 |
| [Exam 2](exams/exam-2.pdf) | Implementation and failure diagnosis | 50 |
| [Exam 3](exams/exam-3.pdf) | Synthesis and transfer | 50 |

Each exam has **30 single-answer multiple-choice questions and 20 numerical questions**. Numerical work includes array/code interpretation, fitting, filtering, geometry and CNN calculations. Use [the reusable answer sheet](answer-sheet.md).

Suggested limit: **150 minutes per exam**. The length, timing and equal point weights are training choices, **not the official exam specification**. The old course mocks explicitly warn that they are not representative of this year's exam.

## How to use the pack

1. Attempt Exam 1 without solutions or AI help. Use your own three double-sided A4 sheets and a local Python/NumPy notebook, as the course permits. Specialized computation routines are supplied where needed; executable OpenCV/PyTorch is not required.
2. Mark it with the separate key. Give one raw point per correct answer, out of 50. For ordinary numerical answers, use ±0.01 around the **unrounded** reference, inclusive; integer counts must be exact. Keep intermediate precision and normally submit two decimals.
3. Review wrong answers **and correct guesses**. Record whether the problem was the concept, formula, convention/sign, array axis, units or arithmetic. Explain why each rejected MC option is wrong.
4. Use [the topic index](TOPIC_INDEX.md) to review the relevant cards. Then solve each missed calculation again without the key.
5. Attempt Exams 2 and 3 as fresh timed tests. They revisit important concepts through different scenarios. If time is short, prioritize weak topics over reading every card in order.

The raw practice score is **not an official exam grade**. The actual ANS grading applies configured guess correction. The syllabus says to answer every MC question even if unsure.

### Solutions — open after your attempt

- [Exam 1 key and worked solutions](exams/exam-1-solutions.pdf)
- [Exam 2 key and worked solutions](exams/exam-2-solutions.pdf)
- [Exam 3 key and worked solutions](exams/exam-3-solutions.pdf)

Each file has a quick answer key, then explanations, numerical references and source citations. The internal `data/` and `tools/` files also contain answers; avoid them during an attempt.

## Flashcards

- [Browse the 673 cards](flashcards.md): grouped into **24 topics**, with expandable answers.
- [Import into Anki](flashcards-anki.tsv): UTF-8, tab-separated **Front / Back / Tags**.
- [Topic index](TOPIC_INDEX.md): card counts and question numbers for each subject.

Cards cover definitions, equations, assumptions, method names, acronym expansions, relationships and common implementation errors. **559 `core` cards** have higher study priority; **114 `breadth` cards** cover supporting material. These are study labels, not exam probabilities.

### Anki import

1. In Anki Desktop, select **File → Import** and choose `study-pack/flashcards-anki.tsv`.
2. Choose the ordinary **Basic** note type, not the reversed-card type, and a destination deck.
3. Confirm **Tab** as the separator; column 1 → **Front**, column 2 → **Back**, column 3 → **Tags**. Keep HTML interpretation **off**. Recent Anki versions can read these settings from the file headers.
4. Check the preview, import, and inspect a formula card and its tags. The source citation and card ID are included on the back.

Useful Anki searches:

```text
tag:priority::core
tag:topic::camera
tag:priority::core tag:topic::flow
```

The TSV was structurally checked, but import into the Anki application was **not** tested here. On an older importer, set the field mapping manually if it does not recognize the headers. The intended result is 673 notes / 673 forward cards before any duplicate filtering.

## Scope and important source warnings

- [COVERAGE.md](COVERAGE.md) maps the lecturer's checklist and labs to the pack, lists exact source paths, and states review limits and optional-content exclusions.
- [SOURCE_NOTES.md](SOURCE_NOTES.md) explains the normal-integration sign discrepancy, NumPy phase argument order, AP variants, YOLO versions and other source qualifications.

Follow a question's stated convention. Do not combine incompatible formulas merely because both appear in course documents. The textbooks were used to support taught topics; neither was read cover to cover. Optional-only advanced code and Guest Lecture 13 are excluded. This pack is not lecturer-issued and cannot guarantee every possible exam question.

Also use the lecturer's [ANS interface-test instructions](../exam-prep/ans_test.md) to practise the digital interface. This pack does not replace that environment test.

## Rebuild and verification

From `/home/richard/Documents/academics/1/computer-vision-1`, with `uv` installed:

For the delivered PDFs (no Markdown exam files required):

```bash
uv run --no-project study-pack/tools/test_pdf_math.py
uv run --no-project study-pack/tools/build_pdfs.py
```

The renderer tests also recompute all 60 numerical answers and execute the eight short NumPy computation snippets. PDF-only notation is in `study-pack/tools/pdf_math.py`; the canonical question and solution text stays unchanged.

For optional Markdown exam exports and the original full-pack verifier:

```bash
uv run --no-project study-pack/tools/build.py
uv run --no-project study-pack/tools/verify.py
```

The build writes only generated files inside `study-pack/`. The original course files are unchanged. Authoring sources are `study-pack/tools/exam1.py`, `study-pack/tools/exam2.py`, `study-pack/tools/exam3.py`, and `study-pack/data/cards.txt`; edit these rather than the generated exam/card files.

Verification independently recomputes all **60 numerical references**, executes the short NumPy computation snippets, and checks counts, IDs, answer keys, generated-content consistency, TSV fields/tags, Markdown formulas/code blocks and local links. The NMS example is checked against actual rectangle geometry. Conceptual correctness and source alignment were also manually reviewed; the script cannot prove them.

No course training notebooks, model downloads, official ANS questions or Anki application import were executed for this verification.
