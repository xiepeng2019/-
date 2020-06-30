from tsms_pytest_commons.tsms_base import TsmsBase
from tsms_pytest_commons.tsms_db import TsmsDB
import logging, pytest

logger = logging.getLogger(__name__)


class TestTsmsSignApiReview():
    @pytest.mark.critical
    def test_sign_review_01(self, create_sign, tb, td, clear_sign):
        """
        审核通过
        """
        sign_id = create_sign
        tb.review("sign", sign_id, audit_status="passed")
        assert tb.status_code == 200
        assert tb.text == "ok"
        res = td.tsms_select("sign", "audit_status", sign_id=sign_id)
        assert res.get("audit_status") == "passed"
        # 清除
        clear_sign(sign_id)

    @pytest.mark.critical
    def test_sign_review_02(self, create_sign, tb, td, clear_sign):
        """
        审核为不通过
        """
        sign_id = create_sign
        # 审核为通过
        tb.review("sign", sign_id, audit_status="rejected")
        assert tb.status_code == 200
        assert tb.text == "ok"
        res = td.tsms_select("sign", "audit_status", sign_id=sign_id)
        assert res.get("audit_status") == "rejected"
        # 清除
        clear_sign(sign_id)

    @pytest.mark.normal
    def test_sign_review_03(self, create_sign, tb, td):
        """
        审核状态不合法
        """
        sign_id = create_sign
        # 审核为通过
        tb.review("sign", sign_id, audit_status="hh")
        assert tb.status_code == 403
        assert tb.json == {'error': 'ER:0013', 'message': 'sign audit_status fail'}
