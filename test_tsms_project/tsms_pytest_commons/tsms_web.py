# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
import os
import sys
import re
import logging
import requests
from configs.tsms_web_config import *
sys.path.append(os.getcwd())            #告诉pytest运行前先检索当前路径
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


# 定义类
class TsmsWeb(object):

    def __init__(self):
        self.s = requests.session()
        self.url_head = url_web
        self.user = account_config.get("default_user")
        self.passwd = account_config.get("default_passwd")

    def login_c(self, user=None, passwd=None):
        if user and passwd:
            user, passwd = user, passwd
        else:
            user, passwd = self.user, self.passwd
        url = url_config.get("login")
        try:
            r = self.s.get(url)
            csrf_token = re.findall(r'csrf_token.*?value="(.*?)">-', r.text)[0]
            logging.info("[获取页面token]: {}".format(csrf_token))
        except:
            logging.WARN("[获取页面token失败]")
            return
        data = {
            "username": user,
            "password": passwd,
            "submit": "Login",
            "csrf_token": csrf_token
        }
        r2 = self.s.post(url, data=data)
        return r2.text

    def is_login(self, user=account_config.get("default_user")):
        url = self.url_head + '/user/%s' % user
        logging.info("[现在登录页面是]: {}".format(url))
        res = self.s.get(url)
        if "资料" in res.text:
            logging.info("登录成功")
            return True
        else:
            logging.WARN("登录失败")
            return False

    def reg_sign(self, user=account_config.get("default_user")):
        url = self.url_head + '/user/%s/sign' % user
        logging.info("[现在要正则匹配的页面是]: {}".format(url))
        html = self.s.get(url).text
        a = re.findall("<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?</tr>", html, re.S)
        return a

    def reg_temp(self, html):
        pass

    def reg_send(self, user=account_config.get("default_user")):
        url = self.url_head + "/user/%s/history" % user
        logging.info("[现在要正则匹配的页面是]: {}".format(url))
        html = self.s.get(url).text
        a = re.findall("<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?</tr>", html, re.S)
        return a

    def get_res(self, exp_id, records_list):
        exp_res = ''
        for record in records_list:
            if str(exp_id) in record:
                exp_res = record
        return exp_res

    def close(self):
        self.s.close()

    def get_web_session(self):
        """获取session"""
        self.login_c()
        assert self.is_login()
        return self.s


if __name__ == '__main__':
    tb = TsmsWeb()
    user = 'dcs'
    passwd = '123'
    tb.login_c(user, passwd)
    tb.is_login(user)
    sign_list = tb.reg_sign(user)
    for i in sign_list:
        print(i)
