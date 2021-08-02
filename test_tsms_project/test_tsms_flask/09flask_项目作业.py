# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
import redis
from flask import Flask
from flask import make_response
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')


r = redis.Redis(host="148.70.194.135",port="8085")
r.set('dcs','40')
app = Flask(__name__)
@app.route("/account/<user>", methods=["GET"])
def get_money(user):
    '''redis查询'''
    r = redis.Redis(host="148.70.194.135",port="8085",db=1)
    return make_response(f'{r.get(user).decode()}',40)

if __name__ == '__main__':
    app.run(debug=True)

