"""Metrics used in the benchmark (docs/PLAN.md section 9.3)."""

import numpy as np
import numpy.typing as npt


def _pair(
    y_true: npt.ArrayLike, y_pred: npt.ArrayLike
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    true = np.asarray(y_true, dtype=np.float64)
    pred = np.asarray(y_pred, dtype=np.float64)
    if true.shape != pred.shape:
        raise ValueError(f"shape mismatch: {true.shape} vs {pred.shape}")
    if true.size == 0:
        raise ValueError("empty input")
    return true, pred


def rmse(y_true: npt.ArrayLike, y_pred: npt.ArrayLike) -> float:
    true, pred = _pair(y_true, y_pred)
    return float(np.sqrt(np.mean((pred - true) ** 2)))


def nasa_score(y_true: npt.ArrayLike, y_pred: npt.ArrayLike) -> float:
    """PHM08 asymmetric score: late predictions (d > 0) cost more than early ones."""
    true, pred = _pair(y_true, y_pred)
    d = pred - true
    penalties = np.where(d < 0, np.exp(-d / 13.0) - 1.0, np.exp(d / 10.0) - 1.0)
    return float(np.sum(penalties))


def interval_coverage(y_true: npt.ArrayLike, lower: npt.ArrayLike, upper: npt.ArrayLike) -> float:
    """Share of true values inside [lower, upper]."""
    true, lo = _pair(y_true, lower)
    _, hi = _pair(y_true, upper)
    if np.any(lo > hi):
        raise ValueError("lower bound above upper bound")
    return float(np.mean((true >= lo) & (true <= hi)))
