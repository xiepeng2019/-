import logging, pytest

logger = logging.getLogger()


class TestTsmsSignApiDelete(object):
    @pytest.mark.critical
    def test_sign_delete_01(self, create_sign, tb):
        """
        删除成功
        """
        sign_id = create_sign
        tb.req_delete("sign", {'sign_id': sign_id})
        assert tb.status_code == 200
        assert tb.text == "ok"

    @pytest.mark.normal
    def test_sign_delete_02(self, tb):
        """
        删除不存在的签名
        """
        tb.req_delete("sign", {'sign_id': 123})
        assert tb.status_code == 403
        assert tb.json == {'error': 'ER:0012', 'message': 'delete sign fail'}
