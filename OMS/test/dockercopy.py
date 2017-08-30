

#coding=utf-8
from selenium import webdriver
import time,threading,nose

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

if __name__ == "__main__":
    threads = []
    # 构建线程
    oms = threading.Thread(target=test, args=())
    oms1 = threading.Thread(target=test2, args=())
    threads.append(oms)
    threads.append(oms1)
    print(threads)

    # 启动所有线程
for thr in threads:
    thr.start()