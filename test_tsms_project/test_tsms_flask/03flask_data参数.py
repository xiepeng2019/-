import requests
# post请求也有可带args
url = "http://127.0.0.1:5000/test/?a=1"
# 1. 直接传字符串，data=data，服务端会识别成为 data 参数，内容解析为字符串
# data = "hello"
# r = requests.post(url=url, data=data)
# print(r.text)

# 2. 直接传字典，data=data，因为requests库默认使⽤application/x-www-formurlencoded，客户端会处理成form
# 服务端会识别到 form，内容解析为字典，所以识别data为空，注意json是为空的！
data = {"name": "hello"}
r = requests.post(url=url, data=data)
print(r.text)

# 3. 通过json=data关键字传参数，服务端会识别 data 参数，但是是json串，同时json内容识别正常
data = {"name": "hello"}
r = requests.post(url=url, json=data)
print(r.text)