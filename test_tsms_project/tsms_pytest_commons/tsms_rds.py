import redis
import logging
from tsms_pytest_commons.configs.tsms_rds_config import *
from tsms_pytest_commons.configs.tsms_base_config import *

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s:')


class TsmsRedis(object):
    def __init__(self):
        self.user = account_config.get("default_user")
        self.pool = redis.ConnectionPool(
            host=rds_config.get("host"),
            port=rds_config.get("port"),
            password=rds_config.get("password"),
            db=rds_config.get("db"),
            decode_responses=True  # 默认解码
        )
        # redis连接池
        self.rds = redis.Redis(connection_pool=self.pool)

    def get_account(self, user=None):
        """获取充值金额"""
        user = user if user else self.user
        key = "tsms:%s:account" % user
        res = self.rds.get(key)
        logging.info("{} = {}".format(key, res))
        return int(res)

    def get_freq(self, phone):
        """获取超频详情"""
        key = "freq:%s" % phone
        res = self.rds.get(key)
        ttl = self.rds.ttl(key)
        logging.info("{} = {} ttl = {}".format(key, res, ttl))
        return int(res), int(ttl)

    def set_freq(self, phone, value):
        """设置频率计数"""
        key = "freq:%s" % phone
        self.rds.setex(key, 600, value)
        res = self.get_freq(phone)
        logging.info("[now freq is]: {}".format(res))
        return res

    def set_mq(self, uuid, value):
        key = "mq:xiepeng:%s" % uuid
        res = self.rds.setex(key, 3000, value)
        return res

    def get_mq(self, key):
        """通过key获取redis中value"""
        res = self.rds.get("mq:" +key)
        logging.info('获取{}的值为：{}'.format(key, res))
        return res

    def clear_freq(self, phone):
        key = "freq:%s" % phone
        res = self.rds.delete(key)
        logging.info("[now delete is]: {}".format(res))
        return res

    def set_callback(self, uuid, value):
        logging.info("[set {}]: {}".format(uuid, value))
        key = "callback:xiepeng:%s" % uuid
        res = self.rds.setex(key, 3600, value)
        return res


if __name__ == '__main__':
    rds = TsmsRedis()
    rds.get_account("root")
    # rds.get_freq("18")
