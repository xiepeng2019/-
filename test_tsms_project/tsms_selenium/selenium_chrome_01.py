from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import time
b = webdriver.Chrome()
b.get('https://www.baidu.com')
time.sleep(5)
#随机打开一个网页
a = b.find_element_by_id('kw')
a.send_keys('吃货')
a.send_keys(Keys.ENTER)
time.sleep(3)
links=b.find_elements_by_css_selector("h3.t>a")
links[random.randint(0,9)].click()
# print(a)
# print(b.current_url)
#通过链接
# input = b.find_element_by_link_text('秒杀').click()
# print(b.current_url)
# print(input.text)

# 通过classname 查找京东左边栏
# c = b.find_elements_by_css_selector("ul li.service_item")
# for i in c:
#         print(i.text)


