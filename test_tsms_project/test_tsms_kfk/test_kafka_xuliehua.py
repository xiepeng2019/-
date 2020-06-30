import json
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
from kafka import KafkaProducer
# 声明编码格式，默认是utf-8
# 注意，value_serializer接收的是⼀个匿名函数，接收⼀个字典对象，返回⼀个bytes对象
producer = KafkaProducer(
    bootstrap_servers=['111.229.87.152:9092'],
    key_serializer=str.encode,
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

future = producer.send('topic_xiepeng', key='key', value={"name":"开⼼麻花","age":18}, partition=0)
result = future.get(timeout=10)
logging.info(result)