# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
from flask import Flask, render_template
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')


app = Flask(__name__)
@app.route('/students/')
def result():
    dict = {
    'ld': 90,
    'scl': 90,
    'ljh': 90,
    'qxl': 90,
    'xp': 90,
    'hhc': 90,
    'wjq': 90,
}
    return render_template('students.html', result=dict)



if __name__ == '__main__':
    app.run(debug=True,host="192.168.31.237",port="5002")