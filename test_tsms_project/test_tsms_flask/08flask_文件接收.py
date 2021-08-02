# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import logging
import os
from flask import Flask, request
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
# 当前⽬录下需要创建这个⽂件夹
basedir = os.path.abspath(os.path.dirname(__name__))
path = basedir + "/upload/"


app = Flask(__name__)
@app.route("/test/", methods=["GET", "POST"])
def get_args():
     logging.info("[请求⽅式]: {}".format(request.method))
     logging.info("[请求args]: {}".format(request.args))
     # 接收⽂件内容
     logging.info("[接收⽂件]: {}".format(request.files))
     file_obj = request.files.get("file_field_name")
     logging.info("[尝试获取⽂件字段对应内容]: {}".format(file_obj))
     logging.info("[尝试获取⽂件名]: {}".format(file_obj.filename))
     # 读取⽂件内容，如果需要重复读取，需要调整指针file_obj.seek(0, 0)
     logging.info("[第一次读取]：{}".format(file_obj.read()))
     logging.info("[第二次读取]：{}".format(file_obj.read()))
     logging.info(file_obj.read())
     # 调整指针，才可重复读取
     file_obj.seek(0, 0)
     logging.info("[第三次读取]：{}".format(file_obj.read()))
     logging.info(file_obj.read())
     # 保存到服务端，仍然需要重新调整指针
     file_obj.seek(0, 0)
     file_path = path + file_obj.filename
     file_obj.save(file_path)
     return "ok"


if __name__ == '__main__':
    app.run(debug=True)