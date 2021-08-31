# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/31

import sys
import pytest
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
limit_ver = pytest.mark.skipif(sys.version_info < (3, 8), reason="python版本过低跳过")
# 当python版本低于3.8则不执⾏该⽤例，我的版本为3.7 所以跳过该⽤例
# 当python版本低于3.8则不执⾏该⽤例，我的版本为3.7 所以跳过该⽤例
@limit_ver
def test_function():
 logging.info(sys.version_info)
 logging.info("hello")
 assert 1 == 1










