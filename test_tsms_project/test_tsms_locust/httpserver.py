from gevent import monkey

monkey.patch_all()
# from utils.database import DataBase
import datetime
import json
from gevent import pywsgi
from flask import Flask, request
from Config.db import test

app = Flask(__name__)


# database = DataBase(test.get("mongo_uri"))
# db = database.connect_db(test.get("db"))
#
#
# def insert_data_into_db(data):
#     data.update(createAt=datetime.datetime.utcnow())
#     try:
#         db.sx_callback_data.insert_one(data)
#     except Exception as e:
#         database.close_db()
#         raise Exception(f"fail to insert callback msg into db:{e}")
#     finally:
#         database.close_db()


# @app.route('/callback', methods=['POST'])
# def test_callback():
#     data = json.loads(request.get_data(as_text=True))
#     # insert_data_into_db(data)
#     print(data)
#     return "callback successfully"


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
