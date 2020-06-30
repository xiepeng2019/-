import logging, pymongo

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

mongo_config = {
    "host": "148.70.194.135",
    "port": 27017,
    "db_name": "tsms_analysis",
    "collection": "tsms_box"
}


class TsmsMongo(object):

    def __init__(self):
        self.mongo_str = "mongodb://{}:{}/".format(
            mongo_config.get("host"),
            mongo_config.get("port")
        )
        self.client = None
        self.db = None
        self.col = None
        self.res = {}

    def mongo_client(self):
        """使用配置文件连接"""
        if self.client:
            logging.info("[连接已存在，无须再次创建]")
            return self.client
        self.client = pymongo.MongoClient(self.mongo_str)
        logging.info(self.client)
        return self.client

    def mongo_db(self, db_name="default"):
        """使用默认库"""
        db_name = mongo_config.get("db_name") if db_name == "default" else db_name
        # db_name = "tsms_analysis"
        if not self.client:
            return
        # db1 = client.box2
        # 1. self.client.db_name ，创建的db是哪个db？
        # a. 创建一个名称为db_name 的 db  b. 创建一个 tsms_analysis 的db
        # 期望写入：self.client.tsms_analysis ：eval()
        # self.db = self.client.db_name
        mod_str = "self.client.{}".format(db_name)
        # mod_str -> self.client.tsms_analysis
        self.db = eval(mod_str)
        logging.info(self.db)
        return self.db

    def mongo_col(self, collection="default"):
        """使用默认集合"""
        collection = mongo_config.get("collection") if collection == "default" else collection
        if not self.db:
            logging.warning("[db尚未实例化]")
            return
        # self.db.{collection}
        self.col = eval("self.db.{}".format(collection))
        logging.info(self.col)
        return self.col

    def mongo_find(self, **kwargs):
        """条件查询"""
        if not kwargs:
            logging.warning("[请输入查询条件]: {}".format(kwargs))
        if not self.col:
            return
        self.res = self.col.find_one(kwargs)
        logging.info("[mongo查询结果是]: {}".format(self.res))
        return self.res

    # { "content_length" : 14, "uid" : "87fb16ea-4fea-11ea-bbf2-5254000db3ea", "phone" : "18695273186", "phone_type" : "联通", "sign" : "测试" }
    def mongo_tsms(self, uid, collection="default", db_name="default"):
        """tsms统计查询"""
        logging.info("[当前要查询的uid是]: {}".format(uid))
        self.mongo_client()
        self.mongo_db(db_name)
        self.mongo_col(collection)
        self.mongo_find(uid=uid)
        logging.info("[当前mongo查询结果是]: {}".format(self.res))
        return self.res

    def mongo_tsms_update(self, condition, update_value):
        """根据业务去定义"""
        pass

    def mongo_tsms_delete(self):
        """根据业务定义"""
        pass


if __name__ == '__main__':
    md = TsmsMongo()  # 实例化
    # 步骤查询
    # md.mongo_client()  # 创建client
    # md.mongo_db()  # 创建db
    # md.mongo_col()  # 创建col
    # md.mongo_find(uid="87fb16ea-4fea-11ea-bbf2-5254000db3ea")  # 执行查询
    # 简易查询
    md.mongo_tsms(uid="8873269e-557b-11ea-bbf2-5254000db3ea")