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
import time


driver = webdriver.Firefox()
driver.get("http://192.168.10.223:61601/")
driver.maximize_window()
driver.find_element_by_id("userName").send_keys("gcwms")
driver.find_element_by_id("userPass").send_keys("td123456")
driver.find_element_by_id("login").click()
driver.execute_script("leftMenu('158','中转收货管理','/receiving/receiving/transfer-list?quick=158')")
time.sleep(2)
driver.switch_to_frame("iframe-container-158")
#driver.find_element_by_id("operate-received-button").click()
driver.find_element_by_xpath(".//*[@id='search-module-baseSearch']/div[5]/input").click()

table = driver.find_element_by_xpath(".//*[@id='receivedForm']/table")

#table的总行数，包含标题
table_rows = table.find_elements_by_tag_name('tr')
print(len(table_rows))
table_cols = table_rows[0].find_elements_by_tag_name('td')
print(len(table_cols))

row1_col2 = table_rows[1].find_elements_by_tag_name('td')[2].text
print(row1_col2)

for index,i in enumerate(table_rows):
    if i.find_elements_by_tag_name('td')[4].text == "G591":
        b = index
        print(b)



        table_rows[b].find_elements_by_tag_name('td')[4].find_element_by_link_text("G591").click()
        break


time.sleep(10)

#driver.close()


'''
def get_table_rows():


def get_table_cloums():

def get_table_text():

def table_should_contain():
'''








