# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "xiepeng"
# Date: 2021/08/02
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.jd.com')
# 1. 使⽤id，*代表所有标签
# a = browser.find_element_by_xpath("//*[@id='q']")
# 2. 使⽤name
# a = browser.find_element_by_xpath("//*[@name='q']")
# 3. 使⽤class
# a = browser.find_element_by_xpath("//*[@class='search-combobox-input']")
# 4. 还可以使⽤其他属性：role="combobox"
# a = browser.find_element_by_xpath("//*[@role='combobox']")
# 5. 如果同个属性，同名的⽐较多，也可以指定标签，会更准确
a = browser.find_element_by_xpath("//input[@id='key']")
print(a)
browser.quit()
