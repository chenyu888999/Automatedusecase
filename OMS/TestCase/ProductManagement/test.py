#-*- coding: utf-8 -*-
'''
@Time    : 2017/7/14 17:39
@Author  : 陈宇
@File    : test.py
@Software: PyCharm
@Describe: 
'''


import unittest,time
from OMS.Keyword.Element import Oms


driver = Oms("firefox")  # 初始化环境以及登陆操作
driver.max_window()
driver.get("http://192.168.10.228:60301/zh-CN/OrdinaryPurchase/PurchasePlanOrderList")
driver.send_keys("id=userCode", "kangkang")
driver.send_keys("id=myPassword", "lfk@#43374")
driver.click("id=submit")
driver.get("http://192.168.10.228:60301/zh-CN")
driver.clickxpath("html/body/div[2]/div/ul/li[2]/a")
driver.clickxpath("html/body/div[2]/div/ul/li[2]/div/a[1]")
time.sleep(2)
driver.clickxpath("/html/body/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/table/tbody/td[2]/a")