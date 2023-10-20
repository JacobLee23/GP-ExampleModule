"""
"""

import io
import sys

import pandas as pd


class GCT:
    """
    :param path:
    """
    _version = "#1.2"
    _delimiter = "\t"
    _header = 2
    _index_col = [0, 1]

    def __init__(self, source: str):
        self._source = source

        self._dataframe = pd.read_table(
            self._source, delimiter=self._delimiter, index_col=self._index_col,
            header=self._header
        )

    @property
    def dataframe(self) -> pd.DataFrame:
        """
        """
        return self._dataframe

    @dataframe.setter
    def dataframe(self, value: pd.DataFrame) -> None:
        """
        """
        self._dataframe = value

    def export(self, buffer: io.TextIOBase):
        """
        :param buffer:
        """
        buffer.write(self._version)
        buffer.write(f"{self._delimiter.join(map(str, self.dataframe.shape))}\n")

        self.dataframe.to_csv(buffer, sep=self._delimiter)

    def write(self, path: str):
        """
        :param path:
        """
        with open(path, "w", encoding="utf-8", newline="") as file:
            self.export(file)
