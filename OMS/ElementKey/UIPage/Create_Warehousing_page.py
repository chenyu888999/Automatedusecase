#-*- coding: utf-8 -*-
'''
@Time    : 2017/9/2 15:03
@Author  : 陈宇
@File    : Create_Warehousing_page.py
@Software: PyCharm
@Describe: 
'''


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from OMS.ElementKey.UIPage import LoginPage
import time,unittest,datetime


class Create_ware_page(LoginPage.LoginPage):
    js = "leftMenu('54','创建入库单','/receiving/receiving/create?quick=54')"
    time.sleep(3)
    frame = (By.ID,"iframe-container-54")
    Transshipment_button = (By.XPATH,".//*[@id='asnForm']/table/tbody/tr[1]/td[2]/div/div[2]")
    Destination_warehouse = (By.ID,"transit_warehouse") #中转仓
    Transit_warehouse = (By.ID,"new_target_warehouse_code")   #目的仓
    total= (By.NAME,"volume")
    weight = (By.NAME,"weight")
    Head_delivery_mode = (By.ID,"sm_code")  #头程派送方式
    Freight_transportation_mode = (By.XPATH, "(//select[@id='receiving_shipping_type'])[2]") #货运方式
    Reference_number = (By.XPATH, "(//input[@id='refrence_no'])[2]") #参考编号
    delivery_mode = (By.XPATH, "(//input[@name='shipping_method'])[2]")#派送方式
    Tracking_number = (By.XPATH, "(//input[@name='tracking_no'])[2]")#跟踪号
    Tariff_type = (By.NAME, "tax_type") #关税类型
    Customs_declaration_type = (By.NAME, "customer_type")#报关类型
    No = (By.ID, "imBoxNo")#箱号
    SKU= (By.ID, "imCodeSearch")
    Number= (By.ID, "imQuantity")
    Add = (By.ID, "addItem")
    Commit = (By.ID,"asnSubmitBtn")
    RV = (By.ID,"create_feedback_div")
    RV_time = (By.XPATH,".//*[@id='ui-datepicker-div']/table/tbody")
    Estimated_time = (By.XPATH,".//*[@id='asnForm']/table/tbody/tr[12]/td[2]/input")
    aa =(By.XPATH,".//*[@id='ui-datepicker-div']/div/a[2]/span") #上一月
    bb = (By.XPATH, ".//*[@id='ui-datepicker-div']/div/a[1]/span") #下一月
    #审核
    js_man = "leftMenu('45','入库单管理','/receiving/receiving/index?quick=45')"
    frame_man = (By.ID, "iframe-container-45")
    table = (By.XPATH,".//*[@id='receivedForm']/table")
    #check_box =(By.ID,"asnCodes[]")
    examine = (By.CSS_SELECTOR,".asnVerifyBtn.baseBtn.opBtn")
    Determine = (By.XPATH,"html/body/div[5]/div[3]/div/button[1]")
    RV_info = (By.ID,"dialog-auto-alert-tip")





    def __init__(self,selenium_driver,base_url,base_title):
        super(Create_ware_page, self).__init__(selenium_driver,base_url,base_title)

    def open_create_ware_page(self):
        self.script(self.js)

    def switch_create_frame(self):
        self.switch_frame(*self.frame)

    def click_Transshipment_button(self):
        self.find_element(*self.Transshipment_button).click()

    def select_Destination_warehouse(self,value):
        return Select(self.find_element(*self.Destination_warehouse)).select_by_value(value)

    def select_Transit_warehouse(self,value):
        return Select(self.find_element(*self.Transit_warehouse)).select_by_value(value)

    def input_Delivery_commodity_attribute(self,m,kg):
        self.find_element(*self.total).send_keys(m)
        self.find_element(*self.weight).send_keys(kg)


    def select_Head_delivery_mode(self,value):
        return Select(self.find_element(*self.Head_delivery_mode)).select_by_value(value)

    def select_Freight_transportation_mode(self,ooo):
        return Select(self.find_element(*self.Freight_transportation_mode)).select_by_value(ooo)

    def input_Reference_number(self,text):
        self.find_element(*self.Reference_number).send_keys(text)

    def input_delivery_mode(self,text):
        self.find_element(*self.delivery_mode).send_keys(text)

    def input_Tracking_number(self,text):
        self.find_element(*self.Tracking_number).send_keys(text)

    def select_Tariff_type(self,value):
        return Select(self.find_element(*self.Tariff_type)).select_by_value(value)

    def select_Customs_declaration_type(self,value):
        return Select(self.find_element(*self.Customs_declaration_type)).select_by_value(value)

    def input_Inbound_commodity_information(self,*args):
        self.find_element(*self.No).send_keys(args[0])
        self.find_element(*self.SKU).send_keys(args[1])
        self.find_element(*self.Number).send_keys(args[2])


    def click_add_button(self):
        self.find_element(*self.Add).click()

    def commit(self):
        self.find_element(*self.Commit).click()

    def up_get_screen(self,):
        js = "document.documentElement.scrollTop = 100000"
        self.script(js)
        time.sleep(2)
        self.get_screenshot()
    def get_rv(self, *element):
        RV_T = []
        text = self.get_text(*self.RV)
        A = str(text).split(":")
        RV_T.append(A)
        return RV_T

    def click_time(self):
        #self.find_element(*self.Estimated_time).click()
        row = self.get_table_text_row_time("6",*self.RV_time)
        col = self.get_table_text_col_time("6",*self.RV_time)
        self.click_table_link(row,col,"6",*self.RV_time)

    def time_handle(self,input,*element):
        self.find_element(*self.Estimated_time).click()
        user_date = datetime.datetime.strptime(input, '%Y-%m-%d')
        locate_time = datetime.datetime.now()
        delta = user_date.month - locate_time.month
        if user_date.month > locate_time.month:
            delta = user_date.month - locate_time.month
            for i in range(delta):
                self.driver.find_element(*self.aa).click()
                if i == delta:
                    break
        elif user_date.month < locate_time.month:
            delta = locate_time.month - user_date.month
            for i in range(delta):
                self.driver.find_element(*self.bb).click()
                if i == delta:
                    break
        else:
            print("点击错误")





    def open_was_manage(self):
        self.script(self.js_man)

    def switch_man_frame(self):
        self.switch_frame(*self.frame_man)


    def Submit_audit(self):
        time.sleep(2)
        self.click_table_element(2,0,"asnCodes[]",*self.table)
        self.find_element(*self.examine).click()
        self.find_element(*self.Determine).click()
        #self.wait_element(*self.RV_info, 7)
        number = str(self.get_text(*self.RV_info))
        return number
























