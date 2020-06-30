import logging,time,json
from tsms_pytest_commons.tsms_rds import TsmsRedis
from tsms_pytest_commons.configs import tsms_mq

from tenacity import retry, stop_after_attempt, wait_random_exponential
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
rds = TsmsRedis()

# def test_003():
#     pass

class TestTsmsMqConsume(object):
    @retry(stop=stop_after_attempt(5), wait=wait_random_exponential(2, max=5))
    def rds_retry(self, uuid, exp):
        res = rds.get_mq(uuid)
        assert json.loads(res) == exp

    def test_consume_01(self, tb, rds):
        """验证mq消费到的的数据是否符合预期"""
        # 调接⼝
        data = tb.send_data()
        tb.req_post("message", data)
        # 检查redis数据(消费到的真实数据)
        exp = {
            "uid": tb.json.get("uuid"),
            "phone": data.get("mobiles")[0],
            "content": "【hellokitty】验证码为：123"
        }
        self.rds_retry(tb.json.get("uuid"), exp)




