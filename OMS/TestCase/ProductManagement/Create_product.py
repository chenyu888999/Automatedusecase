# coding:utf-8

'''
author:陈宇
产品申请、提交审核、审核操作

date:2017-7-1
'''

import unittest
from selenium.webdriver.common.keys import Keys
from OMS.Config.Element_list import _const
from OMS.Keyword.Element import Oms
import datetime,time
import win32com,win32gui,win32con
import configparser


class Create_Product(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Oms("firefox")                                                                                     #初始化环境以及登陆操作
        cls.driver.max_window()
        cls.driver.get("http://192.168.10.223:61604/")
        cls.driver.send_keys("id=userName",_const.name)
        cls.driver.send_keys("id=userPass",_const.password)
        cls.driver.click("css=.loginbtn.radius5")
        cls.sku = cls.driver.RandomNumber(10)
        cls.check_sku = cls.sku.upper()                                                                                 #将sku转大写，便于断言
        cls.proname = cls.driver.RandomNumber(8)
        cls.verification = []
        cls.verification.append(cls.driver.get_text("id=user_info_sys"))                                                #查看登陆是否成功读取登陆用户
        cls.conf = configparser.ConfigParser()
        cls.conf.read(_const.config_path)                                                                               #读取配置文件

    @classmethod
    def tearDownClass(cls):
        sk = str(cls.verification[1])
        sk = str(sk.split(":")[1].split(" ")[0])
        cls.conf.set("OddNumbers","Warehouse_receipt_no",sk)
        cls.conf.write(open(_const.config_path, "w"))                                                                   #sku写入配置文件
        cls.driver.quit()

    #创建产品
    def test_01_create(self):
        self.driver.click("css=.sidebar-header")
        self.driver.js("leftMenu('55','创建商品','/product/product/create?quick=55')")
        self.driver.switch_to_frame("id=iframe-container-55")


        # ---------------------------品类选择----------------------------
        self.driver.click("css=.chosen-single>div>b")
        self.driver.send_keys("css=.chosen-search>input", "Home")
        self.driver.send_keys("css=.chosen-search>input", Keys.ENTER)
        self.driver.clickxpath(".//*[@id='c_level_1_chosen']/a/div/b")
        self.driver.sendkeys_xpath(".//*[@id='c_level_1_chosen']/div/div/input", "Bedding")
        self.driver.sendkeys_xpath(".//*[@id='c_level_1_chosen']/div/div/input", Keys.ENTER)
        self.driver.clickxpath(".//*[@id='c_level_2_chosen']/a/div/b")
        self.driver.sendkeys_xpath(".//*[@id='c_level_2_chosen']/a/div/b", "Bed Skirts")
        self.driver.sendkeys_xpath(".//*[@id='c_level_2_chosen']/a/div/b", Keys.ENTER)
        #---------------------------货品信息------------------------------
        self.driver.send_keys("id=product_title","name"+ self.proname)                                                  #产品名称
        self.driver.send_keys("id=product_sku","sku"+ self.sku)                                                         #SKU
        self.driver.send_keys("id=reference_no","number"+ self.driver.RandomNumber(8))                                  #参考编号
        self.driver.send_keys("id=product_declared_value","50")                                                         #申报价值
        self.driver.send_keys("id=product_declared_name_zh", "测试产品"+ self.driver.RandomNumber(5))                     #中文申报名
        self.driver.send_keys("id=product_declared_name", "test product" + self.driver.RandomNumber(5))                 #海关品名
        self.driver.send_keys("id=hs_code",self.driver.RandomNumber(5))                                                 #海关编码
        self.driver.select("name=product_package_type","value=package")                                                 #货物类型
        #---------------------------规格信息------------------------------
        self.driver.send_keys("id=product_weight", self.driver.fol_number(3))
        self.driver.send_keys("id=product_length",self.driver.fol_number(3))
        self.driver.send_keys("id=product_width",self.driver.fol_number(2))
        self.driver.send_keys("id=product_height", self.driver.fol_number(2))

        #---------------------------产品图片--------------------------------
        #driver.clickxpath(".//*[@id='SWFUpload_0']")
        '''
        time.sleep(5)
        dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, '')  
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) '''

        #---------------------------提交产品--------------------------------
        self.driver.click("id=productSubmitBtn")
        self.driver.wait_element("id=create_feedback_div",5)
        self.driver.wait(2)
        self.verification.append(self.driver.get_text("id=create_feedback_div"))
        self.driver.js("document.documentElement.scrollTop=1000")
        time.sleep(2)
        self.driver.get_screenshot()
        self.driver.switch_to_frame_out()

    #提交审核操作
    def test_02_commite_audit(self):
        #--------------------------------------提交审核---------------------------------------
        self.driver.click("css=.sidebar-header")
        self.driver.js("leftMenu('46','商品维护','/product/product/list?quick=46')")
        self.driver.switch_to_frame("id=iframe-container-46")
        self.driver.is_visible("css=.indexTag2.statusTag.chooseTag",2)
        self.driver.click("text=草稿")
        self.driver.wait(1)
        self.driver.click("id=product_title_like")
        self.driver.send_key("id=product_title_like","name"+ self.proname)
        self.driver.click("css=.baseBtn.submitToSearch")
        self.driver.click("css=.checkAll")
        #self.driver.is_visible("css=.asnSubmitAuditBtn.baseBtn.opBtn",5)
        self.driver.click("css=.asnSubmitAuditBtn.baseBtn.opBtn")
        self.driver.click("id=popup_ok")
        self.driver.wait_element("css=#dialog-auto-alert-tip > p:nth-child(2)",6)
        self.verification.append(self.driver.get_text("css=#dialog-auto-alert-tip > p:nth-child(2)"))
        self.driver.clickxpath("(//button[@type='button'])[13]")
        try:
            table = self.driver.find_element("css=#table-module-list-data")
            table_rows = len(table.find_elements_by_tag_name('tr'))
            print(table_rows)
            if table_rows == 1:
                print("产品名称为:name%s" % self.proname + "提交审核成功")
            else:
                print("产品名称为:name%s" % self.proname + "提交审核未成功")
        except:
            return False

    #海外仓审核操作
    def test_03_audit(self):
        # -----------------------------------审核产品---------------------------------------------
        self.driver.get("http://192.168.10.223:61605/")
        self.driver.send_keys("id=userName","emswms")
        self.driver.send_keys("id=userPass", "td123456")
        self.driver.click("id=login")
        #self.driver.click(u"text=产品管理")
        self.driver.js("leftMenu('235','产品审核','product/product/audit-list?quick=235')")
        self.driver.switch_to_frame("id=iframe-container-235")
        self.driver.wait_element("name=skuType",2)
        self.driver.select("name=skuType", "value=2")
        self.driver.send_keys("id=E2", self.sku)
        self.driver.click("css=.baseBtn.submitToSearch")
        #table = self.driver.find_element("css=#table-module-list-data")
        #table_rows = len(table.find_elements_by_tag_name('tr'))
        self.driver.click("text=审核")
        time.sleep(2)
        self.driver.clickxpath(".//*[@id='productAuditDataForm']/table/tbody/tr[1]/td[2]/label[1]/input")
        self.driver.clickxpath("html/body/div[4]/div[3]/div/button[1]")
        self.driver.wait_element("id=dialog-auto-alert-tip",3)
        self.verification.append(self.driver.get_text("id=dialog-auto-alert-tip"))
        self.driver.clickxpath("/html/body/div[5]/div[3]/div/button/span")
        print(self.verification)

    def test_04_check_product(self):
        print(self.check_sku)
        self.assertEqual("Welcome,\nbaker(000028)",self.verification[0])  # 对登陆页面数据进行断言
        self.assertEqual("SKU:sku%s 创建成功" % self.sku, self.verification[1])  # 创建成功
        self.assertEqual("SKU:SKU%s 审核成功" % self.check_sku ,self.verification[2])  #审核成功
        self.assertEqual("Success", self.verification[3])



if __name__ == '__main__':
    #unittest.main
    suite = unittest.TestSuite()
    suite.addTest(Create_Product("test_01_create"))
    suite.addTest(Create_Product("test_02_commite_audit"))
    suite.addTest(Create_Product("test_03_audit"))
    suite.addTest(Create_Product("test_04_check_product"))
    #suite.addTest(Create_Product("back"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
