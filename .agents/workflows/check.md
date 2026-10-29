---
description: Run every local check before calling a task done
---

1. Run `uv sync`.
2. Run `uv run ruff format .` then `uv run ruff check . --fix`.
3. Run `uv run mypy` and fix every error.
4. Run `uv run pytest` and make sure coverage stays at or above 80%.
5. Report the results as a short Artifact: what passed, anything you had to fix.
