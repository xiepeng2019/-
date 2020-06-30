import json
import logging
import time

from kafka import KafkaConsumer
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
consumer = KafkaConsumer(
    "topic_xiepeng",
    group_id='group6',
    bootstrap_servers=['111.229.87.152:9092'],
)
while True:
    msg = consumer.poll(timeout_ms=5) # 从kafka获取消息
    logging.info("当前拉取的数据: {}".format(msg))
    # time.sleep(10)
    for tp,messages in msg.items():
        for message in messages:
            logging.info("{}:{}:{}: key={}value={}".format(tp.topic,tp.partition,message.offset,message.key,message.value))
    time.sleep(5)
