import pytest
from loguru import logger


def pytest_addoption(parser):
    parser.addoption(
        "--loglevel",
        action="store",
        default="INFO",
        help="Set log level: DEBUG, INFO, WARNING, ERROR, CRITICAL",
    )


    logger.info("All tests finished.")
