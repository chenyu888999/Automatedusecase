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
import win32com, win32gui, win32con, time
from OMS.ElementKey.BaseKey.Log import Logger
import logging

Log = Logger("Auto").getlog()

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
        self.driver.get_screenshot_as_file("F:\\Automated_use_case\\OMS\\screenpicture\\/%s.png" % datetime.datetime.now().strftime("%Y%m%d.%H%M%S"))


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

    def update(self,title,path):
        dialog = win32gui.FindWindow('#32770', title)  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, path)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    def get_table_rows(self,element):
        '''
        获取表格总行数
        '''
        return (self.driver.find_element_by_xpath(element).find_elements_by_tag_name('tr'))
    def get_table_rows_th(self,element):
        '''
        获取表格总行数
        '''
        return (self.driver.find_element_by_xpath(element).find_elements_by_tag_name('th'))

    def get_table_cloumn(self,element,index):
        '''
               获取表格总列数
        '''
        return (self.get_table_rows(element)[index].find_elements_by_tag_name('td'))

    def get_table_text(self,element,rowindex,colindex):
        '''
               获取表格单元格text
        '''
        return (self.get_table_rows(element)[rowindex].find_elements_by_tag_name('td')[colindex].text)

    def get_table_text_row(self,element,colindex,text):
        '''
               获取文本所在行
        '''
        for index,i in enumerate(self.get_table_rows(element)):
            if i.find_elements_by_tag_name('td')[colindex].text == text:
                return index
        else:
            print("未找到%s" % text)

    def get_table_text_col(self,element,text):
        a = self.driver.find_element_by_xpath(element).find_elements_by_tag_name('tr')
        print(a)
        for index,i in enumerate(a):
            g = self.driver.find_element_by_xpath(element).find_elements_by_tag_name('tr')[index].find_elements_by_tag_name('td')
            for index,i in enumerate(g):
                if i.text == text:
                    return index

    def get_table_text_row1(self,element,text):
        '''
               获取时间文本所在行
        '''
        a = self.driver.find_element_by_xpath(element).find_elements_by_tag_name('tr')
        for index,i in enumerate(a):
            g = self.driver.find_element_by_xpath(element).find_elements_by_tag_name('tr')[index].find_elements_by_tag_name('td')
            for i in g:
                if i.text == text:
                    return index
        else:
            print("未找到%s" % text)



    def click_table_element(self,element,textrow,colindex,*args,**kwargs):
        '''
               点击表格中单元格以及单元格中文本链接
               *args,**kwargs不传为点击单元格，传参后即点击超链接
        '''
        try:
            if len(args) <= 0 :
                self.get_table_rows(element)[textrow].find_elements_by_tag_name('td')[colindex].click()
                Log.info("点击元素成功")
            else:
                self.get_table_rows(element)[textrow].find_elements_by_tag_name('td')[colindex].find_element_by_link_text(*args).click()
                Log.info("点击文本值为%s" % args + "的链接成功")
        except:
            pass
            Log.error("未找到文本值为%s" % args + "的元素")




    def click_table_element1(self,element,textrow,colindex,*args,**kwargs):
        '''
               点击表格中单元格以及单元格中文本链接
               *args,**kwargs不传为点击单元格，传参后即点击超链接
        '''
        try:
            if args == False:
                self.get_table_rows(element)[textrow].find_elements_by_tag_name('td')[colindex].click()
                Log.info("点击%s" % args + "的元素成功")

        except:
            self.get_table_rows(element)[textrow].find_elements_by_tag_name('td')[colindex].find_element_by_link_text(*args).click()
            Log.info("点击文本值为%s" % args + "的链接成功")




