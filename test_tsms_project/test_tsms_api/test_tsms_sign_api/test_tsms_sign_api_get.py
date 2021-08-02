# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
import pytest

logger = logging.getLogger()


class TestTsmsSignApiGet(object):
    @pytest.mark.critical
    def test_sign_get_01(self, create_sign, tb, clear_sign):
        """
        查询签名
        """
        sign_id = create_sign
        assert tb.signid_exist(sign_id)
        clear_sign(sign_id)
        assert tb.status_code == 200
