# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
import pytest

logger = logging.getLogger()


@pytest.fixture()
def login2():
    logging.info("当前目录下的前置")
