from tsms_pytest_commons.configs.tsms_base_config import *
import logging, pytest

logger = logging.getLogger()


class TestTsmsChargeApi(object):
    @pytest.mark.critical
    def test_charge_01(self, tb, rds):
        """
        充值一条记录，检查redis
        """
        # 获取历史金额
        money_history = rds.get_account()
        # 发接口请求
        data = tb.charge_data()
        tb.req_post("charge", data, user=account_config.get("root_user"), passwd=account_config.get("root_passwd"))
        assert tb.status_code == 200
        assert tb.text == "ok"
        # 获取现在金额
        money_now = rds.get_account()
        # 计算金额
        assert money_now - money_history == data.get("charge")

    @pytest.mark.normal
    def test_charge_02(self, tb):
        """
        非root用户
        """
        # 发接口请求
        data = tb.charge_data()
        tb.req_post("charge", data, user="dcs", passwd="123")
        assert tb.status_code == 400
        assert tb.json == {'error': 'ER:0003', 'message': 'please use root user request'}

    @pytest.mark.normal
    def test_charge_03(self, tb):
        """
        root密码错误
        """
        # 发接口请求
        data = tb.charge_data()
        tb.req_post("charge", data, user="root", passwd="1234")
        assert tb.status_code == 400
        assert tb.json == {'error': 'ER:0001', 'message': 'auth not pass'}

    @pytest.mark.normal
    def test_charge_04(self, tb):
        """
        金额为字母
        """
        # 发接口请求
        data = tb.charge_data(charge="aaa")
        tb.req_post("charge", data, user=account_config.get("root_user"), passwd=account_config.get("root_passwd"))
        assert tb.status_code == 400
        assert tb.json == {'error': 'ER:0004', 'message': 'prams fail'}

    @pytest.mark.normal
    @pytest.mark.skip(reason="后端有bug，该用例先跳过")
    def test_charge_05(self, tb):
        """
        充值用户不存在，此处有bug，用户不存在也可以充值
        """
        # 发接口请求
        data = tb.charge_data(user="dcs1")
        tb.req_post("charge", data)
        assert tb.status_code == 403
