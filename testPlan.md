# 🐱 MishiTeX

**MishiTeX** is a command‑line tool that scaffolds LaTeX projects (books, papers, slides, etc.) with one command.  
It ships opinionated folder layouts, smart defaults, and a sprinkle of feline flair.

---

## 🎯 Goals
- **Instant scaffolding** – one command → working LaTeX project.
- **10+ template types** – book, thesis, CV, slides, …
- **Extensible** – drop new folders in `templates/`.
- **Beginner‑friendly** – emoji CLI, clear errors, docs.
- **Robust** – every template compiles; enforced by CI.
- **TDD first** – every feature arrives with a failing test.

---

## 🧩 Supported Templates
| Key          | Description                               |
|--------------|-------------------------------------------|
| `book`       | Book / class notes                        |
| `paper`      | Academic paper or conference submission   |
| `cv`         | Résumé or curriculum vitae                |
| `thesis`     | Thesis / dissertation                     |
| `homework`   | Problem sets / homework                   |
| `slides`     | Beamer presentations                      |
| `labreport`  | Scientific / lab report                   |
| `essay`      | Humanities essay                          |
| `worksheet`  | Math worksheets                           |
| `notebook`   | Research logbook                          |

---

## 🗂️ Repository Layout
```text
mishitex/
├── mishitex/               # Python package
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── scaffold.py         # Template logic
│   └── validate.py         # Template integrity checks
├── templates/              # One folder per template type
│   ├── book/
│   ├── thesis/
│   └── ...
├── tests/                  # Pytest test‑suite
│   ├── test_cli.py
│   ├── test_scaffold.py
│   ├── test_validate.py
│   └── fixtures/
├── docs/                   # MkDocs or Sphinx documentation
│   ├── index.md
│   └── contributing.md
├── README.md               # ← you are here
├── setup.py / pyproject.toml
└── .github/workflows/ci.yml
```

---

## 📋 Developer Requirements
- **Python ≥ 3.8**  
- `pytest` + `pytest‑cov` for testing  
- `black`, `isort`, `flake8` for style  
- (Optional) `jinja2` for future template variables  
- LaTeX tool‑chain (`pdflatex`) in CI image for compile tests  

> Create and activate a virtual environment before hacking:
> ```bash
> python -m venv .venv && source .venv/bin/activate
> pip install -e .[dev]
> ```

Dev extras are declared in *pyproject.toml*:
```toml
[project.optional-dependencies]
dev = [
  "pytest~=8.0",
  "pytest-cov",
  "black",
  "isort",
  "flake8",
  "jinja2",
]
```

---

## 🛤️ **Developer Roadmap – Test‑Driven**
The roadmap is broken into iterations.  **Each step starts by writing failing tests** in `tests/`, then implementing the minimal code to pass them.

| Phase | Objective | Write These Tests (fail first) | Implement | Acceptance Criteria |
|-------|-----------|--------------------------------|-----------|---------------------|
| **0 – Bootstrap** | Repo skeleton & CI baseline | • `tests/test_import.py` ensures `import mishitex` works.<br>• `tests/test_version.py` checks `mishitex.__version__` | • `__init__.py` with `__version__`<br>• GitHub Actions `ci.yml` running `pytest` | Green CI ✅ |
| **1 – CLI Parsing** | Basic `mishitex --help` & mandatory flags | • `test_cli.py::test_help_exits_0`<br>• `test_cli.py::test_requires_type_and_name` | • `cli.py` using `argparse`<br>• Entry‑point in `setup.py` (`console_scripts`) | `mishitex --help` prints usage; missing args returns `2`. |
| **2 – Scaffolding** | Copy template to target dir | • `test_scaffold.py::test_copies_template_tree` (use tmpdir)<br>• `test_scaffold.py::test_fails_if_exists` | • `scaffold.copy_template(src, dst)`<br>• Wire to CLI (`mishitex init`) | Directory created with all files; safe failure if exists. |
| **3 – Template Integrity** | Ensure template contains minimal files | • `test_validate.py::test_minimum_files_present`<br>• `test_validate.py::test_pdflatex_compiles` (optional, mark slow) | • `validate.check(template_path)`<br>• Add call in `scaffold` post‑copy | All templates pass check in CI. |
| **4 – Variable Substitution** | Inject title/author vars | • `test_jinja.py::test_variables_replaced` | • Integrate `jinja2` render in `scaffold` when `--vars` passed | `.tex` files contain rendered values. |
| **5 – Interactive Mode** | Prompt for missing info | • `test_cli.py::test_interactive_prompts` using `pexpect` | • CLI falls back to interactive questions | UX validated by test; help docs updated. |
| **6 – Docs & Packaging** | Publish docs & PyPI | • `docs` build in CI<br>• `pytest` ensures `python -m mishitex --version` returns string | • `mkdocs.yml` or `sphinx/`<br>• `setup.cfg` / `pyproject.toml` metadata | Versioned docs on GitHub Pages; `pip install mishitex` works. |

> **Tip for contributors**: run `pytest -q` before every commit; CI must stay ✅.

---

## 📰 Documentation Checklist
- [ ] `docs/index.md` – quick‑start & template gallery
- [ ] `docs/contributing.md` – coding conventions & branching strategy
- [ ] Each template has its own README describing structure & compile instructions.

---

## 🐱 Mascot – **Mishi the TeX Cat**
*Compila bonito o no compiles nada.*  
Mishi lurks in your terminal, catching missing braces before they cause chaos.

---

## 📜 License
MIT – do whatever, give credit, share knowledge.

---

Made with ❤️, `pytest`, and `\documentclass` by the MishiTeX team.



# 🧪 MishiTeX – Test Suite Plan

This file enumerates all tests referenced in the developer roadmap.
Each test name follows `tests/<file>::<test_function>` notation.

---

## Phase 0 – Bootstrap

* **tests/test\_import.py::test\_importable** — `import mishitex` succeeds.
* **tests/test\_version.py::test\_version\_string** — `mishitex.__version__` exists and is semantic‑version string.

## Phase 1 – CLI Parsing

* **tests/test\_cli.py::test\_help\_exits\_0** — `mishitex --help` exits with status 0 and prints usage.
* **tests/test\_cli.py::test\_requires\_type\_and\_name** — missing `--type` or `--name` returns exit 2.

## Phase 2 – Scaffolding

* **tests/test\_scaffold.py::test\_copies\_template\_tree** — `mishitex init --type book --name tmpdir` replicates full tree.
* **tests/test\_scaffold.py::test\_fails\_if\_exists** — same command over existing dir raises `FileExistsError`.

## Phase 3 – Template Integrity

* **tests/test\_validate.py::test\_minimum\_files\_present** — each template contains `main.tex`, `preamble.tex`, etc.
* **tests/test\_validate.py::test\_pdflatex\_compiles** *(slow)* — subprocess compile passes with no errors.

## Phase 4 – Variable Substitution

* **tests/test\_jinja.py::test\_variables\_replaced** — placeholders like `{{ author }}` are rendered in output.

## Phase 5 – Interactive Mode

* **tests/test\_cli.py::test\_interactive\_prompts** — using `pexpect`, ensure prompts appear when args omitted.

## Phase 6 – Docs & Packaging

* **tests/test\_cli.py::test\_version\_flag** — `mishitex --version` prints version.
* **tests/test\_docs.py::test\_docs\_build** — `mkdocs build` (or sphinx) completes without warnings.

---

> **Note**: Mark compile and docs tests with `pytest.mark.slow` so CI can selectively skip.
