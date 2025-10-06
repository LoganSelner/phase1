![CI](https://github.com/LoganSelner/phase1/actions/workflows/ci.yml/badge.svg)

# DSA Labs

A minimal python sandbox that uses **[uv](https://github.com/astral-sh/uv)** for dependency and virtualenv management, **pre-commit** for quality gates, and a clean `src/` layout.

---

## Features

* 🧪 **Tests** via `pytest` (see `tests/test_app.py`)
* 🧰 **uv** for fast, reproducible installs (`pyproject.toml` + `uv.lock`)
* 🧹 **pre-commit** hooks: ruff, black, and more
* 🗂️ `src/` layout with `algos` package

---

## Prerequisites

* **Python 3.13** (a `.python-version` file is included if you use pyenv)
* **uv** (once per machine). Install options:

  * macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  * Windows (PowerShell): `irm https://astral.sh/uv/install.ps1 | iex`

---

## Quickstart (local dev)

```bash
make bootstrap
# → installs a compatible Python, syncs deps (incl. dev), installs git hooks

make qa
# (non-mutating) fmt-check + typecheck + pytest
```

### One-liners you’ll use a lot

```bash
# Run tests
uv run pytest

# Type-check
uv run mypy

# Lint + format (non-destructive checks)
uv run ruff check . && uv run black --check .

# Apply fixes (imports -> ruff, then black)
uv run ruff check --fix . && uv run black .

```

---

## Makefile shortcuts

Run `make help` to see everything. Common targets:

| Target                | What it does                                             |
| --------------------- | -------------------------------------------------------- |
| `make bootstrap`      | Install Python (if needed), sync deps, install git hooks |
| `make update`         | Upgrade locked package versions (respecting constraints) |
| `make env`            | Print tool versions                                      |
| `make test`           | Run pytest                                               |
| `make fmt`            | Apply formatting fixes (ruff imports → black)            |
| `make fmt-check`      | Non-mutating QA check for CI/local                       |
| `make lint`           | Ruff lint                                                |
| `make typecheck`      | Mypy                                                     |
| `make qa`             | Full quality gate (lint+format+types+tests)              |
| `make clean`          | Remove caches                                            |
| `make deep-clean`     | Also remove build artifacts                              |

---

## Project layout

```
.
├─ src/algos/
│  ├─ __init__.py
│  └─ *.py             # Algorithm code
├─ tests/
│  └─ test_*.py        # tests
├─ pyproject.toml      # deps, tool config, build backend
├─ uv.lock             # lockfile (commit this)
├─ Makefile            # dev workflow
└─ README.md

```

---

## pre-commit (quality gates)

This repo is configured to run a suite of checks (ruff, black, etc.).

* Run once on all files:

  ```bash
  uv run pre-commit run --all-files
  ```
* Install into your git hooks (so it runs automatically on commit):

  ```bash
  uv run pre-commit install
  ```


---

## Troubleshooting

* **No files to check**

  * Only tracked files are checked. git add -A, or run make fmt.
* **Python version mismatch**

  * This project targets **Python 3.13**. If you’re on another version, use pyenv or update your interpreter.
* **Fresh env**

  ```bash
  rm -rf .venv
  make bootstrap
  ```
