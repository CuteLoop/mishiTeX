import os
project_name = "mybook"

structure = {
    project_name: {
        "chapters": {
            "chapter1.tex": r"\chapter{Introduction}\nThis is the first chapter.",
            "chapter2.tex": r"\chapter{Second Chapter}\nMore content goes here."
        },
        "figures": {},
        "config": {
            "style-notes.tex": r"""\pagestyle{plain}
\setlength{\parskip}{1em}
\setlength{\parindent}{0pt}
\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue}
""",
            "style-print.tex": r"""\pagestyle{headings}
\setlength{\parskip}{0pt}
\setlength{\parindent}{1.5em}
\hypersetup{colorlinks=false}
"""
        },
        "main.tex": r"""\documentclass[11pt]{book}

\newif\ifnotes
\notestrue  % Change to \notesfalse for print

\input{preamble}

\ifnotes
  \input{config/style-notes}
\else
  \input{config/style-print}
\fi

\title{My Book Title}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle
\tableofcontents

\include{chapters/chapter1}
\include{chapters/chapter2}

\bibliographystyle{plain}
\bibliography{bibliography}

\end{document}
""",
        "preamble.tex": r"""\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{geometry}
\geometry{margin=1in}

\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\eps}{\varepsilon}
""",
        "bibliography.bib": r"% Add your references here",
        "README.md": "# My LaTeX Book Project\nThis repository contains a LaTeX setup for writing a book or class notes.",
        ".gitignore": "*.aux\n*.log\n*.toc\n*.out\n*.bbl\n*.blg\n*.pdf",
        "Makefile": r"""all:
\tpdflatex main.tex
\tbibtex main
\tpdflatex main.tex
\tpdflatex main.tex

clean:
\trm -f *.aux *.log *.toc *.bbl *.blg *.out
"""
    }
}

def write_structure(base, tree):
    for name, content in tree.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            write_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    write_structure(".", structure)
    print(f"✅ LaTeX book project '{project_name}' created successfully.")