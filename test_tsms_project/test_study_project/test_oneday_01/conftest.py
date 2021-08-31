# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02

import pytest
import logging

"""
pytest自定义命令行
"""
def pytest_addoption(parser):
    parser.addoption('--host_addr',action='store',default=None,help='传入host地址')
    parser.addoption('--startall',action='store',default=None,help="标示执行全部用例")
# # 2. 可通过⽅法返回，然后通过fixture透传，注意：这⾥使⽤pytestconfig获取参数
@pytest.fixture()
def host_address(pytestconfig):
    # 这⾥的host_add⾃定义命名，将整个结果返回
    logging.info("[pytestconfig为]:{}".format(pytestconfig))
    return pytestconfig.getoption('--host_addr')
@pytest.fixture()
def host_address1(request):
    # 这⾥的host_add⾃定义命名，将整个结果返回
    return request.config.getoption('--host_addr')