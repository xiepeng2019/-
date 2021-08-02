# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium .webdriver import ActionChains
import time
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com')
# browser.maximize_window()
# # time.sleep(3)
# # mouse = browser.find_element_by_link_text("设置")
# # ActionChains(browser).move_to_element(mouse).perform()#鼠标悬停
# time.sleep(4)
# # browser.quit()
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')
# browser.quit()


# browser.get('https://www.taobao.com')
# # 通过js代码，来实现浏览器操作，下拉到最下⾯
# time.sleep(5)
# # browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# # # 弹出altert提示框
# # browser.execute_script('alert("To Bottom")')
# target = browser.find_element_by_css_selector("li.mod.conve-item-5.min")
# browser.execute_script("arguments[0].scrolllntoView();",target)


# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
# import time
# browser=webdriver.Chrome()
# browser.get('https://www.baidu.com')
# mouse=browser.find_element_by_link_text("设置")
# #执行动作链，鼠标移动到设置上
# ActionChains(browser).move_to_element(mouse).perform()
# browser.find_element_by_link_text("搜索设置").click()
# time.sleep(3)
# s=browser.find_element_by_name("NR")
# #通过text:select_by_visible_text(),操作下拉框选项
# Select(s).select_by_visible_text("每页显示50条")
# time.sleep(3)
# browser.quit()


# from selenium import webdriver
# browser = webdriver.Chrome()
# # 隐式等待
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_css_selector(".Button.AppHeader-login.Button--blue")
# print(input)



# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com/')
# 构造wait对象，最⻓等待10秒，1秒轮询⼀次，默认是0.5秒轮询⼀次
# wait = WebDriverWait(browser, 10, poll_frequency=1)
# 注意：需要传⼊⼀个函数对象
# input = wait.until(lambda x : x.find_element_by_id("kw"))
# input.send_keys("hello")
# time.sleep(2)
# browser.quit()

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.captaintests.club')
browser.find_element_by_id("inputUsername").send_keys("dec")
browser.find_element_by_id("password").send_keys("123")
browser.find_element_by_class_name("form-signin").click()
c = browser.get_cookies()
print(c)

time.sleep(3)
browser.get('http://www.captaintests.club/user/dcs/sign')
time.sleep(3)
browser.quit()





