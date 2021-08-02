# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
from flask import Flask
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')


app = Flask(__name__)

@app.route('/v1/3rd', methods=["POST"])
def get_args():
    # logging.info("[请求方式]：{}".format(request.data))
    # return request.data
    return {"code": 0, "msg": "success"}, 200


if __name__ == '__main__':
    app.run(debug=True,host="192.168.31.237",port="5011")






