# 🐱 MishiTeX

**MishiTeX** is a command-line tool to scaffold LaTeX projects for common academic and professional writing tasks. It helps users quickly generate structured LaTeX environments with clean organization, smart defaults, and a dash of feline flair.

---

## 🎯 Project Goals
- Provide clean, pre-structured LaTeX environments
- Support 10+ common use cases (thesis, slides, CV, etc.)
- Modular and extensible template system
- Beginner-friendly CLI with emoji feedback
- Easy integration of custom styles, macros, and configs

---

## 🧩 Use Cases Supported
| Type       | Description                              |
|------------|------------------------------------------|
| `book`     | Book or class notes                      |
| `paper`    | Academic paper or conference submission  |
| `cv`       | Resume or curriculum vitae               |
| `thesis`   | Thesis or dissertation                   |
| `homework` | Problem sets or homework                 |
| `slides`   | Beamer presentations                     |
| `labreport`| Scientific/lab report                    |
| `essay`    | Essay or humanities writing              |
| `worksheet`| Math handouts or worksheets              |
| `notebook` | Research notebook or logbook             |

---

## 🗂️ Repository Structure
```bash
mishitex/
├── mishitex/               # Python CLI package
│   ├── __init__.py
│   ├── cli.py              # CLI entrypoint logic
│   └── scaffold.py         # Core logic for project creation
├── templates/              # Template folders for each use case
│   ├── book/
│   ├── thesis/
│   └── ...
├── tests/                  # Unit tests for CLI and templates
├── README.md
├── mishitex.py             # CLI shortcut for local use
├── setup.py                # Install script
└── pyproject.toml          # Optional modern packaging
```

---

## 🧱 Template Layout (Example: `book/`)
```bash
templates/book/
├── main.tex                # Main entrypoint
├── preamble.tex            # Shared packages and settings
├── macros.tex              # Custom user commands
├── config/
│   ├── style-notes.tex     # Notes version
│   └── style-print.tex     # Print version
├── chapters/
│   ├── chapter1.tex
│   └── chapter2.tex
├── figures/
└── bibliography.bib        # BibTeX file
```

---

## 🎨 Styling and Commands
- `preamble.tex` — Load core packages and layout defaults
- `macros.tex` — User-defined commands like `\solution{}`
- `config/` — Optional toggles for different styling modes (e.g., notes vs print)

These are loaded in `main.tex` using `\input{}`.

---

## 🚀 Usage
```bash
mishitex init --type book --name "MyCourseNotes"
```
- Creates `MyCourseNotes/` with the `book` template
- Fails gracefully if directory already exists

---

## 🛠️ Future Enhancements
- Interactive prompts (e.g., title, author)
- Template variables using Jinja2-style placeholders
- GitHub Actions for LaTeX build verification
- VS Code LaTeX Workshop config bundling

---

## 🧪 Developer Notes
- Every template must compile with `pdflatex`
- Tests validate that key files like `main.tex` exist
- No PDFs or build artifacts should live in `templates/`

---

## 🐱 Mascot: Mishi the TeX Cat
**Mishi** is a clever academic feline who lives in your terminal and helps you compile beauty from chaos. When you're stuck with 17 open `egin{}`s, she's got your back.

**Lema**: *"Compila bonito o no compiles nada."*

---

## 📄 License
Licensed under the MIT License — free to use, remix, and share with attribution.

---

Made with ❤️ and `\documentclass` by the MishiTeX team.
