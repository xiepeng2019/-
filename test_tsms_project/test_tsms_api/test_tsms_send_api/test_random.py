import logging, pytest,requests
import random

logger = logging.getLogger(__name__)


def test_fix(login, login2, create_sign):
    logging.info("用例本体")


class Test111():
    def test_1(self, tb):
        # logger.info("okk")
        # logger.info(random_1(self.test_1))
        logger.info(tb.send_data(1))

    def test_2(self, tb):
        # logger.info("ok")
        # logger.info(random_1(self.test_1))
        logger.info(tb.send_data(2))


if __name__ == '__main__':
    pytest.main()
