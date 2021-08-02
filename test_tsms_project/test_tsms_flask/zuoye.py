# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import requests
import time
# url = 'http://30116895cy.qicp.vip/v1/3rd/'
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#     'Content-Type': 'application/json'}
# data = {
#         "uid":"xiepeng",
#         "content":"send",
#         "phone":"123143124"
# }
# user="xiep"
# passwd="993715"
# r = requests.post(url=url, headers=headers, json=data)
# print(r.text)
#
#
url = "http://g30113y639.qicp.vip/v1/3rd"
data = {
    "uid": 123,
    "content": "hello",
    "phone": 13899998888
}
start = time.time()
res = requests.post(url, json=data)
end = time.time()
print(res.status_code, res.text, end - start)