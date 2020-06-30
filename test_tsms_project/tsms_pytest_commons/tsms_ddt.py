import re, time
from tsms_pytest_commons.tsms_base import TsmsBase


def ddt_random(text, key="random"):
    """替换${random}为随机字符"""
    ts = TsmsBase
    data = re.sub(r'\${%s}' % key, ts.gen_ranstr(4, 4), text)
    return data


def ddt_random_all(ff, *args):
    a = ''
    print(len(args))
    for i in range(len(args)):
        if i == 0:
            a = ddt_random(ff, args[0])
        a = ddt_random(a, args[i])
    return a


def aa():
    a = 1 + 1
    time.sleep(5)
    return a


if __name__ == '__main__':
    print(aa())
    # a = '''{"name": "${name}", "template": "${template}", "type": 1, "description": "${description}", "sign_id": 1}'''
    # # 新需求
    # b = ddt_random(a, "name")
    # c = ddt_random(b, "template")
    # d = ddt_random(c, "description")
    # print(b)
    # print(c)
    # print(d)
    # a = ddt_random_all(a, "name")
    # print(a)
