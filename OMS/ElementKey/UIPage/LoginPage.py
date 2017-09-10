#-*- coding: utf-8 -*-
'''
@Time    : 2017/9/1 13:17
@Author  : 陈宇
@File    : LoginPage.py
@Software: PyCharm
@Describe: 
'''


from OMS.ElementKey.BaseKey.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    username_loc = (By.ID,"userName")
    password_loc = (By.ID,"userPass")
    commitbutton_loc = (By.CSS_SELECTOR,".loginbtn.radius5")

    def __init__(self,selenium_driver,base_url,base_title):
        super(LoginPage, self).__init__(selenium_driver,base_url,base_title)


    def open_url(self):
        self.open(self.base_url,self.base_title)

    def input_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.commitbutton_loc).click()