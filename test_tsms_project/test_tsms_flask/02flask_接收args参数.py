# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
from flask import Flask, request


logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')

app = Flask(__name__)
@app.route("/test/",methods=["PSOT","GET"])
def get_args():
    logging.info("[请求⽅式]: {}".format(request.method))
    logging.info("[请求args]: {}".format(request.args))
    logging.info("[尝试获取args中的name参数]:{}".format(request.args.get("name")))
    # logging.info("[尝试获取args中的name参数]:{}".format(request.args.post("name")))
 # 没有return则会报错
    return request.args
if __name__ == '__main__':
    app.run(debug=True,host="192.168.31.237",port="5001")