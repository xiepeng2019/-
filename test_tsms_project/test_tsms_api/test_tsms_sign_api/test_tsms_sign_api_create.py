from tsms_pytest_commons.tsms_base import TsmsBase
from tsms_pytest_commons.tsms_db import TsmsDB
import logging, pytest


logger = logging.getLogger(__name__)

ts = TsmsBase()
tb = TsmsDB()


@pytest.fixture(scope="function")
def sign_para_fail(request):
    """
    单个测试夹具：测试所有异常data
    """
    data = ts.sign_data()
    code = request.param.get("http_code")
    exp = request.param.get("expect")
    for k, v in request.param.items():
        if k in data:
            data[k] = v
    ts.req_post("sign", data=data)
    assert ts.status_code == code
    assert ts.json == exp


# 测试参数错误场景
test_sign_param_fail = [
    # 1. 签名内容为None
    {"signature": None, "http_code": 400, "expect": {'error': 'ER:0004', 'message': 'prams fail'}},
    # 2. 签名内容为空
    {"signature": "", "http_code": 400, "expect": {'error': 'ER:0004', 'message': 'prams fail'}},
    # 3. source为空
    {"source": None, "http_code": 400, "expect": {'error': 'ER:0004', 'message': 'prams fail'}},
    # 4. source为空
    {"source": "", "http_code": 400, "expect": {'error': 'ER:0004', 'message': 'prams fail'}},
]


class TestTsmsSignApiCreate(object):
    @pytest.mark.level1
    @pytest.mark.critical
    def test_sign_api_create_01(self, clear_sign):
        """
        创建签名成功
        """
        data = ts.sign_data()
        ts.req_post("sign", data)
        assert ts.status_code == 200
        assert isinstance(ts.json["sign_id"], int)
        # 指定数据清理
        clear_sign(ts.json["sign_id"])

    @pytest.mark.critical
    def test_sign_api_create_02(self):
        """
        账户不存在
        """
        data = ts.sign_data()
        ts.req_post("sign", data, user="dcs1", passwd=123)
        assert ts.status_code == 400
        assert ts.json == {'error': 'ER:0001', 'message': 'auth not pass'}

    @pytest.mark.critical
    def test_sign_api_create_03(self):
        """
        账户不存在
        """
        data = ts.sign_data()
        ts.req_post("sign", data, user="dcs1", passwd="123")
        assert ts.status_code == 400
        assert ts.json == {'error': 'ER:0001', 'message': 'auth not pass'}

    @pytest.mark.normal
    def test_sign_api_create_04(self):
        """
        密码错误
        """
        data = ts.sign_data()
        ts.req_post("sign", data, user="dcs", passwd="1234")
        assert ts.status_code == 400
        assert ts.json == {'error': 'ER:0001', 'message': 'auth not pass'}

    @pytest.mark.normal
    @pytest.mark.parametrize("sign_para_fail", test_sign_param_fail, indirect=True)
    def test_sign_api_create_05(self, sign_para_fail):
        """
        测试所有异常场景，只校验接口返回
        """
        logger.info("[测试异常场景]")

    # @pytest.mark.critical
    # def test_sign_api_create_06(self, clear_sign):
    #     """
    #     创建签名成功，校验db结果
    #     """
    #     data = ts.sign_data()
    #     ts.req_post("sign", data)
    #     assert ts.status_code == 200
    #     assert isinstance(ts.json["sign_id"], int)
    #     # db校验
    #     res = tb.tsms_select(
    #         "sign",
    #         "signature,source,pics,audit_status,reject_reason",
    #         sign_id=ts.json["sign_id"]
    #     )
    #     assert res["signature"] == data["signature"]
    #     assert res["source"] == data["source"]
    #     assert res["pics"] == data["pics"][0]
    #     assert res["audit_status"] == "reviewing"
    #     assert not res["reject_reason"]
    #     # 指定数据清理
    #     clear_sign(ts.json["sign_id"])


def test_sign_api_create_07(tb):
    """演示环境切换"""
    data = tb.sign_data()
    tb.req_post("sign", data)
    assert isinstance(tb.json.get("sign_id"), int)

