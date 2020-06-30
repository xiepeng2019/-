import re,random,pytest,logging
"""学习第一天12-11"""

"""for与else 合法性"""
# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i)
# else:
#     print('ok')

"""else会先行执行完成for循环，然后才会执行if语句"""
# for i in [1,2,3,4,5,6]:
#     if i>2:
#         print(i)
# else:
#     print('ok')

"""列表推导式"""
# a = [1,2,3,4,5,6,7]
# result = list(i*i for i in a )
# print(result)

"""python去除列表中的空字符及\n和特殊字符"""
str ="""
    aa*aa

    bbbb
    cc&&cc
    
"""
# a = str.split('\n')
# result = list(filter(None,list(map(lambda x:re.sub('[*|&| ]','',x),a))))
# print(result)

# name = ["liwenli","xiepeng","zhenghaijuan","tongchengpeng"]
# age = [28,26,25,24]
# height = [173,179,175,158]
# """姓名：年龄：岁 身高：cm"""
# b = zip(name,age)
# print(dict(b))






@pytest.fixture(scope='function')
#指定login为前置
def login():
    logging.info("自定义前置")

#函数当做参数传入
def test_01(login):
    logging.info("test_01执行")
    x = "apple"
    assert 'l' in x

def test_02():
    logging.info("test_02执行")
    assert 2!=3















def test_study():
    pass





















