# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/user/<name>')
def index(name):
    return render_template('hello.html', name=name)



if __name__ == '__main__':
    app.run(debug=True,host="192.168.31.237",port="5002")






