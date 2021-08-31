# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/31

import requests
import json
import sys
import pytest

# class student(object):
#     def __init__(self, name, age):
#         self.__name= name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get__age(self):
#         return self.__age
#
#     def set_name(self, name):
#         if 20<=int(name)<=100:
#             self.__name = name
#         else:
#             raise ValueError("invalid name para")
#         self.__name = name
#
# a = student("谢鹏",26)
# a.set_name(78)
# a.get_name(7/8)

"""子类继承父类"""
# class a(object):
#     def run(self):
#         print("testing")
#
# class b(a):
#
#     def run(self):
#         print("testing laoshi")

# class Testmoney():
#     def test_money_1(self):
#         assert 1+1 == 2
a = [1,2,3,4,5,6,7]
def get_5(x):
    if x > 5:
        return False
b = filter(get_5,a)
print(list(b))






















