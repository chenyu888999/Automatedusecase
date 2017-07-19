# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os, sys, time,unittest,datetime,random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui


class Oms(object):
    """
        Webdriver Two time package

    """

    def __init__(self, browser='firefox'):
        if browser == "firefox" :
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "ie" :
            driver = webdriver.Ie()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'.")

    def get(self, url):
        """
        Open url,same as get.

        Usage:
        driver.get("https://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, secsonds):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secsonds)

    def find_element(self,element):
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split("=")[0]
        value = element.split("=")[1]

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def wait_element(self, element, seconds=5):
        """
        Waiting for an element to display.

        Usage:
        driver.wait_element("id=kw",10)
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split("=")[0]
        value = element.split("=")[1]

        if by == "id":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "text":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def send_keys(self, element, text):
        self.wait_element(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(text)

    def click(self, element):
        self.wait_element(element)
        self.find_element(element).click()

    '''def Releaseclick(self,element):
        ActionChains(self.driver).release(self.find_element(element)).perform()'''

    def right_click(self, element):
        self.wait_element(element)
        ActionChains(self.driver).context_click(self.find_element(element)).perform()

    def move_to_element(self, element):
        #self.wait_element(element)
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    def double_click(self, element):
        self.wait_element(element)
        ActionChains(self.driver).double_click(self.find_element(element)).perform()

    def drag_and_drop(self, source_element, target_element):
        self.wait_element(source_element)
        self.wait_element(target_element)
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element), self.find_element(target_element)).perform()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def get_attribute(self, element, attribute):
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_screenshot(self):
        self.driver.get_screenshot_as_file("F:\\Automated use case\\OMS\\screenpicture\\/%s.png" % datetime.datetime.now().strftime("%Y%m%d.%H%M%S"))


    def submit(self, element):
        self.wait_element(element)
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        self.wait_element(element)
        self.driver.switch_to_frame(self.find_element(element))

    def switch_to_frame_out(self):
        self.driver.switch_to.default_content()

    def open_new_window(self, element):
        current_windows = self.driver.current_window_handle
        self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)
    def F5(self):
        self.driver.refresh()

    def js(self, script):
        self.driver.execute_script(script)

    def accept_alert(self):
        #self.driver.switch_to.alert.accept()
        self.driver.switch_to_alert().accept()
        return self.driver.switch_to_alert().text


    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def RandomNumber(self,number):
        code_list = []
        for i in range(10):
            code_list.append(str(i))
        for i in range(97, 123):
            code_list.append(chr(i))
        baker = random.sample(code_list, number)
        base_code = "".join((baker))
        return base_code

    def select(self,locate,select):
        '''选择方式的选择
        Usage:select(locate,value or index or text)
        '''

        if "=" not in select:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = select.split("=")[0]
        value = select.split("=")[1]

        if by == "value":
           return Select(self.find_element(locate)).select_by_value(value)
        elif by == "index":
           return Select(self.find_element(locate)).select_by_index(value)
        elif by == "text":
           return Select(self.find_element(locate)).select_by_visible_text(value)

    def clickxpath(self,locate):
        self.driver.find_element_by_xpath(locate).click()

    def sendkeys_xpath(self,locate,value):
        self.driver.find_element_by_xpath(locate).send_keys(value)

    def fol_number(self,digit):
        number = str(round((random.uniform(0.001, 5.999)),digit))
        return number

    def is_visible(self,locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def send_key(self, element, text):
        return self.find_element(element).send_keys(text)

    def get_xpath(self,element):
        return self.driver.find_element_by_xpath(element).text




