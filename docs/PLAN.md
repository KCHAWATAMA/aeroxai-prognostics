# AeroXAI Prognostics: working plan

The full analysis and master plan is the online doc
[AeroXAI Rebuild — Analysis & Master Plan](https://claude.ai/artifact/7dWAR6jXpP2FECDvDj7Atw).
This file is the short version agents read before every task. If the two disagree, update this file.

**Current phase: 0 (Reset)**

## Goal

A live fleet health console that predicts RUL for C-MAPSS engines, shows a calibrated interval and an
explanation for every prediction, and is deployed on Google Cloud Run with CI/CD.

## Phases and gates

A phase ends only when its gate passes. About 15 hours a week.

| # | Phase | Weeks | Work | Gate |
|---|---|---|---|---|
| 0 | Reset | 1 | New repo, AGENTS.md, PLAN.md, CI skeleton; tag and archive v1 later | CI green on empty repo |
| 1 | Data and protocol | 2 | `data.py`, `features.py`, engine-wise splits, leakage tests | Leakage tests pass |
| 2 | Benchmark | 3–4 | 6 models x 5 seeds on FD001–FD004; MLflow tracking | Benchmark reproducible |
| 3 | Intervals and explanations | 5 | Split-conformal 90% intervals; attributions + deletion test | Coverage 87–93% on FD001 |
| 4 | API | 6 | FastAPI: fleet, engine, predict, replay; Firestore state | Contract tests pass |
| 5 | Web app | 7–8 | Fleet, Engine and Model card pages; Next.js + TypeScript | Playwright smoke passes |
| 6 | Assistant | 9 | Gemini Flash grounded on API facts; rate limits | No invented numbers in tests |
| 7 | Deploy and ship | 10 | Cloud Run, CI/CD via Workload Identity, README, demo video | Public URL live |

## Evaluation protocol (section 9.1, frozen)

Encoded in [`ml/protocol.py`](../ml/protocol.py). Changing it needs an ADR.

1. Data: C-MAPSS FD001–FD004 from the NASA files; raw files never modified.
2. Features: drop the 7 flat sensors (s1, s5, s6, s10, s16, s18, s19); operating settings only identify regimes (FD002/FD004).
3. Scaling: fitted on training engines only; per regime for FD002/FD004.
4. Target: RUL capped at 125.
5. Windows: 30 cycles (40 and 50 tried as a hyper-parameter).
6. Splits: engine-wise, 5 fixed seeds; validation engines never seen in training.
7. Calibration set for conformal intervals: a separate slice of training engines.
8. Test: the official last window per test engine against `RUL_FD00x.txt`; touched once per final model.

## Decisions (29 Oct 2026)

See [docs/adr/0001-v2-foundations.md](adr/0001-v2-foundations.md).

## Won't do in v2

Login, multiple user roles, a "digital twin" that generates sensors from predicted RUL, N-CMAPSS
(moved to v3), more than three web pages.
