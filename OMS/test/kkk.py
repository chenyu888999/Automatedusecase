#-*- coding: utf-8 -*-
'''
@Time    : 2017/8/15 23:31
@Author  : 陈宇
@File    : kkk.py
@Software: PyCharm
@Describe: 
'''

from OMS.Keyword.Login import Login
from selenium import webdriver

a = {
    "chrome":"http://119.29.148.186:8081/wd/hub",

    "firefox":"http://119.29.148.186:8081/wd/hub"
    }
for i in a.items():
    print(i)
