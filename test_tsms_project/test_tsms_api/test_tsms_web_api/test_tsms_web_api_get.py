from tsms_pytest_commons.configs.tsms_web_config import *
import logging, pytest

logger = logging.getLogger()


class TestTsmsWebApiGet(object):
    @pytest.mark.critical
    def test_web_get_01(self, web_session, tw):
        """
        获取session后在用例层面处理
        """
        url = url_config.get("sign")
        res = web_session.get(url)
        tw.reg_sign()
        assert "reviewing" in res.text

    @pytest.mark.critical
    def test_web_get_02(self, tw):
        """
        通过内部方法处理
        """
        tw.login_c()
        res = tw.reg_sign()
        logger.info(res)
