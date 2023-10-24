"""
Applies a natural logarithmic transformation to the data in a GCT file and writes the transformed
data to a GCT file.
"""

import argparse
import datetime
import logging
import typing

from .gct import GCT
from .transform import log_normalize


class Parser(argparse.ArgumentParser):
    """
    Parser for command-line arguments.
    """
    def __init__(self):
        super().__init__(prog="lognorm", description=__doc__, epilog="5'-NGG-3'")

        self.add_argument(
            "-f", "--filename", type=str,
            help="Path of the file to read pre-processed GCT data from"
        )
        self.add_argument(
            "-o", "--output", type=str,
            help="Path to the file to write processed GCT data to"
        )

        self.add_argument(
            "-v", "--verbose", action="store_true",
            help="Increase verbosity (INFO)"
        )
        self.add_argument(
            "-d", "--debug", action="store_true",
            help="Increase verbosity (DEBUG)"
        )

        self._arguments = self.parse_args()

    def __getitem__(self, item: str) -> typing.Optional[typing.Any]:
        return self._arguments.__dict__[item]


def main() -> None:
    """
    Usage: python -m lognorm [-h] [-f FILENAME] [-o OUTPUT] [-v] [-d]
    """
    parser = Parser()

    logger = logging.getLogger(__name__)
    if parser["debug"]:
        logger.setLevel(logging.DEBUG)
    elif parser["verbose"]:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    exec_start = datetime.datetime.now()
    logger.info("Job initiated: %s", exec_start.strftime("%c"))

    logger.debug("Read GCT file from %s", parser["filename"])
    dataframe = GCT.read(parser["filename"])

    logger.debug("GCT data DataFrame shape: %s", dataframe.shape)

    logger.debug("Transform pre-processed GCT data using logarithmic normalization")
    dataframe = log_normalize(dataframe)

    logger.debug("Write processed GCT data to %s", parser["output"])
    output = GCT.write(dataframe, parser["output"])
    logger.debug("Processed GCT data written to %s", output)

    exec_end = datetime.datetime.now()
    logger.info("Job completed: %s", exec_end.strftime("%c"))

    logger.info("Execution time: %s", (exec_end - exec_start).total_seconds())
