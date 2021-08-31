# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02

import pika
import json
from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_random_exponential
from tsms_pytest_commons import tsms_db
from tsms_pytest_commons import tsms_rds


"""RBMQ实现消费"""
credentials = pika.PlainCredentials("admin","admin")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="192.168.0.180",
        port=5672,
        virtual_host="admin",
        credentials=credentials
    )
)
#建立连接
channel = connection.channel()
#持久化声明
channel.queue_declare(queue='ex-xiepeng', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# 如果ack是true，则会给⼀个回执，则认定消费成功
channel.basic_consume(on_message_callback=callback, queue='ex-xiepeng',auto_ack=True)
print('等待消息，Ctrl+c强制退出')
# 运⾏⼀个⽤来等待消息数据并且在需要的时候运⾏回调函数的⽆限循环
channel.start_consuming()


class TestTsmsMqproduce(object):
    uuid = "a1e2ff2e-23c5-11ea-a694-acde48001122"
    @retry(stop=stop_after_attempt(5), wait=wait_random_exponential(2, max=5))
    def db_retry(self,uuid):
        """
        异步数据校验，重试查询数据库
        """
    res = td.tsms_select("send","consume,status,mobile",uuid=uuid)
    assert res["status"] == "success"
    def test_pro_01(self,mq,td):
        data = {
            "uuid":self.uuid,
            "phone":"17360188737",
            "content": "【hellokitty】验证码为：123"
        }
# 改为failed
    td.tsms_update("send","status","failed",uuid=self.uuid)
    res = td.tsms_select("send", "status", uuid=self.uuid)
    assert res.get("status") == "failed"
    #写mq
    mq.push_direct_secure(json.dumps(data))
    #再查数据库
    self.db_retry(self.uuid)





