url_web = "192.168.0.180:5001"
account_config = {
    "default_user": "dcs",
    "default_passwd": 123,
}
url_config = {
    "login": url_web + "/login",
    "sign": url_web + "/user/{}/sign".format(account_config.get("default_user"))
}
