# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
from multiprocessing import Process,Queue
from multiprocessing import Pool
import os
import time
import random
import threading


"""⽀持跨平台多进程"""
# def run_proc(name):
#     print('正在执⾏的⼦进程 %s (%s)...' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('⽗进程 %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('⼦进程准备执⾏.')
#     p.start()
#     p.join()
#     print('⼦进程执⾏完毕.')


"""通过进程池创建子进程"""
# def long_time_task(name):
#     print('执⾏任务 %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('任务 %s 执⾏了 %0.2f 秒.' % (name, (end - start)))
# if __name__ == '__main__':
#     print('当前进程的⽗进程号 %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('等待所有⼦进程加载...')
#     p.close()
#     p.join()
#     print('所有⼦进程执⾏完毕.')


"""
进程间通信,很重要，需要背下来
"""
# def write(q):
#     print('执⾏写操作的进程id: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('往队列写⼊ %s ...' % value)
#         q.put(value)
#         time.sleep(random.random())
# def read(q):
#     print('执⾏读操作的进程id: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('从队列读取 %s .' % value)
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

"""Python多线程"""
# def loop():
#     print('当前执⾏的线程是： %s ' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('线程 %s >>> 迭代 %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#         print('当前线程 %s 执⾏结束.' % threading.current_thread().name)
#     print('当前执⾏的线程是： %s ' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('当前线程 %s 执⾏完毕.' % threading.current_thread().name)




"""线程锁"""
# balance = 0
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for i in range(1000000):
#         change_it(n)
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
"""
真正的线程锁
优点：某段关键代码，只能由⼀个线程从头到尾执⾏，保证数据准确
缺点：线程不能并发，出现死锁
"""
lock = threading.Lock()
balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)