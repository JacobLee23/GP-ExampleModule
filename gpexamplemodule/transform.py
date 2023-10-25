"""
Transformations for ``ndarray`` objections.
"""

import numpy as np


def log_normalize(
    array: np.ndarray[None, np.dtype[np.float64]]
) -> np.ndarray[None, np.dtype[np.float64]]:
    r"""
    Applies a natural logarithmic transformation on the nonzero elements of an array:

    .. math::

        {A}_{(i, j, ...)} = \begin{cases}
            [{a}_{(i, j, ...)}] & [{a}_{(i, j, ...)}] \leq 0 \\
            \ln([{a}_{(i, j, ...)}]) & [{a}_{(i, j, ...)}] > 0
        \end{cases}

    :param array: The ``ndarray`` to transform
    :return: The transformed array
    """
    array[array > 0] = np.log(array[array > 0])
    return array
