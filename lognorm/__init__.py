"""
"""

import sys

from .gct import GCT
from .lognorm import log_normalize


def main():
    _, source, destination = sys.argv

    gct = GCT(source)
    gct.dataframe = log_normalize(gct.dataframe)
    gct.write(destination)
