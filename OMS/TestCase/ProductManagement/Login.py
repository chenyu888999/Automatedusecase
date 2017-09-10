#-*- coding: utf-8 -*-
'''
@Time    : 2017/9/1 13:51
@Author  : 陈宇
@File    : caselogin.py
@Software: PyCharm
@Describe: 
'''

import unittest
from OMS.ElementKey.UIPage.LoginPage import LoginPage
from selenium import webdriver

class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "http://192.168.10.223:61604/"
        self.username="baker"
        self.password = "Baker888999"
        self.title = "中邮海外仓 - cpws"

    def tearDown(self):
        self.driver.close()

    def test1(self):
        login_page = LoginPage(self.driver,self.url,self.title)
        login_page.open_url()
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        login_page.click_submit()





if __name__=="__main__":
    unittest.main()

