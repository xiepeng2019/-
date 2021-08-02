# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02


"""
一、
    1、topic------消息种子分类，每一类消息称为topic
    2、producer---topic生产者
    3、cosumer----topic消费者，可以订阅一个或对个主题
    4、broker-----消息代理
二、技术实现
    1、partitions实现高并发
    2、partitions复制 + zookeeper 实现高可用
三、原理
    1、偏移量（offset）：重复消费
"""

import logging,time
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
from kafka import KafkaProducer

# producer = KafkaProducer(
#     bootstrap_servers=['111.229.87.152:9092'],
#     key_serializer=str.encode,
#     value_serializer=str.encode
# )
# future = producer.send('topic_xiepeng', key=b'', value='你好', partition=0)
# result = future.get(timeout=100000)
# logging.info(result)




# 声明编码格式，默认是utf-8
producer = KafkaProducer(
    bootstrap_servers=['111.229.87.152:9092'],
    key_serializer=str.encode,
    value_serializer=str.encode
)
future = producer.send('topic_xiepeng', key='key', value='我爱你', partition=0)
result = future.get(timeout=10)
logging.info(result)







