import logging, pytest

logger = logging.getLogger()


@pytest.fixture()
def login2():
    logging.info("当前目录下的前置")
