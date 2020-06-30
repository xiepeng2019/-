from tsms_pytest_commons.tsms_base import TsmsBase
from tsms_pytest_commons.tsms_db import TsmsDB

import logging, pytest

logger = logging.getLogger(__name__)
# 声明测试夹具
tb = TsmsBase()
temp_para_fail = tb.gen_para_fail("temp")

# 统一管理异常场景
test_temp_param_fail = [
    # 1. sign_id为None
    {"sign_id": None, "http_code": 403, "expect": {'error': 'ER:0021', 'message': 'template prams fail'}},
    # 2. sign_id为空字符
    {"sign_id": "", "http_code": 403, "expect": {'error': 'ER:0021', 'message': 'template prams fail'}},
    # 3. type为0
    {"type": 0, "http_code": 403, "expect": {'error': 'ER:0021', 'message': 'template prams fail'}},
    # 4. type为4
    {"type": 4, "http_code": 403, "expect": {'error': 'ER:0021', 'message': 'template prams fail'}},
    # 5. ...
]


class TestTsmsTempApiCreate(object):
    @pytest.mark.critical
    def test_temp_create_01(self, tb, td):
        """
        创建一个模版，检查db内容
        """
        data = tb.temp_data()
        tb.req_post("temp", data)
        assert tb.status_code == 200
        assert isinstance(tb.json.get("temp_id"), int)
        # 查询数据库
        res = td.tsms_select(
            "temp",
            "temp_name,template,description,audit_status,temp_sign_id,temp_type",
            temp_id=tb.json.get("temp_id")
        )
        assert res.get("temp_name") == data.get("name")
        assert res.get("template") == data.get("template")
        assert res.get("description") == data.get("description")
        assert res.get("audit_status") == "reviewing"
        assert res.get("temp_sign_id") == data.get("sign_id")
        assert res.get("temp_type") == data.get("type")

    @pytest.mark.normal
    @pytest.mark.parametrize("temp_para_fail", test_temp_param_fail, indirect=True)
    def test_temp_create_02(self, temp_para_fail):
        """
        测试所有异常
        """
        logger.info("[测试所有异常]")
