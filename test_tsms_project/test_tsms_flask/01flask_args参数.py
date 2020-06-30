import requests
# get请求只有args
# url = "http://192.168.31.237:5001/v1/3rd//"
# r = requests.get(url=url)
# print(r.text)

# # post请求也有可带args
url = "http://192.168.31.237:5001/v1/3rd//?a=1"
r = requests.post(url=url)
print(r.text)

#
# # 使⽤params带args参数
# url = "http://127.0.0.1:5000/test/"
# params = {"a": 1}
# r = requests.get(url=url, params=params)
# print(r.text)
