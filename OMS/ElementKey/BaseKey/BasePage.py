#-*- coding: utf-8 -*-
'''
@Time    : 2017/9/1 13:10
@Author  : 陈宇
@File    : BasePage.py
@Software: PyCharm
@Describe: 
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os, sys, time,unittest,datetime,random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import win32com, win32gui, win32con, time
from OMS.ElementKey.BaseKey.Log import Logger
import logging
import configparser
from OMS.Config.Element_list import _const
Log = Logger("Auto").getlog()

class BasePage(object):

    def __init__(self, selenium_driver, base_url,base_title):
        self.driver = selenium_driver
        self.base_url = base_url
        self.base_title = base_title


    def on_title(self,pagetitle):
        return pagetitle in  self.driver.title


    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()


    def open(self,url,pagetitle):
        try:
            self._open(url)
            Log.info("打开网页成功%s" % url)
            assert self.on_title(pagetitle), "打开页面失败%s" % url
        except:
            Log.error("打开网页失败%s" % url)



    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            Log.info("%s 页面中成功找到 %s 元素" % (self, loc))
            return self.driver.find_element(*loc)
        except:
            Log.error("%s页面未能找到%s元素"% (self,loc))


    def script(self,js):
        try:
            self.driver.execute_script(js)
            Log.info("%s页面执行js:%s成功" % (self,js))
        except:
            Log.error("%s页面执行js:%s失败" % (self,js))

    def switch_frame(self,*loc):
        Log.info("%s切换frame:%s成功" % (self, loc))
        return self.driver.switch_to.frame(self.find_element(*loc))


    def right_click(self, *element):
        try:
            ActionChains(self.driver).context_click(self.find_element(*element)).perform()
            Log.info("%s右击成功%s元素"%(self,element))
        except:
            Log.error("%s右击未成功%s元素" % (self, element))
    def move_to_element(self, *element):
        try:
            ActionChains(self.driver).move_to_element(self.find_element(*element)).perform()
            Log.info("%s移动成功%s元素" % (self, element))
        except:
            Log.error("%s移动未成功%s元素" % (self, element))

    def double_click(self, *element):
        try:
            ActionChains(self.driver).double_click(self.find_element(*element)).perform()
            Log.info("%s双击成功%s元素" % (self, element))
        except:
            Log.error("%s双击未成功%s元素" % (self, element))


    def drag_and_drop(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element),self.find_element(target_element)).perform()


    def back(self):
        try:
            self.driver.back()
            Log.info("返回成功")
        except:
            Log.error("返回失败")

    def forward(self):
        self.driver.forward()

    def get_attribute(self, *element, attribute):
        try:
            return self.find_element(*element).get_attribute(attribute)

        except:
            Log.error("%s获取属性值未成功%s元素" % (self, element))

    def get_text(self, *element):
        try:
            return self.find_element(*element).text
        except:
            Log.error("%s获取文本值未成功%s元素" % (self, element))

    def get_display(self, *element):
        try:
            return self.find_element(*element).is_displayed()
        except:
            Log.error("%s页面显示成功%s元素" % (self, element))

    def get_title(self):
        try:
            return self.driver.title
        except:
            Log.error("title获取失败" )

    def get_url(self):
        return self.driver.current_url

    def get_screenshot(self):
        try:
            screen = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            self.driver.get_screenshot_as_file(screen + "\\screenpicture\\/%s.png" % datetime.datetime.now().strftime("%Y%m%d.%H%M%S"))
            Log.info("截图成功，以保存到：%s"% screen+"\\screenpicture")
        except:
            Log.error("截图失败")


    def switch_to_frame(self, *element):
        self.driver.switch_to_frame(self.find_element(*element))

    def switch_to_frame_out(self):
        self.driver.switch_to.default_content()

    def open_new_window(self, *element):
        try:
            current_windows = self.driver.current_window_handle
            self.find_element(*element).click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != current_windows:
                    self.driver.switch_to.window(handle)
            Log.info("%s以跳转到新窗口：%s" % (self,element))
        except:
            Log.error("%未跳转到新窗口：%s" % (self, element))

    def F5(self):
        try:
            self.driver.refresh()
            Log.info("刷新页面成功")
        except:
            Log.error("刷新页面失败")



    def accept_alert(self):
        try:
            self.driver.switch_to.alert.accept()
            Log.info("异常接受成功")
            #self.driver.switch_to_alert().accept()
            return self.driver.switch_to_alert().text
        except:
            Log.error("异常接受失败")


    def dismiss_alert(self):
        try:
            self.driver.switch_to.alert.dismiss()
            Log.info("异常取消成功")
        except:
            Log.error("异常取消失败")

    def close(self):
        try:
            self.driver.close()
            Log.info("浏览器关闭")
        except:
            Log.info("浏览器关闭失败")


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

    def select(self,*locate,select):
        '''选择方式的选择
        Usage:select(locate,value or index or text)
        '''

        if "=" not in select:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = select.split("=")[0]
        value = select.split("=")[1]
        try:
            if by == "value":
                return Select(self.find_element(*locate)).select_by_value(value)
            elif by == "index":
                return Select(self.find_element(*locate)).select_by_index(value)
            elif by == "text":
                return Select(self.find_element(*locate)).select_by_visible_text(value)
        except:
            Log.error("%s选择失败%s"%(self,locate))




    def fol_number(self,digit):
        number = str(round((random.uniform(0.001, 5.999)),digit))
        return number

    def is_visible(self,locator, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False


    def update(self,title,path):
        try:
            time.sleep(1)
            dialog = win32gui.FindWindow('#32770', title)  # 对话框
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
            Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
            button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
            win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, path)
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
            Log.info("上传文件成功")
        except:
            Log.error("上传文件失败")

    def get_table_rows(self,*element):
        '''
        获取表格总行数
        '''
        return (self.driver.find_element(*element).find_elements_by_tag_name('tr'))

    def get_table_cloumn(self,*element,index):
        '''
               获取表格总列数
        '''
        return (self.get_table_rows(*element)[index].find_elements_by_tag_name('td'))

    def get_table_text(self,rowindex,colindex,*element):
        '''
               获取表格单元格text
        '''
        return (self.get_table_rows(*element)[rowindex].find_elements_by_tag_name('td')[colindex].text)

    def get_table_text_row(self,colindex,text,*element):
        '''
               获取文本所在行
        '''
        for index,i in enumerate(self.get_table_rows(*element)):
            if i.find_elements_by_tag_name('td')[colindex].text == text:
                return index
        else:
            print("未找到%s" % text)

    def click_table_element(self,textrow,colindex,locate,*element,**kwargs):
        '''
               点击表格中单元格以及单元格中文本链接
               *args,**kwargs不传为点击单元格，传参后即点击超链接
        '''
        try:
            self.get_table_rows(*element)[textrow].find_elements_by_tag_name('td')[colindex].find_element_by_id(locate).click()
            Log.info("点击元素成功")

        except:
            Log.info("点击元素失败")


    def click_table_link(self,textrow,colindex,linktext,*element):
        try:
            self.get_table_rows(*element)[textrow].find_elements_by_tag_name('td')[colindex].find_element_by_link_text(linktext).click()
            Log.info("点击文本值为%s" % linktext + "的链接成功")
        except:
            Log.error("未找到文本值为%s" % linktext + "的元素")



    def get_table_text_col_time(self,time,*element):
        '''

        获取时间文本所在列
        '''
        a = self.driver.find_element(*element).find_elements_by_tag_name('tr')
        print(a)
        for index,i in enumerate(a):
            g = self.driver.find_element(*element).find_elements_by_tag_name('tr')[index].find_elements_by_tag_name('td')
            for index,i in enumerate(g):
                if i.text == time:
                    return index


    def get_table_text_row_time(self,time,*element):
        '''
               获取时间文本所在行
        '''
        a = self.driver.find_element(*element).find_elements_by_tag_name('tr')
        for index,i in enumerate(a):
            g = self.driver.find_element(*element).find_elements_by_tag_name('tr')[index].find_elements_by_tag_name('td')
            for i in g:
                if i.text == time:
                    return index
        else:
            print("未找到%s" % time)


    def read_conf(self,key,value):
        self.conf = configparser.ConfigParser()
        self.conf.read(_const.config_path)
        return self.conf.get(key, value)

    def write_conf(self,key,value,text):
        self.conf = configparser.ConfigParser()
        self.conf.read(_const.config_path)
        self.conf.set(key, value, text)
        self.conf.write(open(_const.config_path, "w"))

    def wait_element(self,seconds=5,*element):
        """
        Waiting for an element to display.

        Usage:
        driver.wait_element("id=kw",10)
        """
        try:
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located(*element))

        except:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")


