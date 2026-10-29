"""The evaluation protocol (docs/PLAN.md section 9.1).

Every number in the README comes from code that imports these constants.
Changing a value here changes the benchmark, so it needs an ADR in docs/adr/.
"""

from typing import Final

import numpy as np
import numpy.typing as npt

DATASETS: Final = ("FD001", "FD002", "FD003", "FD004")

# Datasets with six operating regimes; settings are used only to find the regime.
MULTI_REGIME_DATASETS: Final = frozenset({"FD002", "FD004"})

SETTING_COLUMNS: Final = ("op1", "op2", "op3")
SENSOR_COLUMNS: Final = tuple(f"s{i}" for i in range(1, 22))

# Flat or near-flat on FD001; carry no degradation signal.
DROPPED_SENSORS: Final = frozenset({"s1", "s5", "s6", "s10", "s16", "s18", "s19"})

FEATURE_SENSORS: Final = tuple(s for s in SENSOR_COLUMNS if s not in DROPPED_SENSORS)

RUL_CAP: Final = 125
WINDOW_SIZE: Final = 30
WINDOW_SIZES_TO_TUNE: Final = (30, 40, 50)

# Five fixed seeds; every result is reported as mean +/- std over these.
SEEDS: Final = (0, 1, 2, 3, 4)

# Share of training engines held out, by engine, never by row.
VALIDATION_FRACTION: Final = 0.15
CALIBRATION_FRACTION: Final = 0.15


def cap_rul(rul: npt.ArrayLike, cap: int = RUL_CAP) -> npt.NDArray[np.float64]:
    """Piecewise-linear target: RUL is flat at `cap` early in life, then falls linearly."""
    values = np.asarray(rul, dtype=np.float64)
    if np.any(values < 0):
        raise ValueError("RUL cannot be negative")
    return np.minimum(values, float(cap))
