"""Create six standalone LaTeX sources and compile separate question/solution PDFs."""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata

from build import RULES

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "latex"
PDF = ROOT / "pdf"
BUILD = Path("/tmp/opencode/cv1-study-pack-latex")

ESCAPES = {
    "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
    "$": r"\$", "&": r"\&", "#": r"\#", "%": r"\%",
    "_": r"\_\allowbreak{}", "^": r"\textasciicircum{}", "~": r"\textasciitilde{}",
    "=": r"=\allowbreak{}", "*": r"*\allowbreak{}", "/": r"/\allowbreak{}",
    ",": r",\allowbreak{}", "|": r"|\allowbreak{}",
}


def escape(text):
    return "".join(ESCAPES.get(char, char) for char in str(text))


def inline(text):
    parts = re.split(r"(`[^`\n]+`|\*\*.*?\*\*)", text)
    output = []
    for part in parts:
        if part.startswith("`"):
            output.append(r"\texttt{" + escape(part[1:-1]) + "}")
        elif part.startswith("**"):
            output.append(r"\textbf{" + escape(part[2:-2]) + "}")
        else:
            output.append(escape(part))
    return "".join(output)


def prose(text):
    output = []
    for part in re.split(r"(```[^\n]*\n.*?\n```)", text, flags=re.S):
        if part.startswith("```"):
            code = part.split("\n", 1)[1].rsplit("\n```", 1)[0]
            output.append("\n\\begin{Code}\n" + code + "\n\\end{Code}\n")
        else:
            output.append(inline(part))
    return "".join(output)


def preamble(title, subtitle, header):
    return r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=20mm,headheight=15pt]{geometry}
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setmonofont{DejaVu Sans Mono}[Scale=0.82]
\usepackage{microtype}
\usepackage{enumitem}
\usepackage{fvextra}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{fancyhdr}
\usepackage[hidelinks]{hyperref}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\setlength{\emergencystretch}{3em}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\raggedright
\DefineVerbatimEnvironment{Code}{Verbatim}{fontsize=\small,
  breaklines=true,breakanywhere=true,breaksymbolleft={},breaksymbolright={},
  frame=single,framesep=5pt}
\setlist[enumerate]{leftmargin=7mm,itemsep=3pt,topsep=5pt,parsep=0pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Computer Vision 1}
\fancyhead[R]{\small """ + escape(header) + r"""}
\fancyfoot[C]{\small \thepage}
\hypersetup{pdftitle={""" + escape(title) + r"""},pdfsubject={CV1 practice material}}
\begin{document}
{\LARGE\bfseries """ + escape(title) + r"""}\par
{\large """ + escape(subtitle) + r"}\par\bigskip" + "\n"


def question_block(number, label, content):
    # All questions fit on one page; keep their code and answer choices together.
    return (r"\begin{minipage}{\linewidth}" + "\n"
            + r"\textbf{Q" + f"{number:02d}" + " — " + escape(label) + r"}\par\smallskip" + "\n"
            + content + "\n\\end{minipage}\n\\par\\vspace{12pt}\n")


def exam_document(exam):
    title = exam["title"]
    output = [preamble(title, "Questions only", f'Exam {exam["number"]} · Questions'),
              r"\textbf{Name:} \rule{70mm}{0.4pt}\hfill \textbf{Date:} \rule{30mm}{0.4pt}" + "\n",
              r"\section*{Conditions}" + "\n", r"\begin{itemize}[leftmargin=5mm,itemsep=5pt]" + "\n"]
    for rule in RULES.strip().splitlines():
        output.append(r"\item " + inline(rule.removeprefix("- ")) + "\n")
    output += [r"\end{itemize}" + "\n",
               "Solutions are in a separate PDF. Do not open them until you finish.\n",
               r"\clearpage\section*{Part A — Single-answer multiple choice}" + "\n"]
    for q in exam["questions"]:
        if q["number"] == 31:
            output.append(r"\clearpage\section*{Part B — Numerical values}" + "\n")
        body = prose(q["stem"]) + "\n"
        if q["kind"] == "mc":
            body += r"\begin{enumerate}[label=\textbf{\Alph*.}]" + "\n"
            body += "".join(r"\item " + prose(option) + "\n" for option in q["options"])
            body += r"\end{enumerate}"
        else:
            body += r"\par\medskip\textbf{Answer:} \rule{55mm}{0.4pt}"
        output.append(question_block(q["number"], "Multiple choice" if q["kind"] == "mc" else "Numerical", body))
    return "".join(output) + "\n\\end{document}\n"


def solution_document(exam):
    number = exam["number"]
    output = [preamble(f"Exam {number} — Solutions", exam["title"].split(" — ", 1)[1],
                       f"Exam {number} · Solutions"),
              "Answer key and worked explanations. Source aliases and convention warnings are listed in "
              r"\texttt{COVERAGE.md} and \texttt{SOURCE\_NOTES.md} in the study pack." + "\n",
              r"\section*{Quick key}" + "\n",
              r"\begin{longtable}{@{}r l@{\hspace{25mm}}r l@{}}" + "\n",
              r"\toprule Question & Answer & Question & Answer \\ \midrule" + "\n"]
    for left, right in zip(exam["questions"][:25], exam["questions"][25:]):
        output.append(f'{left["number"]:02d} & {escape(left["display_answer"])} & '
                      f'{right["number"]:02d} & {escape(right["display_answer"])}' + r" \\" + "\n")
    output += [r"\bottomrule\end{longtable}" + "\n",
               r"\clearpage\section*{Worked solutions}" + "\n"]
    for q in exam["questions"]:
        if q["kind"] == "mc":
            body = r"\textbf{" + escape(q["answer"] + ". " + q["correct"]) + r"}\par" + "\n"
        else:
            body = (r"\textbf{Submit " + escape(q["display_answer"]) + ".} "
                    + "Unrounded reference: " + r"\texttt{" + escape(q["answer"]) + r"}.\par" + "\n")
        body += prose(q["explanation"]) + r"\par" + "\n"
        body += r"{\small\itshape Topic: " + escape(q["topic"]) + ". Sources: " + escape(q["source"]) + ".}\n"
        output.append(question_block(q["number"], q["display_answer"], body))
    return "".join(output) + "\n\\end{document}\n"


def normalized(text):
    # Ignore layout whitespace and typographic apostrophes/ligatures, not operators.
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text).replace("’", "'"))


def source_text(text):
    # Strip Markdown only outside fences: '**' inside Python is exponentiation.
    parts = []
    for part in re.split(r"(```[^\n]*\n.*?\n```)", text, flags=re.S):
        if part.startswith("```"):
            parts.append(part.split("\n", 1)[1].rsplit("\n```", 1)[0])
        else:
            parts.append(part.replace("`", "").replace("**", ""))
    return "".join(parts)


def compile_and_check(job):
    tex_path, exam, solutions = job
    work = BUILD / tex_path.stem
    work.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
                             f"-outdir={work}", str(tex_path)], cwd=TEX,
                            capture_output=True, text=True)
    (work / "build-output.txt").write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f"LaTeX failed for {tex_path}; inspect {work / 'build-output.txt'}")
    log = (work / (tex_path.stem + ".log")).read_text()
    for problem in ("Overfull", "Missing character:"):
        if problem in log:
            raise RuntimeError(f"{problem} in {work / (tex_path.stem + '.log')}")
    artifact = work / (tex_path.stem + ".pdf")
    text = subprocess.check_output(["pdftotext", "-layout", str(artifact), "-"], text=True)
    headings = re.findall(r"^\s*Q(\d{2})\s+—", text, flags=re.M)
    if headings != [f"{n:02d}" for n in range(1, 51)]:
        raise AssertionError(f"Missing/reordered PDF questions: {tex_path}")
    visible = normalized(text)
    for q in exam["questions"]:
        required = [q["explanation"], q["source"]] if solutions else [q["stem"]]
        required += [q["correct"]] if solutions and q["kind"] == "mc" else []
        required += q["options"] if not solutions and q["kind"] == "mc" else []
        for value in required:
            if normalized(source_text(value)) not in visible:
                raise AssertionError(f"PDF content mismatch: {tex_path.name} {q['id']}: {value[:90]}")
    if not solutions:
        assert "Unrounded reference" not in text and "Worked solutions" not in text
    destination = PDF / artifact.name
    shutil.copy2(artifact, destination)
    info = subprocess.check_output(["pdfinfo", str(destination)], text=True)
    pages = re.search(r"^Pages:\s+(\d+)", info, flags=re.M).group(1)
    return f"PASS: {destination.relative_to(ROOT)} — {pages} pages; all 50 questions and content verified."


def main():
    TEX.mkdir(exist_ok=True)
    PDF.mkdir(exist_ok=True)
    exams = json.loads((ROOT / "data/exams.json").read_text())
    jobs = []
    for exam in exams:
        for solutions in (False, True):
            suffix = "-solutions" if solutions else ""
            path = TEX / f'exam-{exam["number"]}{suffix}.tex'
            path.write_text(solution_document(exam) if solutions else exam_document(exam))
            jobs.append((path, exam, solutions))
    with ThreadPoolExecutor(max_workers=3) as pool:
        for message in pool.map(compile_and_check, jobs):
            print(message)


if __name__ == "__main__":
    main()
