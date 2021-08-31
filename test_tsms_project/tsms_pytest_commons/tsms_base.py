# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02

import random
import string
import os
import json
import pytest
import requests
from tsms_pytest_commons.common_tools.common_decorator import logging, logit
from tsms_pytest_commons.configs.tsms_base_config import *


class TsmsBase(object):
    def __init__(self, env=0):
        if env == 0:
            self.head_url = url_config.get("test")
        elif env == 1:
            self.head_url = url_config.get("dev")
        elif env == 2:
            self.head_url = url_config.get("pro")
        else:
            self.head_url = url_config.get("test")

        self.s = requests.session()

        self.headers = url_config.get("default_headers")
        self.tieba = url_config.get("tieba")


        self.user = account_config.get("default_user")
        self.passwd = account_config.get("default_passwd")
        self.root = account_config.get("root_user")
        self.root_pass = account_config.get("root_passwd")

        self.phone_heads = data_config.get("default_heads")
        self.sign_id = data_config.get("default_sign_id")
        self.temp_id = data_config.get("default_temp_id")

        self.status_code = ''
        self.text = ''
        self.json = {}
        self.exp_str = ''

    def choice_url(self, url_type):
        if url_type == 'sign':
            url = self.head_url + '/v1/signature'
        elif url_type == 'temp':
            url = self.head_url + '/v1/template'
        elif url_type == 'message':
            url = self.head_url + '/v1/message'
        elif url_type == 'send':
            url = self.head_url + '/v1/message'
        elif url_type == "sign_review":
            url = self.head_url + '/v2/signreview'
        elif url_type == "temp_review":
            url = self.head_url + '/v2/tempreview'
        elif url_type == 'charge':
            url = self.head_url + '/v2/charge'
        else:
            return url_type
        logging.info("[当前请求的地址是]: {}".format(url))
        return url

    def req_get(self, url, *, headers=None):
        """请求前端链接，获取到一个json数据 或 text数据"""
        hd = headers if headers else self.headers
        r = requests.get(url, headers=hd)
        try:
            res = r.json()
        except Exception as e:
            logging.warning("[tsms_get的res转json触发异常]:{}".format(e))
            res = r.text
        return res

    @logit
    def tsms_get(self, url_type, user=None, passwd=None, *, headers=None):
        url = self.choice_url(url_type)
        if user and passwd:
            user, passwd = user, passwd
        else:
            user, passwd = self.user, self.passwd
        logging.info("[鉴权用户密码为]: {} {}".format(user, passwd))
        hd = headers if headers else self.headers
        response = requests.get(url, auth=(user, passwd), headers=hd)
        self.status_code = response.status_code
        logging.info("[返回码是:] {}".format(self.status_code))
        self.json = response.json()
        logging.info("[返回内容是]: {}".format(self.json))
        return self.json

    @logit
    def req_post(self, url_type, data, user=None, passwd=None, *, headers=None):
        url = self.choice_url(url_type)
        hd = headers if headers else self.headers
        if user and passwd:
            user, passwd = user, passwd
        else:
            user, passwd = self.user, self.passwd
        logging.info("[鉴权用户密码为]: {} {}".format(user, passwd))
        response = requests.post(url, json=data, auth=(user, passwd), headers=hd)
        self.status_code = response.status_code
        logging.info("[返回码是:] {}".format(self.status_code))
        try:
            self.json = response.json()
            logging.info("[返回内容是]: {}".format(self.json))
            return self.json
        except Exception as e:
            logging.warning("[req_post的res转json触发异常]:{}".format(e))
            self.text = response.text
            return self.text

    @logit
    def req_delete(self, url_type, data, user=None, passwd=None, *, headers=None):
        url = self.choice_url(url_type)
        hd = headers if headers else self.headers
        if user and passwd:
            user, passwd = user, passwd
        else:
            user, passwd = self.user, self.passwd
        response = requests.delete(url, json=data, auth=(user, passwd), headers=hd)
        self.status_code = response.status_code
        logging.info("[req_delete 返回码是:] {}".format(self.status_code))
        try:
            self.json = response.json()
            logging.info("[返回内容是]: {}".format(self.json))
            return self.json
        except Exception as e:
            logging.warning("[req_delete 触发异常]".format(e))
            self.text = response.text
            logging.info("[返回内容是]: {}".format(self.text))
            return self.text

    @logit
    def req_put(self, url_type, data, user=None, passwd=None, *, headers=None):
        url = self.choice_url(url_type)
        hd = headers if headers else self.headers
        if user and passwd:
            user, passwd = user, passwd
        else:
            user, passwd = self.user, self.passwd
        response = requests.put(url, json=data, auth=(user, passwd), headers=hd)
        self.status_code = response.status_code
        logging.info("[req_put 返回码是:] {}".format(self.status_code))
        try:
            self.json = response.json()
            logging.info("[返回内容是]: {}".format(self.json))
            return self.json
        except Exception as e:
            logging.warning("[req_put 触发异常]".format(e))
            self.text = response.text
            logging.info("[返回内容是]: {}".format(self.text))
            return self.text

    def signid_exist(self, sign_id, user=None, passwd=None):
        """判断签名id是否存在"""
        if user and passwd:
            user, passwd = user, passwd
        else:
            user, passwd = self.user, self.passwd
        res = self.tsms_get("sign", user=user, passwd=passwd)
        # 注意：get请求返回的key是id
        sign_ids = self.recur("id", res)
        if sign_id in sign_ids:
            return True
        else:
            return False

    def get_field(self, field, **kwargs):
        """解析get请求的指定字段"""
        for k, v in kwargs.items():
            for d in self.json["items"]:
                if d[k] == v:
                    logging.info("[当前查询字段 {} 的值是]: {}".format(field, d[field]))
                    return d[field]
        logging.error("[未找到指定的字段]: {}".format(field))

    @logit
    def review(self, review_type, review_id, audit_status, reject_reason=None, user=None, passwd=None):
        if user:
            user, passwd = user, passwd
        else:
            user, passwd = self.root, self.root_pass
        data = {
            "audit_status": audit_status,
            "reject_reason": reject_reason
        }
        if review_type == "sign":
            url = self.choice_url("sign_review")
            data["sign_id"] = review_id
        elif review_type == "temp":
            url = self.choice_url("temp_review")
            data["temp_id"] = review_id
        else:
            logging.error("[审核参数有误]: {}".format(review_type))
            return
        logging.info("[请求地址是]: {}".format(url))
        res = requests.post(url, json=data, auth=(user, passwd), headers=self.headers)
        logging.info("[审核结果是]: {} {} ".format(res.status_code, res.text))
        self.status_code = res.status_code
        try:
            self.json = res.json()
            return self.json
        except Exception as e:
            self.text = res.text
            return self.text

    def recur(self, key, res):
        """从字典中解析需要的字段，将所有解析结果组成列表返回"""
        self.exp_list = []

        def get(getkey, res_dict):
            if isinstance(res_dict, dict):
                for key, value in res_dict.items():
                    if key == getkey:
                        logging.info("[当前解析的字段是 {} 解析结果是]: {}".format(key, value))
                        self.exp_list.append(value)
                        break
                    get(getkey, value)
            elif isinstance(res_dict, list):
                for ele in res_dict:
                    get(getkey, ele)

        get(key, res)
        if len(self.exp_list) == 1:
            return self.exp_list[0]
        return self.exp_list

    def download_by_url(self, url, dir='testdata'):
        """通过链接下载内容，存放到本地"""
        pic_path = os.path.join(os.getcwd(), dir)
        name = ''.join(random.sample(string.ascii_lowercase, 5)) + '.jpg'
        pic_name = os.path.join(pic_path, name)
        with open(pic_name, 'wb', encoding="utf-8") as f:
            r_pic = requests.get(url, headers=self.headers)
            f.write(r_pic.content)
            f.close()

    def download_all(self, url_list):
        """下载所有链接"""
        if isinstance(url_list, list):
            for url in url_list:
                logging.info("[当前下载的链接是]: ".format(url))
                self.download_by_url(url)
        else:
            logging.error("[传入的链接格式有误]:".format(url_list))

    def gen_ranstr(self, num_int=0, num_letters=0, num_zh=0, num_pun=0):
        """生成随机字符串"""
        a = [random.choice(string.digits) for i in range(int(num_int))]
        b = [random.choice(string.ascii_letters) for i in range(int(num_letters))]
        c = [chr(random.randint(0x4e00, 0x9fbf)) for i in range(int(num_zh))]
        d = [random.choice(string.punctuation) for i in range(int(num_pun))]
        ran_list = a + b + c + d
        random.shuffle(ran_list)
        return ''.join(ran_list)

    def gen_phones(self, num, phone_heads=None):
        """生成随机号码，可以指定数量，返回一个列表"""
        if not phone_heads:
            phone_heads = self.phone_heads
        head_list = phone_heads.split(',')
        phone_list = []
        for i in range(int(num)):
            phone_head_list = random.sample(head_list, 1)
            phone_head = phone_head_list[0]
            len_body = 11 - len(phone_head)
            b = ''.join(random.sample(string.digits, len_body))
            phone = phone_head + b
            phone_list.append(phone)
        return phone_list

    # 可以把函数封装成属性，通过：self.sign_data来使用
    def sign_data(self, signature=None, source=None, pics=None):
        signature = signature if signature else self.gen_ranstr(3, 3)
        source = source if source else self.gen_ranstr(0, 4)
        pics = pics if pics else [self.gen_ranstr(3, 3)]
        data = {
            "signature": signature,  # 必填
            "source": source,  # 必填
            "pics": pics  # 选填
        }
        return data

    def temp_data(self, sign_id=None, type=None, name=None, template=None, description=None):
        sign_id = sign_id if sign_id else self.sign_id
        type = type if type else 1
        name = name if name else self.gen_ranstr(3, 3)
        template = template if template else self.gen_ranstr(5, 5)
        description = description if description else self.gen_ranstr(5, 5)
        data = {
            "sign_id": sign_id,
            "type": type,
            "name": name,
            "template": template,
            "description": description,
        }
        return data

    def send_data(self, num=None, sign_id=None, temp_id=None):
        num = int(num) if num else 1
        sign_id = int(sign_id) if sign_id else self.sign_id
        temp_id = int(temp_id) if temp_id else self.temp_id
        data = {
            "sign_id": sign_id,  # 必填
            "temp_id": temp_id,  # 必填
            "mobiles": self.gen_phones(int(num))
        }
        return data

    def charge_data(self, user=None, charge=None):
        user = user if user else self.user
        charge = charge if charge else random.randint(1, 1000)
        data = {
            "user": user,
            "charge": charge
        }
        return data

    def check_sign(self):
        # assert isinstance(r["sign_id"], int), "签名id类型有误"
        assert isinstance(self.json["sign_id"], int), "签名id类型有误"

    def check_fail(self, code, msg):
        assert self.status_code == code, "[期待返回码是:{} 但实际返回是]: {}".format(code, self.status_code)
        assert self.json == msg, "[预期返回结果是:{}，但实际返回是:]{}".format(msg, self.json)

    def gen_para_fail(self, para_type):
        """
        夹具生成器
        """
        if para_type == "sign":
            data = self.sign_data()
        elif para_type == "sign":
            data = self.temp_data()
        elif para_type == "message":
            data = self.send_data()
        else:
            data = self.sign_data()

        @pytest.fixture(scope="function")
        def para_fail(request):
            """
            测试夹具：测试所有异常data
            """
            code = request.param.get("http_code")
            exp = request.param.get("expect")
            logging.info("[获取的code 和 exp 是]: {} {}".format(code, exp))
            for k, v in request.param.items():
                if k in data:
                    data[k] = v
            self.req_post(para_type, data=data)
            assert self.status_code == code
            assert self.json == exp

        return para_fail


if __name__ == '__main__':
    ts = TsmsBase()
    a = ts.gen_phones(10, "139,189")
    print(a)
    # b = ts.gen_ranstr(2, 2, 2, 2)
    # print(b)
