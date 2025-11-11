import pytest
from loguru import logger


def pytest_addoption(parser):
    parser.addoption(
        "--loglevel",
        action="store",
        default="INFO",
        help="Set log level: DEBUG, INFO, WARNING, ERROR, CRITICAL",
    )


@pytest.fixture(scope="session", autouse=True)
def setup_logger(request):
    log_level = request.config.getoption("--loglevel").upper()

    logger.remove()
    logger.add("test_log.log", level=log_level, rotation="1 MB", compression="zip")
    logger.info(f"Logger initialized with level {log_level}")

    yield

    logger.info("All tests finished.")
