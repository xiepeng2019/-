# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import json
import logging
import time
from tsms_pytest_commons.configs.tsms_mq import MQPush
from multiprocessing import Process
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


def consumer(name):
    logging.info("consumer {}".format(name))
    mq = MQPush()
    mq.consume_direct(name)


if __name__ == '__main__':
    p1 = Process(target=consumer, args=("direct",))
    p1.start()
    time.sleep(5)
    mq = MQPush()
    data = {
        "uid": "a1e2ff2e-23c5-11ea-a694-acde48001122",
        "phone": "17134198056",
        "content": "【hellokitty】验证码为：123"
    }
    mq.push_direct_secure("direct", json.dumps(data))
    time.sleep(3)
    p1.terminate()
