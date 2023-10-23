"""
"""

import numpy as np


def log_normalize(
    array: np.ndarray[None, np.dtype[np.float64]]
) -> np.ndarray[None, np.dtype[np.float64]]:
    """
    :param df:
    :return:
    """
    array[array > 0] = np.log(array[array > 0])
    return array
