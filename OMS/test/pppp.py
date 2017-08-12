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
import time


driver = Oms("firefox")
driver.get("http://192.168.10.223:61601/")
driver.max_window()
driver.find_element("id=userName").send_keys("gcwms")
driver.find_element("id=userPass").send_keys("td123456")
driver.find_element("id=login").click()
driver.js("leftMenu('158','中转收货管理','/receiving/receiving/transfer-list?quick=158')")
time.sleep(2)
driver.switch_to_frame("id=iframe-container-158")
#driver.find_element_by_id("operate-received-button").click()
driver.clickxpath(".//*[@id='search-module-baseSearch']/div[5]/input")

#table = driver.find_element_by_xpath(".//*[@id='receivedForm']/table")

#table的总行数，包含标题
#table_rows = table.find_elements_by_tag_name('tr')

a = driver.get_table_rows(".//*[@id='receivedForm']/table")
b = driver.get_table_cloumn(".//*[@id='receivedForm']/table",1)
c = driver.get_table_text(".//*[@id='receivedForm']/table",2,3)
time.sleep(2)
d = driver.get_table_text_row(".//*[@id='receivedForm']/table",4,"G591")

print(d)

driver.click_table_element(".//*[@id='receivedForm']/table",d,4,"G591")
time.sleep(2)
driver.close()






'''


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

driver.close()



def get_table_rows():


def get_table_cloums():

def get_table_text():

def table_should_contain():

def table_element_click()




driver.find_element_by_xpath("fdsfdf").text'''





