# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import json
import logging
from kafka import KafkaConsumer


logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')

consumer = KafkaConsumer(
    'topic_xiepeng',
    group_id='group6',
    bootstrap_servers=['111.229.87.152:9092'],
    key_deserializer=bytes.decode,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
for msg in consumer:
    logging.info("[当前接收到到数据是]: {}".format(msg))






