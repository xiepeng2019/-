import json
from tsms_pytest_commons.tsms_rds  import TsmsRedis
from flask import Flask, request
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

app_3rd = Flask(__name__)
rds = TsmsRedis()
base_config = {
    "user": "root",
    "passwd": "dcs123",
    "black_list": ["fuck", "敏感", "色情"]
}


def is_black(content, black_list: list):
    for black in black_list:
        if black in content:
            return True
    return False


@app_3rd.route("/v1/3rd", methods=["POST"])
def mock_3rd():
    # 鉴权
    auth = request.authorization
    user = auth.get("username")
    passwd = auth.get("password")
    logging.info("[data]: {}".format(request.data))
    logging.info("[user:{} passwd:{}]".format(user, passwd))
    # logging.info("{} {}".format(request.json, type(request.json)))
    if user != base_config.get("user") or passwd != base_config.get("passwd"):
        return {"code": -1, "msg": "authfail"}, 400
    # 限长
    body = request.json
    logging.info("[body is]: {}".format(body))
    content = body.get("content")
    if len(content) > 20:
        return {"code": 1, "msg": "lengthlimit"}, 403
    # 黑词
    if is_black(content, base_config.get("black_list")):
        return {"code": 2, "msg": "blackword"}, 403
    return {"code": 0, "msg": "success"}, 200


@app_3rd.route("/v1/callback", methods=["POST"])
def get_callback():
    body = request.json
    logging.info("[回调信息]: {}".format(body))
    logging.info("[]: {}".format(request.headers))
    logging.info("[]: {}".format(request.method))
    rds.set_callback(uuid=body.get("uid"), value=json.dumps(body))
    return "ok"


if __name__ == '__main__':
    app_3rd.run(debug=True, host="192.168.31.237",port="5011")