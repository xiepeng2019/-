from tsms_pytest_commons.configs.tsms_db_config import *
import records,logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s:')


class TsmsDB(object):
    def __init__(self):
        self.db_con_str = "mysql+{0}://{1}:{2}@{3}:{4}/{5}?charset={6}".format(db_config["engine"], db_config["user"], db_config["passwd"], db_config["host"], db_config["port"], db_config["database"], db_config["charset"])
        try:
            self.db = records.Database(self.db_con_str)
        except Exception as e:
            logging.error(e)
            raise

    def exe_sql(self, sql):
        """不设限制，请谨慎使用"""
        try:
            res = self.db.query(sql).all(as_dict=True)
            logging.info("[execute sql result is]: {}".format(res))
            if len(res) == 1:
                return res[0]
            return res
        except Exception as e:
            logging.error(e)

    def tsms_select(self, table_type, *fields, **kwargs):
        """select *fields from table where **kwargs"""
        table = table_config.get(table_type)
        options = 'where ' if kwargs else ''
        for k, v in kwargs.items():
            if isinstance(v, str):
                v = '\"' + v + '\"'
            options += k + "=" + str(v) + " and "
        if kwargs:
            options = options[:-4]
        query_fields = ','.join(fields)
        sql = '''select {0} from {1} {2};'''.format(query_fields, table, options)
        logging.info("[now execute sql is]: {}".format(sql))
        return self.exe_sql(sql)

    def tsms_update(self, table_type, field, value, **kwargs):
        """更新指定的字段，一次只允许修改一个"""
        table = table_config.get(table_type)
        # 限制字段
        if field not in ["audit_status", "is_delete"]:
            logging.info("[更新字段失败]: {}".format(field))
            return
        if kwargs:
            options = 'where '
            for k, v in kwargs.items():
                if isinstance(v, str):
                    v = '\"' + v + '\"'
                options += k + "=" + str(v) + " and "
            options = options[:-4]
        else:
            return
        if isinstance(value, int):
            sql = '''update {0} set {1}={2} {3};'''.format(table, field, value, options)
        else:
            sql = '''update {0} set {1}="{2}" {3};'''.format(table, field, value, options)
        logging.info("[now execute sql is]: {}".format(sql))
        try:
            self.db.query(sql)
        except:
            logging.ERROR("[数据库更新失败 sql 是]: {}".format(sql))

    def tsms_delete(self, table_type, **kwargs):
        """DELETE FROM `dcs_user` WHERE xxx=dcs"""
        table = table_config.get(table_type)
        options = 'where ' if kwargs else ''
        for k, v in kwargs.items():
            if isinstance(v, str):
                v = '\"' + v + '\"'
            options += k + "=" + str(v) + " and "
        if kwargs:
            options = options[:-4]
        sql = '''delete from {0} {1};'''.format(table, options)
        logging.info("[now execute sql is]: {}".format(sql))
        return self.db.query(sql)

    def tsms_record_del(self, table, **kwargs):
        self.tsms_update(table, "is_delete", 1, **kwargs)

    def tsms_insert(self):
        pass


if __name__ == '__main__':
    db = TsmsDB()
    a = db.tsms_select("sms_sign", "sign_id,signature", "source", "audit_status", sign_id=1289)
    b = db.tsms_update("sms_sign", "audit_status", "passed111", sign_id=1289)
    print(a)
    # TsmsDB.sign_sql()
    # c = db.tsms_delete("dcs_user", name="dcs")
    # print(c)
    # d = db.tsms_record_del("dcs_user", name="dcs")
