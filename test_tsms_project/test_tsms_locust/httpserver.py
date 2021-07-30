from gevent import monkey

monkey.patch_all()
# from utils.database import DataBase
import datetime
import json
from gevent import pywsgi
from flask import Flask, request

app = Flask(__name__)



@app.route('/kronos', methods=['POST'])
def kronos():
    data = request.get_data(as_text=True)
    print(data)
    return "kronos callback successfully"


@app.route('/viva', methods=['POST'])
def viva():
    data = request.get_data(as_text=True)
    print(data)
    return "viva callback successfully"


if __name__ == '__main__':
    app.debug = True
    server = pywsgi.WSGIServer(('0.0.0.0', 5050), app)
    server.serve_forever()
