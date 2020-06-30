import requests,json,time

url_web='https://testcustomer.yidayuntu.cn/login'
data = {
    "username": "yida",
    "password": "01234567"
}
headers = {
    "paramKey": "C92EB6DBCC6DAB184183217D820DF951",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

response = requests.post(headers=headers,url=url_web,json=data)
print(response.json())