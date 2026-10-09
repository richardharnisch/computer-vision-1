"""Render the authored study materials; no source-course files are modified."""

from collections import Counter
import csv
import importlib
import json
from pathlib import Path
import random
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LETTERS = "ABCD"
RULES = """- 50 questions: 30 single-answer multiple choice and 20 numerical. Each is worth 1 raw practice point.
- Suggested training limit: **150 minutes**. This is not a claim about the actual exam duration or question count.
- Use up to three double-sided A4 sheets, prepared by you, and a local Jupyter notebook. No internet, AI assistance or answer key during the attempt.
- Use Python/NumPy for computation; SciPy is also allowed. You do not need executable OpenCV or PyTorch. Specialized routines are provided when needed.
- For multiple choice, select exactly one of A–D. Attempt every question.
- Unless an exact integer is requested, round the final numerical answer to **two decimal places**. Keep full precision in intermediate steps. Use fractions rather than percentages unless specified.
- Numerical practice grading uses the syllabus rule: within ±0.01 of the unrounded reference, inclusive. Counts require the exact integer; no partial credit.
- Conventions stated in a question override defaults. Arrays use [row,column] = [y,x]; geometric vectors are columns; image-plane projection is virtual/front-facing; foreground is 1.
- This is original, challenging training material based on the supplied course files, not a lecturer-issued mock or a prediction of the exam.
"""


def write(relative, text):
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def literal_prose(text):
    """Keep formula operators visible while preserving authored code spans/fences."""
    pieces = re.split(r"(```.*?```|`[^`\n]*`)", text, flags=re.S)
    return "".join(piece if index % 2 else piece.replace("*", r"\*").replace("_", r"\_")
                   for index, piece in enumerate(pieces))


def prepare_exam(number):
    module = importlib.import_module(f"exam{number}")
    rng = random.Random(20261009 + number)
    slots = [0] * 8 + [1] * 8 + [2] * 7 + [3] * 7
    rng.shuffle(slots)
    prepared = []
    for index, original in enumerate(module.QUESTIONS, 1):
        q = dict(original, id=f"E{number}Q{index:02d}", number=index)
        if q["kind"] == "mc":
            wrong = list(q["distractors"])
            rng.shuffle(wrong)
            slot = slots[index - 1]
            wrong.insert(slot, q["correct"])
            q["options"] = wrong
            q["answer"] = LETTERS[slot]
            q["display_answer"] = q["answer"]
        else:
            q["display_answer"] = str(int(q["answer"])) if q["integer"] else f'{q["answer"]:.2f}'
        prepared.append(q)
    return {"number": number, "title": module.TITLE, "questions": prepared}


def render_exams(exams):
    for exam in exams:
        number = exam["number"]
        question_text = [f'# {exam["title"]}\n', "## Conditions\n", RULES,
                         "\nUse [the blank answer sheet](../answer-sheet.md). Solutions are in a separate folder; do not open them until you finish.\n",
                         "## Part A — Single-answer multiple choice\n"]
        solutions = [f'# Exam {number} — Answers and explanations\n',
                     f'Questions: [Exam {number}](../exams/exam-{number}.md). Source aliases: [coverage map](../COVERAGE.md). Convention warnings: [source notes](../SOURCE_NOTES.md).\n',
                     "## Quick key\n\n| Question | Answer | Question | Answer |\n|---|---|---|---|\n"]
        questions = exam["questions"]
        for left, right in zip(questions[:25], questions[25:]):
            solutions.append(f'| {left["number"]:02d} | {left["display_answer"]} | {right["number"]:02d} | {right["display_answer"]} |\n')
        solutions.append("\n## Worked solutions\n")
        for q in questions:
            if q["number"] == 31:
                question_text.append("\n## Part B — Numerical values\n")
            kind = "Multiple choice" if q["kind"] == "mc" else "Numerical"
            question_text.append(f'\n### Q{q["number"]:02d} — {kind}\n\n{literal_prose(q["stem"])}\n')
            if q["kind"] == "mc":
                for letter, option in zip(LETTERS, q["options"]):
                    question_text.append(f'\n- **{letter}.** {literal_prose(option)}\n')
            else:
                question_text.append("\n**Answer:** ____________________\n")
            solutions.append(f'\n### Q{q["number"]:02d} — {q["display_answer"]}\n\n')
            if q["kind"] == "mc":
                solutions.append(f'**{q["answer"]}. {literal_prose(q["correct"])}**\n\n')
            else:
                reference = str(q["answer"])
                solutions.append(f'**Submit {q["display_answer"]}.** Unrounded reference: `{reference}`.\n\n')
            solutions.append(f'{literal_prose(q["explanation"])}\n\n*Topic: {q["topic"]}. Sources: {literal_prose(q["source"])}.*\n')
        write(f"exams/exam-{number}.md", "".join(question_text))
        write(f"solutions/exam-{number}-solutions.md", "".join(solutions))
    write("data/exams.json", json.dumps(exams, ensure_ascii=False, indent=2) + "\n")
    rows = ["# Reusable answer sheet\n\nExam: ___   Date: ___   Time used: ___\n\n",
            "Record A–D for Q01–Q30 and one number for Q31–Q50. Mark low-confidence answers in the last column, but still answer them.\n\n",
            "| Q | Answer | Confidence / review note |\n|---|---|---|\n"]
    rows += [f"| {n:02d} | | |\n" for n in range(1, 51)]
    write("answer-sheet.md", "".join(rows))


def read_cards():
    cards = []
    for line_number, line in enumerate((ROOT / "data/cards.txt").read_text().splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = [s.strip() for s in line.split(" | ")]
        if len(parts) != 5:
            raise ValueError(f"cards.txt line {line_number}: expected 5 fields, got {len(parts)}")
        topic, priority, front, back, source = parts
        cards.append(dict(id=f"CV1-{len(cards)+1:03d}", topic=topic, priority=priority,
                          front=front, back=back, source=source))
    return cards


def render_cards(cards):
    # Three import fields. Source and stable ID are part of Back, not extra notes.
    with (ROOT / "flashcards-anki.tsv").open("w", encoding="utf-8", newline="") as handle:
        handle.write("#separator:Tab\n#html:false\n#tags column:3\n#columns:Front\tBack\tTags\n")
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        for c in cards:
            writer.writerow([c["front"], f'{c["back"]} [Sources: {c["source"]}. ID: {c["id"]}]',
                             f'cv1 topic::{c["topic"]} priority::{c["priority"]}'])
    grouped = {}
    for c in cards:
        grouped.setdefault(c["topic"], []).append(c)
    text = [f'# CV1 flashcards — {len(cards)} cards\n\n',
            "Each prompt tests one main fact or distinction. Try to answer before opening the back. Formulas use ordinary text, not rendered mathematics.\n\n",
            "**core** = direct emphasis in the lecturer checklist or a closely related calculation/failure mode. **breadth** = other taught content, supporting names and details. These labels are study priorities, not predictions.\n\n",
            "Import version: [Anki TSV](flashcards-anki.tsv). Source aliases: [coverage](COVERAGE.md). Conventions and source issues: [notes](SOURCE_NOTES.md).\n\n",
            "## Topics\n\n"]
    for topic, group in grouped.items():
        text.append(f'- [{topic}](#{topic}) — {len(group)} cards\n')
    for topic, group in grouped.items():
        text.append(f"\n## {topic}\n")
        for c in group:
            text.append(f'\n### {c["id"]} · {c["priority"]}\n\n**{literal_prose(c["front"])}**\n\n<details>\n<summary>Show answer</summary>\n\n{literal_prose(c["back"])}\n\n*Sources: {literal_prose(c["source"])}.*\n\n</details>\n')
    write("flashcards.md", "".join(text))
    write("data/flashcards.json", json.dumps(cards, ensure_ascii=False, indent=2) + "\n")


def render_topic_index(exams, cards):
    topics = list(dict.fromkeys(c["topic"] for c in cards))
    lines = ["# Topic index\n\n",
             "Use this after an attempt to find the flashcards for weak topics. Question numbers refer to the individual exam, not card IDs. Q01–Q30 are multiple choice; Q31–Q50 are numerical. Primary-topic tags do not list every secondary concept in a question.\n\n",
             "[Exam 1](exams/exam-1.md) · [Exam 2](exams/exam-2.md) · [Exam 3](exams/exam-3.md) · [Scope and sources](COVERAGE.md)\n\n",
             "| Topic / cards | Core | Breadth | Total | Exam 1 Q | Exam 2 Q | Exam 3 Q |\n",
             "|---|---:|---:|---:|---|---|---|\n"]
    for topic in topics:
        group = [c for c in cards if c["topic"] == topic]
        priorities = Counter(c["priority"] for c in group)
        qs = []
        for exam in exams:
            matches = [f'{q["number"]:02d}' for q in exam["questions"] if q["topic"] == topic]
            qs.append(", ".join(matches) if matches else "—")
        lines.append(f'| [{topic}](flashcards.md#{topic}) | {priorities["core"]} | {priorities["breadth"]} | {len(group)} | '+" | ".join(qs)+" |\n")
    counts = Counter(c["priority"] for c in cards)
    lines.append(f'\n**Total: {len(cards)} cards — {counts["core"]} core, {counts["breadth"]} breadth.** These priorities are study guidance, not exam probabilities.\n\n')
    lines.append("There is no question tagged primarily `coding`, but code/array interpretation and computation appear across the subject tags. `foundations` includes task definitions also used throughout the exams.\n")
    write("TOPIC_INDEX.md", "".join(lines))


def main():
    exams = [prepare_exam(n) for n in (1, 2, 3)]
    render_exams(exams)
    if "--exams-only" not in sys.argv:
        cards = read_cards()
        render_cards(cards)
        render_topic_index(exams, cards)
        print(f"Built 3 exams ({sum(len(e['questions']) for e in exams)} questions) and {len(cards)} cards.")
        print("Card counts:", dict(Counter(c["topic"] for c in cards)))
    else:
        print("Built 3 exams.")


if __name__ == "__main__":
    main()
