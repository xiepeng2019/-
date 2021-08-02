# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02

import logging
import queue
import re
import requests
from locust import TaskSet, task, HttpLocust

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


class UserLogin(TaskSet):
    def on_start(self):
        self.reg_url = "http://www.captaintests.club/login"
        res = requests.get(self.reg_url, allow_redirects=False)
        pat = re.compile('''<input id="csrf_token" name="csrf_token" type="hidden" value="(.*?)">''', re.S)
        self.token = re.findall(pat, res.text)[0]
        self.ck = res.cookies
        logging.info("[token is]: {}".format(self.token))
        logging.info("[cookie is]: {}".format(self.ck))

    @task
    def test_register(self):
        try:
            data = self.locust.user_data_queue.get()
            data_origin = data
        except queue.Empty:
            logging.info("[test data empty, exit send]")
            exit(0)
        data["csrf_token"] = self.token
        logging.info(data)
        with self.client.post("/login", data=data, cookies=self.ck, catch_response=True) as res:
            logging.info(res.status_code)
            if res.status_code == 200 and data.get("username") in res.text:
                res.success()
            else:
                res.failure("[unknow fail]")
        self.locust.user_data_queue.put(data_origin)


class WebsiteUser(HttpLocust):
    host = "http://www.captaintests.club"
    task_set = UserLogin
    user_data_queue = queue.Queue()
    for index in range(1000):
        data = {
            "username": "xiepeng%04d" % index,
            "password": "xie%04d" % index,
        }
        user_data_queue.put_nowait(data)
    min_wait = 0
    max_wait = 0