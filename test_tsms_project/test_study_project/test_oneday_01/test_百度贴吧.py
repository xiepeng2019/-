# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02

import requests
import random
import string
import os


url = 'https://tieba.baidu.com/hottopic/browse/topicList'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
r = requests.get(url,headers=headers)
a = r.json()

exp = []
def get5(getkey, res_dict):
    if isinstance(res_dict, dict):
        for k, v in res_dict.items():
            if k == getkey:
                # 把找到数据增加到exp中
                exp.append(v)
                # 如果每个v只要找一个，可以手动中断
            get5(getkey, v)
    elif isinstance(res_dict, list):
        for ele in res_dict:
            get5(getkey, ele)


get5("topic_pic", r.json())
for url in exp:
    name = ''.join(random.sample(string.ascii_lowercase, 5)) + '.jpg'
    pic_path = os.path.join(os.getcwd(), 'pic')
    pic_name = os.path.join(pic_path, name)
    # pic_dir = '/Users/panwj/mypython3/02teach_auto_test/01高级课程/递归字典/pic/hello.jpg'
    with open(pic_name, 'wb') as f:
        # 要下载图片，当然要先发起图片请求咯
        # 注意，这里也会使用全局变量 headers
        r_pic = requests.get(url, headers=headers)
        # 把图片内容写入到文件
        f.write(r_pic.content)
        # 关闭图片文件
        f.close()




class Testmoney():
    def test_01(self):
        assert 1 + 1 == 2



