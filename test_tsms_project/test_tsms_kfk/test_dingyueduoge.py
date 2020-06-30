import logging
from kafka import KafkaConsumer
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
consumer = KafkaConsumer(
    'msgTopic',
    group_id='group19',
    bootstrap_servers=['111.229.87.152:9092'],
)
# 订阅多个topic，⽤列表传参
consumer.subscribe(topics=['msgTopic', 'msgTopic1','topic_xiepeng','topic_lijihua','topic_shang'])
for msg in consumer:
    logging.info("[当前接收到到数据是]: {}".format(msg))