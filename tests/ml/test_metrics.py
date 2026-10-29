import math

import pytest

from ml.metrics import interval_coverage, nasa_score, rmse


def test_rmse_known_value() -> None:
    assert rmse([0, 0], [3, 4]) == pytest.approx(math.sqrt(12.5))


def test_rmse_perfect_is_zero() -> None:
    assert rmse([10, 20], [10, 20]) == 0.0


def test_nasa_score_penalises_late_more_than_early() -> None:
    late = nasa_score([50], [60])
    early = nasa_score([50], [40])
    assert late == pytest.approx(math.e - 1)
    assert early == pytest.approx(math.exp(10 / 13) - 1)
    assert late > early


def test_shape_mismatch_raises() -> None:
    with pytest.raises(ValueError, match="shape"):
        rmse([1, 2], [1])


def test_empty_input_raises() -> None:
    with pytest.raises(ValueError, match="empty"):
        nasa_score([], [])


def test_interval_coverage() -> None:
    assert interval_coverage([5, 15, 25], [0, 0, 0], [10, 10, 30]) == pytest.approx(2 / 3)


def test_interval_coverage_rejects_inverted_bounds() -> None:
    with pytest.raises(ValueError, match="lower"):
        interval_coverage([5], [10], [0])
