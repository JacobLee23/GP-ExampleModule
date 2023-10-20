"""
"""

import numpy as np
import pandas as pd


def log_normalize(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df:
    :return:
    """
    df[df > 0] = np.log(df[df > 0])
    return df
