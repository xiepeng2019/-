# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/31
from pymongo import MongoClient

client = MongoClient("mongodb://148.70.194.135:27017/")
db=client.tsms_box
col=db.tsms_box
# test = {
#     "name":"测试年龄属性为null",
#     "age":""
# }
#
# tester = {
#     "name":"武汉加油",
#     "age":2020
# }
# mg=col.insert_one(test)
# print(mg.inserted_id)

"""查询MongoDB数据"""

cx = col.find()
# print(cx)
for i in cx:
    print(i)
"""正则匹配查询"""
# cx = col.find({'name':{'$regex':'武汉.*'}})
# for i in cx:
#     print(i)

"""属性是否存在"""
# cx = col.find({'age':{'$exists':False}})
# for i in cx:
#     print(i)

"""高级条件查询"""
# cx = col.find({'$where':'obj.age==obj.friends'})
# for i in cx:
#     print(i)