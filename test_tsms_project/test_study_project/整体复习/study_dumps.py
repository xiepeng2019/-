import json
import records

""""序列化"""
data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
"""将 Python 对象编码成 JSON 字符串"""
b = json.dumps(data)
# print(b,type(b))
"""将已编码的 JSON 字符串解码为 Python 对象"""
c = json.loads(b)
print(c,type(c))


