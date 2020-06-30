import gevent,time,logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')
# def foo():
#     print('开始执⾏ foo')
#     gevent.sleep(0)
#     print('切换上下⽂ foo')
# def bar():
#     print('开始执⾏ bar')
#     gevent.sleep(0)
#     print('切换上下⽂ bar')
# gevent.joinall([
#  gevent.spawn(foo),
#  gevent.spawn(bar),
# ])


"""
模拟IO阻塞调⽤，协程异步
"""
# from gevent import select
# start = time.time()
# tic = lambda: '时间差为: %1.1f' % (time.time() - start)
# def gr1():
#     print('gr1开始轮询: %s' % tic())
#     select.select([], [], [], 2)
#     print('gr1结束轮询: %s' % tic())
# def gr2():
#     print('gr2开始轮询时间: %s' % tic())
#     select.select([], [], [], 2)
#     print('gr2结束轮询: %s' % tic())
# def gr3():
#     print("gr3执⾏时间, %s" % tic())
#     gevent.sleep(1)
#     print("gr3执⾏完毕, %s" % tic())
# gevent.joinall([
#  gevent.spawn(gr1),
#  gevent.spawn(gr2),
#  gevent.spawn(gr3),
# ])



""""
同步执⾏与异步执⾏
"""
# import time
# import gevent
# import random
# def task(pid):
#  # gevent.sleep(random.randint(0, 2) * 0.001)
#     gevent.sleep(0.1)
#     print('任务完成: %s' % pid)
# def synchronous():
#     start = time.time()
#     for i in range(0, 10):
#         task(i)
#     end = time.time()
#     print("同步任务执⾏时间: {}".format(end - start))
#
#
# def asynchronous():
#      start = time.time()
#      threads = [gevent.spawn(task, i) for i in range(10)]
#      gevent.joinall(threads)
#      end = time.time()
#      print("异步任务执⾏时间: {}".format(end - start))
#
#
# print('执⾏同步任务:')
# synchronous()
# print('执⾏异步任务:')
# asynchronous()


"""
同步与异步发http请求
"""
# import time
# import gevent.monkey
# gevent.monkey.patch_socket()
# import gevent
# import requests
# def fetch(pid):
#     response = requests.get('http://httpbin.org/get', timeout=50)
#     print('请求结果 %s: %s' % (pid, response.status_code))
#     return response.text
# def synchronous():
#     start = time.time()
#     for i in range(1, 10):
#         fetch(i)
#     end = time.time()
#     print("同步任务执⾏时间: {}".format(end - start))
# def asynchronous():
#     start = time.time()
#     threads = []
#     for i in range(1, 10):
#         threads.append(gevent.spawn(fetch, i))
#         gevent.joinall(threads)
#     end = time.time()
#     print("异步任务执⾏时间: {}".format(end - start))
# print('同步执⾏:')
# synchronous()
# print('异步执⾏:')
# asynchronous()


"""
猴⼦补丁
"""
import time,requests,json
from gevent import monkey;monkey.patch_all()
import gevent
import socket
from tsms_base import TsmsBase
ts = TsmsBase()
url = "http://www.captaintests.club/v1/message"
def task():
    data = {
    "sign_id": 16,
    "temp_id": 6,
    "mobiles": ts.gen_phones(1)
    }
    user = "dcs"
    password = "123"
    res = requests.post(url, json=data, auth=(user, password))
    logging.info(res.status_code)


def get_time(url):
    start = time.time()
    ip = socket.gethostbyname(url)
    time.sleep(1)
    end = time.time()
    print("耗时", end - start, url)
    return ip
start = time.time()
jobs = [gevent.spawn(get_time, url) for url in url]
gevent.joinall(jobs, timeout=1)
end = time.time()
print("总耗时", end - start)
print([job.value for job in jobs])








