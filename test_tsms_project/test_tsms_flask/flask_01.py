# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
from flask import Flask
from flask import redirect
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')


app = Flask(__name__)

# @app.route('/getint/<int:sign_id>')
# def flask_api(sign_id):
#     print(sign_id,type(sign_id))
#     return '数据类型id是 %d'%sign_id
#
# @app.route('/getfloat/<float:ft>')
# def getfloat(ft):
#     print(ft,type(ft))
#     return 'ft is %f' %ft

# @app.route('/xp/')
# def xiepeng():
#     return "这是谢鹏的名字"

@app.route('/xp')
def hello_xp():
    return '你好  xp'


@app.route('/ql')
def hello_ql():
    return 'hello ql'


@app.route('/user/<name>')
def hello_user(name):
    logging.info("[name is]:{}".format(name))
    if name =='xp':
        return redirect("http://127.0.0.1:5000/xp")
    if name =='ql':
        return redirect("http://127.0.0.1:5000/ql")
    else:
        return redirect("http://www.baidu.com")


if __name__ == '__main__':
    app.run(debug=True,host="192.168.31.237",port="5001")