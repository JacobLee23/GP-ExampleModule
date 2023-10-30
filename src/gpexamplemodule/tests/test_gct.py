"""
Unit tests for :py:mod:`gpexamplemodule.gct`.
"""

import io
import urllib.request

import pandas as pd
import pytest

from gpexamplemodule.gct import GCT


@pytest.mark.parametrize(
    "path", [
        "https://datasets.genepattern.org/data/all_aml/all_aml_train.gct",
        "https://datasets.genepattern.org/data/test_data/BRCA_minimal_60x19.gct",
        "https://datasets.genepattern.org/data/test_data/BRCA_large_20783x40.gct"
    ]
)
class TestGCT:
    """
    Unit tests for :py:class:`GCT`.
    """
    def test_read(self, path: str):
        """
        Unit test for :py:path:`GCT.read`.
        """
        with urllib.request.urlopen(path) as response:
            version = response.readline().decode("utf-8").strip()
            assert version == GCT._version, path

            shape = tuple(map(int, response.readline().decode("utf-8").strip().split()))
            dataframe = GCT.read(path)
            assert shape == dataframe.shape, path

            columns = response.readline().decode("utf-8").strip().split()
            assert pd.Index(columns[2:]).equals(dataframe.columns), path
    
    def test_export(self, path: str):
        """
        Unit test for :py:meth:`GCT.export`.
        """
        with urllib.request.urlopen(path) as response:
            content = response.read()
            
        dataframe = GCT.read(path)

        with io.StringIO() as buffer:
            GCT.export(dataframe, buffer, lineterminator="\n")

            assert buffer.getvalue().encode() == content, path
