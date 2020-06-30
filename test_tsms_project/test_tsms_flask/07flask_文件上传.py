import requests
from requests_toolbelt import MultipartEncoder
# 参数说明：
# ('name', (None, 'dcs')) 1. files字段名 2. ⽂件名 3. ⽂件内容
# 1. 如果⽂件名为None，⽂件内容是⼀个字符串，则requests会将其视为 form内容发送
# 2. 如果⽂件名不为None，且⽂件内容为⼀个⽂件对象，则requests将其视为files 发送
files = [
    ('name', (None, 'dcs')),
    ("file_field_name", ("file_name", open("file.txt", "r"))) # "r" ⽅式 与"rb"⽅式都可
]
url = "http://127.0.0.1:5000/test?a=1"
r = requests.post(url=url, files=files)
print(r.text)


# data = MultipartEncoder(
#  fields={
#     'field0': 'value', # form内容
#     'field1': 'value', # form内容
#     'field2': ('filename', open('file.txt', 'rb')) # ⽂件内容，只可rb⽅式打开
#     }
# )
# r = requests.post('http://127.0.0.1:5000/test?a=1', data=data, headers={'ContentType': data.content_type})
# print(r.text)