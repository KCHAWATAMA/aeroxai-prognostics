# AeroXAI Prognostics

Remaining-useful-life (RUL) prediction for turbofan engines, with honest uncertainty intervals and
explanations, served as a fleet health console on Google Cloud.

> **Status: Phase 0 (foundations).** No model yet. Results, live demo link and screenshots arrive in
> later phases. v1 (the dissertation version) is frozen at
> [KCHAWATAMA/aircraft-engine-predictive-maintenance](https://github.com/KCHAWATAMA/aircraft-engine-predictive-maintenance).

## What it will do

- Rank a fleet of engines by predicted RUL, with a calibrated interval for each.
- Explain each prediction by sensor and by time, and check the explanations are faithful.
- Answer questions about an engine with a Gemini assistant that only sees the computed numbers.

## Data

NASA C-MAPSS FD001–FD004. N-CMAPSS is planned for v3. The evaluation protocol is fixed in
[`ml/protocol.py`](ml/protocol.py) and [docs/PLAN.md](docs/PLAN.md).

## Run it

Needs [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run pytest
uv run uvicorn api.main:app --reload
```

With `make`: `make setup`, `make check`, `make serve`.

## Layout

```text
ml/        offline pipeline: data, features, models, benchmark, conformal, explain
api/       FastAPI service
web/       Next.js console (Phase 5)
infra/     Dockerfiles and Cloud Run config (Phase 7)
tests/     pytest suites mirroring ml/ and api/
docs/      plan, model card, decision records
.agents/   Antigravity rules and workflows
```

## License

MIT
