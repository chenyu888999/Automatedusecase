

#coding=utf-8
from selenium import webdriver
import time,threading,nose,sys
from OMS.ElementKey.BaseKey.Element import Oms

firefox_capabilities = {
            "seleniumProtocol": "WebDriver",
            "browserName": "firefox",
            "maxInstances": 1,
            "applicationName": "",
            "platform": "LINUX",
        }
firefox_capabilities1 = {
            "seleniumProtocol": "WebDriver",
            "browserName": "chrome",
            "maxInstances": 1,
            "applicationName": "",
            "platform": "LINUX",
        }


def test():
    browser = webdriver.Remote(command_executor="http://119.29.148.186:8081/wd/hub", desired_capabilities=firefox_capabilities)
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_keys("python")
    browser.find_element_by_id("su").click()
    time.sleep(2)
    a = browser.title
    print(a)
    # browser.get_screenshot_as_file("D:/baidu.png")
    browser.close()

def test2():
    browser = webdriver.Remote(command_executor="http://119.29.148.186:8081/wd/hub", desired_capabilities=firefox_capabilities1)
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_keys("测试基础")
    browser.find_element_by_id("su").click()
    time.sleep(2)
    a = browser.title
    print(a)
    # browser.get_screenshot_as_file("D:/baidu.png")
    browser.close()

def test3():
    driver = Oms("firefox")
    driver.get("http://192.168.10.223:61601/")
    driver.max_window()
    driver.find_element("id=userName").send_keys("gcwms")
    driver.find_element("id=userPass").send_keys("td123456")
    driver.find_element("id=login").click()
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
    time.sleep(2)
    d = driver.get_table_text_row(".//*[@id='receivedForm']/table", 4, "G591")

    print(d)

    driver.click_table_element(".//*[@id='receivedForm']/table", d, 4, "G591d")
    time.sleep(2)
    driver.close()


def test4():
    driver = Oms("firefox")
    driver.get("http://192.168.10.223:61601/")
    driver.max_window()
    driver.find_element("id=userName").send_keys("gcwms")
    driver.find_element("id=userPass").send_keys("td123456")
    driver.find_element("id=login").click()
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
    time.sleep(2)
    d = driver.get_table_text_row(".//*[@id='receivedForm']/table", 4, "G591")

    print(d)

    driver.click_table_element(".//*[@id='receivedForm']/table", d, 4, "G591")
    time.sleep(2)
    driver.close()


if __name__ == "__main__":
    threads = []
    oms = threading.Thread(target=test, args=())
    oms1 = threading.Thread(target=test2, args=())
    oms2 = threading.Thread(target=test3, args=())
    oms3 = threading.Thread(target=test4, args=())
    threads.append(oms)
    threads.append(oms1)
    threads.append(oms2)
    threads.append(oms3)
    print(threads)
    time.sleep(10)


    for thr in threads:
        thr.start()
    sys.exit()