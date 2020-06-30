import requests
from requests_toolbelt import MultipartEncoder
url = "http://127.0.0.1:5000/test/?a=1"
# 若传字典，则会被识别为 form，因为requests库默认使⽤application/x-www-formurlencoded
# data = {"name": "dcs"}
# r = requests.post(url=url, data=data)
# print(r.text)


# data = MultipartEncoder(
#  fields={ 'field0': 'xiepeng',
#     'field1': 'liujia',
#     }
# )
# print(data.content_type)
# # 必须添加content_type，否则会识别错误
# r = requests.post('http://127.0.0.1:5000/test/?a=1', data=data, headers={'ContentType': data.content_type})
# print(r.text)




# 若传字典，则会被识别为 form，因为requests库默认使⽤application/x-www-formurlencoded
# data = {"name": "bird1"}
# r = requests.post(url=url, data=data)
# print(r.text)
# 构造MultipartEncoder对象传参
data = MultipartEncoder(
 fields={
    'name': 'bird2',
    'age': "13",
    }
)
print(data.content_type)
# 必须添加content_type，否则会识别错误
r = requests.post('http://127.0.0.1:5000/test/?a=1', data=data, headers=
{'Content-Type': data.content_type})
print(r.text)