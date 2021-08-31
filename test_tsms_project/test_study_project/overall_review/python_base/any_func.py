# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/31

import random,string
"""随机数练习"""
def create_str(num_int=0,num_letters=0,num_zh=0,num_pun=0):
    list = []
    for i in range(num_int):
        list.append(random.choice(string.digits))
    for i in range(num_letters):
        list.append(random.choice(string.ascii_letters))
    for i in range(num_zh):
        list.append(chr(random.randint(0x4e00,0x9fbf)))
    for i in range(num_pun):
        list.append(random.choice(string.punctuation))
    random.shuffle(list)
    return ''.join(list)
# print(string.punctuation)
a = create_str(1,1,1,1)
print(a)



n = 0
for i in range(11):
    n = n+i
print(n)

def old():
    print('step 1')
    yield (1)
    print('step 2')
    yield (2)
h = old()
next(h)



import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.info("[当前调⽤的函数是]: {}".format(func.__name__))
        for i in range(len(args)):
            logging.info("[第{}个参数是]: {}".format(i, args[i]))
        for k, v in kwargs.items():
            logging.info("key is: {} value is: {}".format(k, v))
        return func(*args, **kwargs)
    return wrapper
@use_logging
def add(a, b):
    c = a + b
    return c
@use_logging
def test(x, y, z=2):
    return x + y -z

add(a=1, b=44)
test(1,2,z=3)