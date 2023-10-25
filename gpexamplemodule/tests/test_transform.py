"""
Unit tests for :py:mod:`gpexamplemodule.transform`.
"""

import numpy as np
import pytest

from gpexamplemodule import transform


@pytest.mark.parametrize(
    ("array", "expected"), [
        (np.array([1], dtype=np.float64), np.array([0], dtype=np.float64)),
        (np.array([0], dtype=np.float64), np.array([0], dtype=np.float64)),
        (np.array([-1], dtype=np.float64), np.array([-1], dtype=np.float64)),
        (np.array([np.e], dtype=np.float64), np.array([1], dtype=np.float64)),
        (np.array([-np.e], dtype=np.float64), np.array([-np.e], dtype=np.float64)),

        (np.array([1, np.e, np.e ** 2], dtype=np.float64), np.array([0, 1, 2], dtype=np.float64)),
        (np.array([-np.e ** 2, -np.e, -1], dtype=np.float64), np.array([-np.e ** 2, -np.e, -1], dtype=np.float64)),
        (np.array([0, 1, np.e, np.e ** 2, np.e ** 3], dtype=np.float64), np.array([0, 0, 1, 2, 3], dtype=np.float64)),
        (np.array([-np.e ** 3, -np.e ** 2, -np.e, -1, 0], dtype=np.float64), np.array([-np.e ** 3, -np.e ** 2, -np.e, -1, 0], dtype=np.float64)),
        (np.array([-np.e, -1, 0, 1, np.e], dtype=np.float64), np.array([-np.e, -1, 0, 0, 1], dtype=np.float64)),

        (np.arange(1, 101, dtype=np.float64), np.log(np.arange(1, 101, dtype=np.float64))),
        (np.arange(-100, 1, dtype=np.float64), np.arange(-100, 1, dtype=np.float64)),
        (np.e ** np.arange(1, 101), np.arange(1, 101, dtype=np.float64)),
        (-np.e ** np.arange(-100, 1, dtype=np.float64), -np.e ** np.arange(-100, 1, dtype=np.float64)),
    ]
)
def test_log_normalize(array: np.ndarray, expected: np.ndarray):
    """
    Unit test for :py:func:`transform.log_normalize`.
    """
    assert np.array_equal(transform.log_normalize(array), expected), array
