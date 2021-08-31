# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/31

import pytest,logging,json,sys,random
from json import JSONDecodeError
from test_study_project.test_oneday_01.test_skip_import import limit_ver
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s:')


# a = "test_input,expected"
# # b =  [
# #     ("1+1", 2),
# #     ("2*3", 6),
# #     #
# #     pytest.param("3-0", 3, marks=pytest.mark.xfail),
# # ]
# @pytest.mark.parametrize(a, b)
# def test_eval(test_input, expected):
#     logging.info("测试用例执行")
#     assert eval(test_input) == expected
#     logging.info(test_input)
#     logging.info(expected)

"""参数组合"""
# @pytest.mark.parametrize('a', [ 3, 3])
# @pytest.mark.parametrize('b', [4, 4])
# def test_01(a, b):
#     logging.info("测试⽤例执⾏ {} {}".format(a, b))
#     assert a != b

"""
多重前置+多重Parms
"""

# a = ["admin","root"]
# b = ["123","456"]
# @pytest.fixture(scope="module")
# def input_user(request):
#     user = request.param
#     logging.info(user)
#     return user
# @pytest.fixture(scope="module")
# def input_paw(request):
#     psw = request.param
#     return psw
# @pytest.mark.parametrize("input_user",a,indirect=True)
# @pytest.mark.parametrize("input_paw",b,indirect=True)
# def test_login(input_user,input_paw):
#     c = input_user
#     d = input_paw
#     logging.info("数据组合 {}{}".format(c,d))

"""
断言与异常
"""
# def test_json():
#     """触发异常"""
#     a = '''{'name':'dcs}'''
#     try:
#         a = '''{'name':'dcs}'''
#         b = json.load(a)
#     except Exception as c:
#         logging.info("捕获异常")
#         logging.info(c)

"""
捕获异常并断言
"""
# def test_json_error1():
#     a = '''{'name': 'dcs'}'''
#     with pytest.raises(JSONDecodeError, message="hello") as e:
#         b = json.loads(a)
# # 断⾔异常类型type，从json库导⼊
#     assert e.type == JSONDecodeError
# # 断⾔异常value值，需要转换str
#     assert "Expecting property name enclosed in double quotes: line 1 column 2(char 1)" in str(e.value)


# def test_json_error1():
#     a = '''{'name': 'dcs'}'''
#     with pytest.raises(JSONDecodeError, message="hello") as e:
#         b = json.loads(a)
#         logging.info("打印异常")
#  # 断⾔异常类型type，从json库导⼊
#     assert e.type == JSONDecodeError
#  # 断⾔异常value值，需要转换str
#     assert "Expecting property name enclosed in double quotes: line 1 column 2(char 1)" in str(e.value)




# def test_json_error():
#     '''触发异常'''
#     a = '''{'name': 'dcs'}'''
#     b = json.loads(a)
# def test_json_error1():
#     '''先捕获再断⾔'''
#     a = '''{'name': 'dcs'}'''
#     #    a = '''{"name": "dcs"}'''
#     #    b = json.loads(a)
#     try:
#         b = json.loads(a)
#     except JSONDecodeError as e:
#         logging.info("只要打印这⾏，则说明捕获到了异常")
#         logging.info(e)


"""
用例跳过
"""
# '''不执行该用例时使用上面的skip'''
#常用写法
# @pytest.mark.skip(reason="调试动作")
# def test_tiaoshi_01():
#     assert 2==2




# """装饰器标记"""
# def a():
#     logging.info("判断配置是否准确")
#     return False
# def test_b():
#     if not a():
#         pytest.skip("配置错误")
#     logging.info("如果没有跳过，则会执行这行")
#     assert 1 == 2
# def test_c():
#     assert 1 == 1



"""
命令行跳过
"""
# a = 2
# if a == 1:
#     pytest.skip("skipping windows-only tests",allow_module_level=True)
#
# def test_skip5():
#     logging.info("ok")
#     assert 1 == 1

#skipif条件跳过



# @limit_ver
# def test_function():
#     logging.info(sys.version_info)
#     logging.info("hello")
#     assert 1 == 1
# if __name__ == '__main__':
#  pytest.main(['-s'])




"""
xfail跳过
"""
#登录数据
test_login_data = [
    {"user":"dcs", "psw": "123"},
    {"user":"root", "psw":"123"}
]
# #登录前置模块
@pytest.fixture(scope="module")
def login(request):
    logging.info(request.param)
    user = request.param["user"]
    psw = request.param["psw"]
    logging.info(user)
    logging.info(psw)
    res = random.choice([True,False])
    logging.info("登录状态是：{}".format(res))
    return res
@pytest.mark.parametrize("login",test_login_data,indirect=True)
class TestMark():
    def test_login_01(self,login):
        res = login
        if not res:
            pytest.xfail("登录失败，标记为xfail")
        logging.info("i'm ok")
    def test_login_02(self,login):
        logging.info("sorry")



# """用例标记,等级划分"""
# class TestClsMark(object):
#     @pytest.mark.lv1
#     def test_01(self):
#         logging.info("日志")
#     def test_02(self):
#         logging.info("打印")



"""
pytest自定义命令行
"""
# def pytest_addoption(parser):
#     parser.addoption('--host_addr',action='store',default=None,help='传入host地址')
#     parser.addoption('--startall',action='store',default=None,help="标示执行全部用例")
# # # 2. 可通过⽅法返回，然后通过fixture透传，注意：这⾥使⽤pytestconfig获取参数
# @pytest.fixture()
# def host_address(pytestconfig):
#     # 这⾥的host_add⾃定义命名，将整个结果返回
#     logging.info("[pytestconfig为]:{}".format(pytestconfig))
#     return pytestconfig.getoption('--host_addr')
# @pytest.fixture()
# def host_address1(request):
#     # 这⾥的host_add⾃定义命名，将整个结果返回
#     return request.config.getoption('--host_addr')




# def test_ngix():
#     pytest.assume(1 + 1 == 2)


















# @pytest.fixture(scope="function")
# def tb(pytestconfig):
#     logging.info("[环境参数为]: {}".format(pytestconfig.getoption("--env")))
#     if pytestconfig.getoption("--env") == "pro":
#         return TsmsBase(env=2)
#     else:
#         return TsmsBase()
# def test_sign_api_create_07(self, tb):
#     """演示环境切换"""
#     data = tb.sign_data()
#     tb.req_post("sign", data)
#     assert isinstance(tb.json.get("sign_id"), int)








