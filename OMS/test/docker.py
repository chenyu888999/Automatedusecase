

#coding=utf-8
from selenium import webdriver
import time,threading,nose




def test(host,firefox_capabilities,text):
    browser = webdriver.Remote(command_executor=host, desired_capabilities=firefox_capabilities)
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(text)
    browser.find_element_by_id("su").click()
    time.sleep(2)
    a = browser.title
    print(a)
    # browser.get_screenshot_as_file("D:/baidu.png")
    browser.close()

if __name__ == "__main__":
    a = {
        "firefox": "http://119.29.148.186:8081/wd/hub",

        "chrome": "http://119.29.148.186:8081/wd/hub"
    }
    threads = []
    for webbrowser, host in a.items():
        print(webbrowser,host)
        firefox_capabilities = {
            "seleniumProtocol": "WebDriver",
            "browserName": webbrowser,
            "maxInstances": 1,
            "applicationName": "",
            "platform": "LINUX",
        }


        # 构建线程
        oms = threading.Thread(target=test, args=(host,firefox_capabilities,"python"))
        threads.append(oms)
        print(threads)

        # 启动所有线程
    for thr in threads:
        thr.start()
        time.sleep(10)

