# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import pika
import sys
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="192.168.0.180",
        port=5672,
        virtual_host="admin",
        credentials=credentials
    )
)
channel = connection.channel()
message = ' '.join(sys.argv[1:0]) or "我是发布订阅模式"
#申明交换机
channel.exchange_declare(exchange='谢鹏', exchange_type='fanout',durable=True)
channel.basic_publish(exchange='谢鹏',routing_key='',body=message)
print("发送信息 %s % message")
connection.close()


# result = channel.queue_declare(queue='',exclusive=True)
# queue_name = result.method.queue
# channel.queue_bind(exchange='xiepeng007',queue=queue_name)
#
# def callback(ch,method,properties,body):
#     print("获取消息队列信息中...: %r" % (body,))
# channel.basic_consume(on_message_callback=callback,queue=queue_name,auto_ack=True)
# channel.start_consuming()






















