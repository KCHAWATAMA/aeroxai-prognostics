# One command per job. On Windows without make, run the uv commands directly.
.PHONY: setup lint typecheck test check serve

setup:
	uv sync

lint:
	uv run ruff check .
	uv run ruff format --check .

typecheck:
	uv run mypy

test:
	uv run pytest

check: lint typecheck test

serve:
	uv run uvicorn api.main:app --reload --port 8000
