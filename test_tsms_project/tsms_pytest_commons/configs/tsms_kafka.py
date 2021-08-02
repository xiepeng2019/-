# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging
import random
import json
import time
from pymongo import MongoClient
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


# client = MongoClient("mongodb://148.70.194.135:27017/")
# db=client.tsms_box
# col=db.tsms_box

kfk_config = {
    "host": "111.229.87.152",
    "port": 9092,
}


class KafkaSender:
    def __init__(self, kafkaTopic="topic_dcs"):
        self.kafkaHost = kfk_config.get("host")
        self.kafkaPort = kfk_config.get("port")
        self.kafkaTopic = kafkaTopic
        self.producer = None

    def connect(self):
        self.producer = KafkaProducer(
            bootstrap_servers='{kafka_host}:{kafka_port}'.format(
                kafka_host=self.kafkaHost,
                kafka_port=self.kafkaPort
            )
        )

    def close(self):
        self.producer.close()

    def send_data(self, params):
        logging.info("[现在准备发送数据]: {}".format(params))
        try:
            producer = self.producer
            producer.send(self.kafkaTopic, key=None, value=params.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            return {"result": "error", "message": str(e)}
        else:
            return {"result": "success", "message": "发送成功"}

    def send_data_secure(self, params):
        self.connect()
        self.send_data(params)
        self.close()




if __name__ == '__main__':
    message = '{"uid": "241214764", "phone": "17360188737", "content": "【当前数据】hello"}'
    sender = KafkaSender()
    sender.send_data(message)
    # sender.send_data_secure(message)
    # cx = col.find()
    # for i in cx:
    #     print(i)
