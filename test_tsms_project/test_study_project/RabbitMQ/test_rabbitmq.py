# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import pika


"""RBMQ实现生产"""
credentials = pika.PlainCredentials("admin","admin")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="192.168.0.180",
        port=5672,
        virtual_host="admin",
        credentials=credentials
    )
)
# channel = connection.channel()
# channel.basic_publish(
#     exchange='',
#     routing_key='谢鹏',
#     body='打扰了，大哥大姐们'
# )
# print("发送消息")


"""RBMQ实现消费"""
#建立连接
channel = connection.channel()
#持久化声明
channel.queue_declare(queue='谢鹏', durable=True)
def callback(ch,method,properties,body):
    print(body)

# 这⾥ack是false，没有回执，所以会⼀直消费
channel.basic_consume(on_message_callback=callback,queue="谢鹏",auto_ack=True)

print('等待消息 亲：可以强制退出的哦')
channel.start_consuming()






credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(
 pika.ConnectionParameters(
 host="192.168.0.180",
 port=5672,
 virtual_host="admin",
 credentials=credentials
 )
)
# 建⽴连接
channel = connection.channel()
channel.queue_declare(queue='谢鹏', durable=True)
# 为队列定义⼀个回调（callback）函数
# 当我们获取到消息的时候，Pika库就会调⽤此回调函数
# 这个回调函数会将接收到的消息内容输出到屏幕上
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# 告诉RabbitMQ这个回调函数将会从名为"queue_dcs"的队列中接收消息
# 这⾥ack是false，没有回执，所以会⼀直消费
# channel.basic_consume(on_message_callback=callback, queue='谢鹏',auto_ack=False)
# 如果ack是true，则会给⼀个回执，则认定消费成功
channel.basic_consume(on_message_callback=callback, queue='谢鹏',auto_ack=True)
# 扇形交换机
# 扇形交换机将消息路由给它绑定的所有队列，⽽不管绑定的路由健。若某个扇形交换机绑定了N个队
# 列，当有消息发到交换机，它会把消息拷⻉分别发送给这N个队列。即：⼴播路由
# 使⽤案例：
# 1. ⼤规模多⽤户在线游戏，处理排⾏榜更新等全局事件
# 2. 体育新闻⽹站将⽐分更新分发给移动客户端
# 3. 分发系统⼴播各种状态和配置更新
# 4. 群聊，分发消息给参与群聊的⽤户
# 先创建好 fanout交换机，然后绑定多个队列，然后通过python往交换机⾥写数据
# 同时消费两个队列
print('等待消息 CTRL+C强制退出')
# 运⾏⼀个⽤来等待消息数据并且在需要的时候运⾏回调函数的⽆限循环
channel.start_consuming()