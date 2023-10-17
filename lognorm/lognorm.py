"""
"""

import numpy as np
import pandas as pd


class GCT:
    """
    """
    _delimiter = "\t"
    _header = 2
    _index_col = [0, 1]

    @classmethod
    def read(cls, path: str) -> pd.DataFrame:
        """
        :param path:
        :return:
        """
        return pd.read_table(
            path, delimiter=cls._delimiter, headers=cls._header, index_col=cls._index_col
        )
    
    @classmethod
    def write(cls, df: pd.DataFrame) -> str:
        """
        :param df:
        :param path:
        :return:
        """
        pass


def lognormalize(df: pd.DataFrame) -> pd.DataFrame:
    """
    :param df:
    :return:
    """
    df[df > 0] = np.log(df[df > 0])
    return df
