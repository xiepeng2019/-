# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import pika




def callback(ch,method,properties,body):
    """RBMQ实现生产"""
    print("获取到消息 %s" % body)

credentials = pika.PlainCredentials("admin","admin")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="192.168.0.180",
        port=5672,
        virtual_host="admin",
        credentials=credentials
    )
)

channel = connection.channel()
# channel.exchange_declare(exchange='ex-xiepeng',exchange_type='fanout',durable=True)
# a = random.randint(1,666)
# msg = '这是谢鹏的个人队列信息，请大家不要随意获取，谢谢各位老板!{}'.format(str(a))
# channel.basic_publish(
#     exchange='ex-xiepeng',
#     routing_key='',
#     body=msg,
# )
# print('发送成功')
# connection.close()


# """同时消费两个队列"""
# channel.queue_declare(queue='xiepeng',durable=True)
# channel.basic_consume(on_message_callback=callback,queue='ex-xiepeng',auto_ack='True')
#
# #建立连接2
# channel2 = connection.channel()
# channel2.queue_declare(queue='queue_dcs_fanout2', durable=True)
# channel2.basic_consume(on_message_callback=callback,queue='ex-xiepeng_01', auto_ack=True)
# print("等待消息推送中...")
# channel.start_consuming()
# channel2.start_consuming()






# """第一条"""
# channel.exchange_declare(exchange="ex-xiepeng004",exchange_type="topic",durable=True)
# a = random.randint(1,218)
# msg1 = '我是topic，请消费我，谢谢！！！{}'.format(str(a))
# channel.basic_publish(
#     exchange="ex-xiepeng004",
#     routing_key="ex-xiepeng004",
#     body=msg1
# )
# """第二条"""
# a = random.randint(1,88)
# msg2 = "我是消息队列2，请消费我，谢谢！{}".format(str(a))
# channel.basic_publish(
#     exchange="ex-xiepeng004",
#     routing_key="ex-xiepeng004",
#     body=msg2
# )
# print("发送的两个消息 %s % msg")
# connection.close()





# """绑定routing_keys，进行统一消费，支持routing.name.*方式消费"""
# def callback(ch,method,properties,body):
#     print("获取到消费信息 %s % body")

# credentials = pika.PlainCredentials("admin","admin")
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(
#         host="192.168.0.101",
#         port="5672",
#         virtual_host="admin",
#         credentials=credentials
#     )
# )
#建立连接1
# channel = connection.channel()
#绑定交换机
channel.exchange_declare(
    exchange="ex-xiepeng004",
    exchange_type="topic",
    durable=True
)
#获取队列名
result = channel.queue_declare('',exclusive=True)
queue_name = result.method.queue
print(queue_name)
#循环绑定routing_keys
bingding_keys = ["routing.ex-xiepeng_01,ex-xiepeng_02"]
binding_keys = ["routing.ex-xiepeng.*"]
for binding_keys in bingding_keys:
    channel.queue_bind(
        exchange='ex-xiepeng004',
        queue=queue_name,
        routing_key=bingding_keys
    )
channel.basic_consume(on_message_callback=callback,queue=queue_name,auto_ack=True)
print("监听消息队列信息中...")
channel.start_consuming()

