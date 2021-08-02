# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 声明浏览器对象
browser = webdriver.Chrome()
try:
    # 打开⽹站
    browser.get('https://www.baidu.com')
    # 定位元素
    input = browser.find_element_by_id('kw')
    # 往元素输⼊python
    input.send_keys('Python')
    # 输⼊回⻋
    input.send_keys(Keys.ENTER)
    # 等待时间
    wait = WebDriverWait(browser, 10)
    # 判断等待结果是否出现
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # 打印url
    print(browser.current_url)
    # 打印cookies
    print(browser.get_cookies())
    # 打印源代码
    print(browser.page_source)
finally:
    # 关闭浏览器
    browser.close()