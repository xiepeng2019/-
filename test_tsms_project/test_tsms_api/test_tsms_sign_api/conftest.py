# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import pytest
import logging
from tsms_pytest_commons.tsms_base import TsmsBase


def pytest_addoption(parser):
 # 定义命令⾏参数
     parser.addoption('--env', action='store', default=None, help='传⼊host地址')


@pytest.fixture(scope="function")
def tb(pytestconfig):
    logging.info("[环境参数为]: {}".format(pytestconfig.getoption("--env")))
    if pytestconfig.getoption("--env") == "pro":
        return TsmsBase(env=0)
    else:
        return TsmsBase()

# @pytest.fixture(scope="function")
# def sign_para_fail(request):
#     """
#     单个测试夹具：测试所有异常data
#     """
#     data = ts.sign_data()
#     code = request.param.get("http_code")
#     exp = request.param.get("expect")
#     for k, v in request.param.items():
#         if k in data:
#             data[k] = v
#     ts.req_post("sign", data=data)
#     assert ts.status_code == code
#     assert ts.json == exp