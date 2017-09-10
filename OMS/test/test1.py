#-*- coding: utf-8 -*-
'''
@Time    : 2017/8/8 8:43
@Author  : 陈宇
@File    : pppp.py
@Software: PyCharm
@Describe: 
'''

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from OMS.Keyword.Element import Oms
import time,unittest,nose
from flaky import flaky



class test(unittest.TestCase):
    def setUp(self):
        self.driver = Oms("firefox")
        self.driver.get("http://192.168.10.223:61601/")
        self.driver.max_window()
        self.driver.find_element("id=userName").send_keys("gcwms")
        self.driver.find_element("id=userPass").send_keys("td123456")
        self.driver.find_element("id=login").click()



    def tearDown(self):
        self.driver.close()
        print("fdsf")


    @flaky(max_runs=3)
    def test(self):
        driver=self.driver
        driver.js("leftMenu('158','中转收货管理','/receiving/receiving/transfer-list?quick=158')")
        time.sleep(2)
        driver.switch_to_frame("id=iframe-container-158")
        # driver.find_element_by_id("operate-received-button").click()
        driver.clickxpath(".//*[@id='search-module-baseSearch']/div[5]/input")

        # table = driver.find_element_by_xpath(".//*[@id='receivedForm']/table")

        # table的总行数，包含标题
        # table_rows = table.find_elements_by_tag_name('tr')

        a = driver.get_table_rows(".//*[@id='receivedForm']/table")
        b = driver.get_table_cloumn(".//*[@id='receivedForm']/table", 1)
        c = driver.get_table_text(".//*[@id='receivedForm']/table", 2, 3)
        d = driver.get_table_text_row(".//*[@id='receivedForm']/tableppp", 4, "G296")
        driver.click_table_element(".//*[@id='receivedForm']/table", d, 4, "G296")
        print(d)




if __name__ == '__main__':
    unittest.main()


















