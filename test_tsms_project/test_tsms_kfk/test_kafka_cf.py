import json
import logging
import time
from kafka import KafkaConsumer, TopicPartition
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
consumer = KafkaConsumer(
    group_id='group6',
    bootstrap_servers=['111.229.87.152:9092'],
)
# 指定分区
tp = TopicPartition("msgTopic", 0)
# 初始化
consumer.assign([tp])
# 寻找分区的最早可⽤的偏移量
consumer.seek_to_beginning()
# 指定偏移量
consumer.seek(tp, 5)
# 开始消费
for msg in consumer:
    time.sleep(1)
    logging.info("[当前接收到到数据是]: {}".format(msg))
    logging.info(msg.value)

