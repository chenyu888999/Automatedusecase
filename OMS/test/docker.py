

#coding=utf-8
from selenium import webdriver
import time

'''firefox_capabilities ={
"seleniumProtocol":"WebDriver",
"browserName":"chrome",
"maxInstances":1,
"version":"59.0.3071.115",
"applicationName":"",
"platform":"LINUX",
}
'''
firefox_capabilities ={
"seleniumProtocol":"Selenium",
"browserName":"firefox",
"maxInstances":1,
"platform":"LINUX",
}


browser=webdriver.Remote("http://119.29.148.186:4444/wd/hub",desired_capabilities=firefox_capabilities)
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("python")
browser.find_element_by_id("su").click()
time.sleep(2)
a = browser.title
print(a)
#browser.get_screenshot_as_file("D:/baidu.png")
browser.close()


{
"seleniumProtocol":"Selenium",
"browserName":"firefox",
"maxInstances":1,
"platform":"LINUX",
}