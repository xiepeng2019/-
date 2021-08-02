# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
from flask import Flask, request
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')



app = Flask(__name__)
@app.route("/test/", methods=["GET", "POST"])
def get_args():
    logging.info("[请求headers]：{}".format(request.headers))
    logging.info("[请求⽅式]: {}".format(request.method))
    logging.info("[请求args]: {}".format(request.args))
    # 1. requests客户端直接提交的字符串数据，会识别成为bytes数据，如果需要字符串，需要⾃⾏解码
    # 2. requests客户端直接提交的字典数据，request.data会识别为 b""
    logging.info("[请求data]: {} {}".format(request.data, type(request.data)))
    logging.info("[data数据解码后结果]: {}".format(request.data.decode()))
    logging.info("[尝试获取data中的name参数]:{}".format(request.args.get("name")))
    # 获取form数据，如果form-data的key 与 args参数名重复，会优先取args参数
    logging.info("[请求form数据]: {} {}".format(request.form,type(request.form)))
    logging.info("[尝试获取form中的name参数]:{}".format(request.form.get("name")))
    # 获取json数据
    logging.info("[请求json数据]: {} {}".format(request.json,type(request.json)))
    # 没有return则会报错
    return request.data
if __name__ == '__main__':
    app.run(debug=True)