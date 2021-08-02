# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
from locust import HttpLocust, TaskSet, task
user = "dcs"
passwd = 123
class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login",{
            "username":user,
            "password":123
        })
    @task(2)
    def index(self):
        self.client.get("/index")

    @task(1)
    def about(self):
        self.client.get("/user/{}/".format(user))
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://www.captaintests.club/login"
    min_wait = 1000
    max_wait = 5000