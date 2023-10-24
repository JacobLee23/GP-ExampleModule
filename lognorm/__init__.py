"""
"""

import argparse
import datetime
import logging
import typing

from .gct import GCT
from .lognorm import log_normalize


class Parser(argparse.ArgumentParser):
    """
    """
    def __init__(self):
        super().__init__(prog="lognorm", description=__doc__, epilog="5'-NGG-3'")

        self.add_argument(
            "-f", "--filename", type=str,
            help=""
        )
        self.add_argument(
            "-o", "--output", type=str,
            help=""
        )

        self.add_argument(
            "-v", "--verbose", action="store_true",
            help=""
        )
        self.add_argument(
            "-d", "--debug", action="store_true",
            help=""
        )

        self._arguments = self.parse_args()

    def __getitem__(self, item: str) -> typing.Optional[typing.Any]:
        return self.arguments[item]
    
    @property
    def arguments(self) -> typing.Dict[str, typing.Any]:
        """
        """
        return self._arguments.__dict__


def main() -> None:
    parser = Parser()

    logger = logging.getLogger("lognorm")
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

    logger.debug("Reading GCT file from %s", parser["filename"])
    gct = GCT(parser["filename"])
    logger.debug("GCT data read from %s", gct._source)
    
    logger.debug("GCT data DataFrame shape: %s", gct.dataframe.shape)

    logger.debug("Log-normalizing pre-processed GCT data")
    gct.dataframe = log_normalize(gct.dataframe)

    logger.debug("Writing processed GCT data to %s", parser["output"])
    output = gct.write(parser["output"])
    logger.debug("Processed GCT data written to %s", output)

    exec_end = datetime.datetime.now()
    logger.info("Job completed: %s", exec_end.strftime("%c"))

    logger.info("Execution time: %s", (exec_end - exec_start).total_seconds())
