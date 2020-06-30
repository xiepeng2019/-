import logging, requests
import time
import gevent

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')
from multiprocessing import Process, Pool
from tsms_base import TsmsBase

ts = TsmsBase()


def task():
    url = "http://www.captaintests.club/v1/message"
    data = {
        "sign_id": 16,
        "temp_id": 6,
        "mobiles": ts.gen_phones(1)
    }
    user = "dcs"
    password = "123"
    res = requests.post(url, json=data, auth=(user, password))
    logging.info(res.status_code)

"""多进程"""
def main1():
    start = time.time()
    p = Pool(8)
    for i in range(8):
        p.apply_async(task, args=())
    p.close()
    p.join()
    end = time.time()
    logging.info("[time is]: {}".format(end - start))

"""单进程"""
def main2():
    start = time.time()
    for i in range(8):
        task()
    end = time.time()
    logging.info("[time is]: {}".format(end - start))

"""多协程"""
def main4(num):
    start = time.time()
    a = [gevent.spawn(task) for i in range(int(num))]
    gevent.joinall(a)
    end = time.time()
    logging.info("[time is]: {}".format(end - start))
    logging.info("[tps is]: {}".format(num / (end - start)))

"""多进程+多协程"""
def main5(num):
    start = time.time()
    p1 = Process(target=main4,args=(num / 2,))
    p2 = Process(target=main4,args=(num / 2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    logging.info("[process + gevent tps is]:{}".format(num / (end - start)))

if __name__ == '__main__':
    main5(12)
    # main4(12)
    # main1()
    # main2()
    # task()