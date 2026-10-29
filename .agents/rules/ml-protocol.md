---
trigger: glob
globs: ml/**/*.py
description: Leakage and evaluation rules for the ML pipeline
---

# ML protocol rules

- Import constants from `ml/protocol.py`; never hard-code RUL cap, window size, seeds or dropped sensors.
- Split train/validation/calibration by engine ID. Assert no engine appears in two splits.
- Fit scalers and regime clustering on training engines only, then apply to the rest.
- FD002/FD004: operating settings identify the regime; they are not model inputs.
- Report every metric as mean +/- std over `protocol.SEEDS`.
- The official test files are opened only in `ml/evaluate_final.py`.
- Metrics come from `ml/metrics.py`. Add a new metric there with a test, not inline.
