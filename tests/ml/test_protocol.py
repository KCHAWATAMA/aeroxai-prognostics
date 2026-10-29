import numpy as np
import pytest

from ml import protocol


def test_feature_sensors_exclude_flat_sensors() -> None:
    assert len(protocol.FEATURE_SENSORS) == 14
    assert not set(protocol.FEATURE_SENSORS) & protocol.DROPPED_SENSORS


def test_seeds_are_five_fixed_values() -> None:
    assert protocol.SEEDS == (0, 1, 2, 3, 4)


def test_held_out_fractions_leave_most_engines_for_training() -> None:
    assert protocol.VALIDATION_FRACTION + protocol.CALIBRATION_FRACTION < 0.5


def test_cap_rul_clips_at_cap() -> None:
    out = protocol.cap_rul([0, 50, 125, 200])
    np.testing.assert_array_equal(out, [0.0, 50.0, 125.0, 125.0])


def test_cap_rul_rejects_negative() -> None:
    with pytest.raises(ValueError, match="negative"):
        protocol.cap_rul([-1, 10])
