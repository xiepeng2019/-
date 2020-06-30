db_config = {
    "engine": "pymysql",
    "user": "root",
    "passwd": "123456",
    "host": "192.168.0.180",
    "port": 3306,
    "database": "flaskblog",
    "charset": "utf8"  # 注意：utf-8不可以
}

table_config = {
    "sign": "sms_sign",
    "temp": "sms_template",
    "send": "sms_send"
}
