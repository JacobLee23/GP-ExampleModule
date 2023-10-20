"""
Unit tests for :py:mod:`lognorm.gct`.
"""

import io
import urllib.request

import pandas as pd
import pytest

from lognorm.gct import GCT


@pytest.fixture(scope="module")
def gct(request: pytest.FixtureRequest) -> GCT:
    """
    :param request:
    :return:
    """
    return GCT(request.param)


@pytest.mark.parametrize(
    "gct", [
        "https://datasets.genepattern.org/data/all_aml/all_aml_train.gct",
        "https://datasets.genepattern.org/data/test_data/BRCA_minimal_60x19.gct",
        "https://datasets.genepattern.org/data/test_data/BRCA_large_20783x40.gct"
    ], indirect=True
)
class TestGCT:
    """
    Unit tests for :py:class:`GCT`.
    """
    def test_dataframe(self, gct: GCT):
        """
        Unit test for :py:attr:`GCT.dataframe`.
        """
        with urllib.request.urlopen(gct._source) as response:
            version = response.readline().decode("utf-8").strip()
            assert version == GCT._version, gct._source

            shape = tuple(map(int, response.readline().decode("utf-8").strip().split()))
            assert shape == gct.dataframe.shape, gct._source

            columns = response.readline().decode("utf-8").strip().split()
            assert pd.Index(columns[2:]).equals(gct.dataframe.columns), gct._source
    
    def test_export(self, gct: GCT):
        """
        Unit test for :py:meth:`GCT.export`.
        """
        with urllib.request.urlopen(gct._source) as response:
            content = response.read()
            
        with io.StringIO() as buffer:
            gct.export(buffer, lineterminator="\n")

            assert buffer.getvalue().encode() == content, gct._source
