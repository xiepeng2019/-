# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
import json
from kafka import KafkaConsumer


logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')

# consumer = KafkaConsumer(
#     'topic_xiepeng',
#     group_id='6',
#     bootstrap_servers=['111.229.87.152:9092'],
#     key_deserializer=bytes.decode,
#     value_deserializer=bytes.decode
#     # consumer_timeout_msg=1000
# )
# for msg in consumer:
#     logging.info('[分区信息]：{}'.format(msg))
#     logging.info('[消息类容]：{}'.format(msg.value))
#     logging.info('[当前订阅的topic]: {}'.format(consumer.subscription()))
#     logging.info('[当前topic和分区信息]：{}'.format(consumer.assignment()))
#     logging.info('[可消费的偏移量]：{}'.format(consumer.beginning_offsets(consumer.assignment())))



#解码格式
consumer = KafkaConsumer(
    'topic_xiepeng',
    group_id='group6',
    bootstrap_servers=['111.229.87.152:9092'],
    key_deserializer=bytes.decode,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
for msg in consumer:
    logging.info("[当前接收到到数据是]: {}".format(msg))
