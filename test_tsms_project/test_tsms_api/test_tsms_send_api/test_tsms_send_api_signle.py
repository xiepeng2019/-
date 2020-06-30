from tsms_pytest_commons.tsms_base import TsmsBase
from tsms_pytest_commons.tsms_db import TsmsDB
from tsms_pytest_commons.tsms_rds import TsmsRedis
from tsms_pytest_commons.configs.tsms_base_config import *
import logging, pytest
from tenacity import retry, stop_after_attempt, wait_random_exponential

logger = logging.getLogger(__name__)

# 声明夹具
td = TsmsDB()
tbs = TsmsBase()
send_para_fail = tbs.gen_para_fail("message")

# 异常场景
test_send_param_fail = [
    # 1. sign_id和temp_id不匹配
    {"sign_id": 1, "http_code": 403, "expect": {'error': 'ER:0023', 'message': 'sign id is not belong to user'}},
    # 2. temp_id审核未通过
    {"sign_id": data_config.get("default_sign_id"), "temp_id": data_config.get("not_pass_temp_id"), "http_code": 403, "expect": {'error': 'ER:0032', 'message': 'temp is not passed'}},
]


class TestTsmsSendApiSingle(object):
    @retry(stop=stop_after_attempt(5), wait=wait_random_exponential(2, max=5))
    def db_retry(self, data, uuid):
        """
        异步数据校验，重试查询数据库
        """
        res = td.tsms_select("send", "consume,status,mobile", uuid=uuid)
        assert res["consume"] == 1
        assert res["status"] == "success"
        assert res["mobile"] == data["mobiles"][0]
    @pytest.mark.critical
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_send_api_01(self, tb, rds):
        """
        发送一条消息，重试查询db
        """
        data = tb.send_data()
        rds.clear_freq(data.get("mobiles")[0])
        tb.req_post("message", data=data)
        assert tb.status_code == 200
        assert isinstance(tb.json["uuid"], str)
        self.db_retry(data, tb.json["uuid"])

    @pytest.mark.normal
    @pytest.mark.parametrize("send_para_fail", test_send_param_fail, indirect=True)
    def test_send_api_02(self, send_para_fail):
        """
        测试一般异常场景，只校验接口返回
        """
        logger.info("[测试异常场景]")

    @pytest.mark.normal
    def test_send_api_03(self, tb):
        """
        发送条数超过10条
        """
        data = tb.send_data(num=11)
        tb.req_post("message", data)
        assert tb.status_code == 200
        assert tb.json == {'error': 'ER:0033', 'message': 'invalidate mobile exist'}

    @pytest.mark.normal
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_send_api_04(self, tb, rds):
        """
        测试记频，有错误重试
        """
        data = tb.send_data()
        rds.clear_freq(data.get("mobiles")[0])
        logger.info("[当前data是]: {}".format(data))
        tb.req_post("message", data)
        assert tb.status_code == 200
        freq, ttl = rds.get_freq(data.get("mobiles")[0])
        assert freq == 1
        assert ttl == 600

    @pytest.mark.normal
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_send_api_05(self, tb, rds):
        """
        测试计费
        """
        # 获取历史金额
        money_history = rds.get_account()
        data = tb.send_data()
        rds.clear_freq(data.get("mobiles")[0])
        logger.info(data)
        logger.info("[当前data是]: {}".format(data))
        tb.req_post("message", data)
        # 获取现在金额
        money_now = rds.get_account()
        assert money_history - money_now == 1

    @pytest.mark.normal
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_send_api_06(self, tb, rds):
        """
        测试超频
        """
        # 发第一次，记频为1
        data = tb.send_data()
        rds.clear_freq(data.get("mobiles")[0])
        tb.req_post("message", data)
        assert tb.status_code == 200
        freq, ttl = rds.get_freq(data.get("mobiles")[0])
        assert freq == 1
        assert ttl == 600
        # 修改记频为19，发第二条
        rds.set_freq(data.get("mobiles")[0], value=19)
        tb.req_post("message", data)
        assert tb.status_code == 200
        # 发第三条，触发超频
        tb.req_post("message", data)
        assert tb.status_code == 403
        assert tb.json == {'error': 'ER:0036', 'message': 'send freq out of limit'}


    @pytest.mark.normal
    @pytest.mark.parametrize("send_para_fail", test_send_param_fail, indirect=True)
    def test_ceshizhuanbg(self):
        pass