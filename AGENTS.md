# AeroXAI Prognostics: agent rules

These rules apply to every agent (Antigravity, Claude Code, or any other) working in this repo.
Detailed rules live in `.agents/rules/`; repeatable tasks in `.agents/workflows/`.

## Before any task
- Read `docs/PLAN.md`. Work only on the current phase; anything else goes in PLAN.md first.
- For changes touching more than ~3 files, show a plan and wait for approval.

## Non-negotiables
- The evaluation protocol is `ml/protocol.py` (PLAN section 9.1). Do not change it without an ADR in `docs/adr/`.
- The official test set (`test_FD00x.txt`, `RUL_FD00x.txt`) is read only by `ml/evaluate_final.py`.
- Splits are by engine, never by row. Scalers are fitted on training engines only.
- No number goes in the README unless `make benchmark` produced it.
- No secrets in code or git. Config comes from environment variables (`api/settings.py`).

## Code standards
- Python 3.12, managed with uv. Type hints everywhere; `ruff` and `mypy --strict` must pass.
- Every new function gets a pytest test. Coverage on `ml/` and `api/` stays >= 80%.
- Never mark a task done with failing checks. Run `make check` (or the uv commands in the Makefile).
- Files stay under 300 lines; `api/main.py` under 150. Split modules instead.
- Deep learning uses PyTorch.
- Frontend (Phase 5): Next.js + TypeScript strict + Tailwind; three pages only (Fleet, Engine, Model card).

## Git
- Small commits, one slice each, with a message saying what and why.
- Never commit data, model files, `.env`, or keys.
