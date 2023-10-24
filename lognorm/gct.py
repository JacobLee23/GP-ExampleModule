"""
Interfaces for GCT file-handling.
"""

import csv
import io

import pandas as pd


class GCT:
    """
    Interface for GCT file-handling. Supports both reading from and writing to GCT files and
    conversions between GCT files and ``DataFrame`` representations of GCT data.
    """
    # GCT file-reading constants
    _version = "#1.2"
    _delimiter = "\t"
    _header = 2
    _index_col = [0, 1]

    @classmethod
    def read(cls, path: str) -> pd.DataFrame:
        """
        :param path: The path of the file to read pre-processed GCT data from
        :return: A ``DataFrame`` representation of the data contained in the input GCT file
        """
        return pd.read_table(
            path, delimiter=cls._delimiter, index_col=cls._index_col, header=cls._header
        )

    @classmethod
    def export(cls, dataframe: pd.DataFrame, buffer: io.TextIOBase, **kwargs) -> None:
        """
        Writes the contents of a ``DataFrame`` to ``buffer`` in GCT format.

        :param dataframe: A ``DataFrame`` representation of the GCT data to output
        :param buffer: A text stream
        """
        buffer.write(f"{cls._version}\n")
        buffer.write(f"{cls._delimiter.join(map(str, dataframe.shape))}\n")

        dataframe.to_csv(buffer, sep=cls._delimiter, quoting=csv.QUOTE_NONE, **kwargs)

    @classmethod
    def write(cls, dataframe: pd.DataFrame, path: str) -> str:
        """
        Writes the contents of a ``DataFrame`` to a GCT file located at ``path``.

        :param path: The path to the file to write processed GCT data to
        :return: The path of the file to which the processed GCT data was written
        """
        with open(path, "w", encoding="utf-8", newline="") as file:
            cls.export(dataframe, file)

        return path
