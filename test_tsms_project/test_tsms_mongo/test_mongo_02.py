# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/31

import json
import logging
import random
from tsms_pytest_commons.configs.tsms_mongo_config import TsmsMongo
from tenacity import retry, stop_after_attempt, wait_random_exponential
from tsms_pytest_commons.tsms_base import TsmsBase
tb =TsmsBase()
md = TsmsMongo()
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


class TestTsmsKfkAnalysis(object):
    def test_find_mongo_01(self,tb):
        """立即查询mongo"""
        data = tb.send_data(sign_id=16, temp_id=6)
        tb.req_post("message", data)
        # 直接查询
        # time.sleep(2)
        # res = md.mongo_tsms(uid=tb.json.get("uuid"))
        # assert res.get("uid") == tb.json.get("uuid")
        # 错误重试
        self.find_mongo(tb.json.get("uuid"))

    @retry(stop=stop_after_attempt(5), wait=wait_random_exponential(2, max=5))
    def find_mongo(self, uid):
        md = TsmsMongo()
        # md.mongo_tsms(uid="27d7769a-557c-11ea-bbf2-5254000db3ea")
        res = md.mongo_tsms(uid=uid)
        assert res.get("uid") == uid

    def test_find_mongo_02(self, tb):
        """错误重试"""
        data = tb.send_data()
        tb.req_post("message", data)
        self.find_mongo(uid=tb.json.get("uid"))

    def test_kfk_01(self, kfk,md):
        uid = str(random.randint(10000000, 999999999))
        data = {
            "uid": uid,
            "phone": "13988886666",
            "content": "【签名测试】这是内容"
        }
        # 直接写数据到kafka
        kfk.send_data_secure(json.dumps(data))
        md.mongo_tsms(uid=uid)
        assert md.res.get("uid") == uid
        assert md.res.get("phone") == "13988886666"
        assert md.res.get("sign") == "签名测试"
        assert md.res.get("phone_type") == "移动"


if __name__ == '__main__':
    tk = TestTsmsKfkAnalysis()