# ADR 0001: v2 foundations

- Status: accepted
- Date: 2026-10-29

## Context

v1 (the dissertation build) reported an RMSE it could not reproduce (13.12 claimed, 14.00 on the
official test), measured uncertainty on a different model from the one served, and ran a circular
"digital twin". v2 is a rebuild in a new repo, not a patch.

## Decisions

| Topic | Decision | Reason |
|---|---|---|
| Framework | PyTorch | Most common in ML job adverts and research code; v1's Keras model is retrained anyway. |
| N-CMAPSS | v3 | v2 ships FD001–FD004 properly first; N-CMAPSS (~15 GB) would delay the first release. |
| Name | AeroXAI, repo `aeroxai-prognostics` | Continuity with the dissertation and CV. |
| v1 | Frozen, untouched | Safe whether or not the dissertation is final. |
| Pace | ~15 h/week, ~10 weeks | At 10 h/week, ~14 weeks; gates unchanged. |
| Old repo | Public, tag `v1-dissertation`, archive at v2 launch, README points to v2 | Shows the v1 → v2 progression. |
| Uncertainty | Split-conformal intervals on the served model | Coverage can be checked; v1's MC dropout was on the wrong model. |
| Hosting | Google Cloud Run, scale to zero | Cheap for a demo, HTTPS by default, fits the Google stack. |

## Consequences

Python 3.12 + uv, Ruff, mypy strict, pytest with 80% coverage from day one. The evaluation
protocol lives in `ml/protocol.py` and changes only through a new ADR.
