import logging, pytest

logger = logging.getLogger()


class TestTsmsSignApiUpdate(object):
    @pytest.mark.critical
    def test_sign_update_01(self, rejected_sign, tb, td, clear_sign):
        """
        更新签名成功
        """
        sign_id = rejected_sign
        data = tb.sign_data()
        data["sign_id"] = sign_id
        tb.req_put("sign", data)
        assert tb.status_code == 200
        assert tb.json == {'sign_id': sign_id}
        # 校验数据库
        res = td.tsms_select("sign", "audit_status", sign_id=sign_id)
        assert res.get("audit_status") == "reviewing"
        # 清除
        clear_sign(sign_id)

    @pytest.mark.normal
    def test_sign_update_02(self, tb, td):
        """
        更新签名id不存在
        """
        data = tb.sign_data()
        data["sign_id"] = 123
        tb.req_put("sign", data)
        assert tb.status_code == 403
        assert tb.json == {'error': 'ER:0011', 'message': 'edit sign fail'}
