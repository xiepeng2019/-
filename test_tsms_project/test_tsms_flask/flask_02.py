
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        logging.info("[请求表单是]: {}".format(request.form))
# 处理post请求
        user = request.form['name']
        logging.error("[从表单取出name值]: {}".format(user))
# 重定向到success()
# 1. 重定向的地址 2. 参数
        return redirect(url_for('success', name=user))
    else:
# 处理其他(get)请求
        logging.info("[get请求参数]: {}".format(request.args))
# 必须传⼊name参数
        user = request.args.get('name')
        return redirect(url_for('success', name=user))
if __name__ == '__main__':
    app.run(debug=True,host="192.168.31.237",port="5001")