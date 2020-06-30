import json
import logging, pika

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

mq_config = {
    "user": "admin",
    "passwd": "admin",
    "host": "192.168.0.180",
    "port": 5672,
    "vhost": "admin",
}

mq_push = {
    "direct": {
        "queue": "queue.celery.tsms.mq",
        "exchange": "xiepeng008",
        "routing_key": "xiepeng008"
    }
}


class MQPush(object):

    def __init__(self):
        self._host = mq_config.get("host")
        self._port = mq_config.get("port")
        self._vhost = mq_config.get("vhost")
        self._credentials = pika.PlainCredentials(mq_config.get("user"), mq_config.get("passwd"))
        self._connection = None

    def connect(self):
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self._host,
                port=self._port,
                virtual_host=self._vhost,
                credentials=self._credentials,
            )
        )

    def push_direct(self, body):
        if not self._connection:
            return
        queue = mq_push.get("direct").get("queue")
        exchange = mq_push.get("direct").get("exchange")
        routingkey = mq_push.get("direct").get("routing_key")
        logging.info("[push direct config is]: {} {}".format(exchange, routingkey))
        logging.info("[push body is]: {}".format(body))
        # 获取通道
        channel = self._connection.channel()
        # 绑定队列
        channel.queue_declare(queue=queue, durable=True)
        # 发送消息
        channel.basic_publish(
            exchange=exchange,  # 为空也允许
            routing_key=routingkey,
            body=body,
        )

    def close(self):
        if self._connection:
            self._connection.close()

    def push_direct_secure(self, body):
        self.connect()
        self.push_direct(body)
        self.close()

    def consume_direct(self):
        if not self._connection:
            return
        logging.info("[开始消费]")
        queue = mq_push.get("direct").get("queue")
        channel = self._connection.channel()
        channel.queue_declare(queue=queue)
        channel.basic_consume(on_message_callback=self.callback, queue=queue, auto_ack=False)
        channel.start_consuming()




    def push_fanout(self, body):
        if not self.connection:
            return
        queue = mq_push.get("fanout").get("queue")
        exchange = mq_push.get("fanout").get("exchange")
        routingkey = mq_push.get("routing_key")
        logging.info("[push fanout config is ]:{}{}".format(exchange, routingkey))
        logging.info("[push body is ]:{}".format(body))
        # 绑定队列
        channel = self._connection.channel()
        # 绑定队列
        channel.queue_declare(queue=queue, durable=True)
        # 发送消息
        channel.basic_publish(
            exchange=exchange,
            routing_key=routingkey,
            body=body
        )

    def close(self):
        if self._connection:
            self._connection.close()

    @staticmethod
    def callback(ch, method, properties, body):
        logging.info("[ch is]: {}".format(ch))
        logging.info("[methos is]: {}".format(method))
        logging.info("[properties is]: {}".format(properties))
        logging.info("[body is]: {}".format(body))


if __name__ == '__main__':
    mq = MQPush()
    data = {
        "uuid": "a1e2ff2e-23c5-11ea-a694-acde48001122",
        "phone": "17460178737",
        "content": "【hellokitty】验证码为：123"
    }
    mq.push_direct_secure(json.dumps(data))
    # mq.connect()
    # mq.push_direct("hello")
    # mq.close()