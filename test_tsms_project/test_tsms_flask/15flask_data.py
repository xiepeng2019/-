import logging,request,json
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
from flask import Flask, render_template
app = Flask(__name__)
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
    # 黑名单
    if is_black(content, base_config.get("black_list")):
        return {"code": 2, "msg": "blackword"}, 403
    return {"code": 0, "msg": "success"}, 200