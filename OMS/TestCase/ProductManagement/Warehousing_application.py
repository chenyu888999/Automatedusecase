# coding:utf-8

'''
author:陈宇
填写入库单，入库签收，收货、上架

date:2017-7-5
'''

import unittest,time
from OMS.Keyword.Element import Oms
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
import configparser




class Warehousing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Oms("firefox")  # 初始化环境以及登陆操作
        cls.driver.max_window()
        cls.driver.get("http://192.168.10.223:61604/")
        cls.driver.send_keys("id=userName", "6000fish")
        cls.driver.send_keys("id=userPass", "Td123456")
        cls.driver.click("css=.loginbtn.radius5")
        cls.verification = []
        cls.OddNumbers = []
        #cls.verification.append(cls.driver.get_text("id=user_info_sys"))
        cls.conf = configparser.ConfigParser()
        cls.conf.read("F:\Automated use case\OMS\Config\Variable_Config.conf")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("浏览器退出成功")

     #填写入库申请
    def test_01_create_warehousing(self):
        #------------------------------------入库信息填写---------------------------------
        driver = self.driver
        driver.js("leftMenu('54','创建入库单','/receiving/receiving/create?quick=54')")
        driver.switch_to_frame("id=iframe-container-54")
        driver.wait(2)
        #driver.wait_element("id=target_warehouse_code",3)
        driver.select("id=receiving_shipping_type","value=0")
        driver.select("id=target_warehouse_code","value=USEA")
        driver.send_keys("id=refrence_no",self.driver.RandomNumber(5))
        driver.send_keys("name=shipping_method",self.driver.RandomNumber(5))
        driver.send_keys("name=tracking_no",self.driver.RandomNumber(5))
        #------------------------------------入库商品信息----------------------------------
        driver.send_keys("id=imBoxNo",1)
        driver.send_key("id=imCodeSearch",self.conf.get("OddNumbers", "warehouse_receipt_no"))
        driver.send_keys("id=imQuantity",3)
        driver.click("id=addItem")
        driver.click("id=asnSubmitBtn")
        driver.wait_element("id=create_feedback_div",3)
        create_back = str(driver.get_text("id=create_feedback_div")).split(":")
        driver.switch_to_frame_out()
        driver.js("leftMenu('45','入库单管理','/receiving/receiving/index?quick=45')")
        driver.wait_element("id=iframe-container-45",2)
        driver.switch_to_frame("id=iframe-container-45")
        driver.wait(2)
        driver.click("name=common_code")
        driver.wait_element("id=table-module-list-data",5)
        driver.is_visible("name=common_code",5)
        driver.send_key("name=common_code",create_back[1])
        driver.clickxpath(".//*[@id='search-module-baseSearch']/div/input")

        #入库单审核通过
    def test_02_examine_warehousing(self):
        #-------------------------------入库申请单审核--------------------------------------
        driver = self.driver
        #driver.clickxpath(".//*[@id='fix_header_content']/div/div[1]/ul/li[1]/a")
        driver.clickxpath(".//*[@id='fix_header_content']/div/div[1]/ul/li[2]/a")
        driver.clickxpath(".//*[@id='no_sign_tbody']/td[1]/input")
        driver.clickxpath(".//*[@id='fix_header_content']/div/div[2]/div/input[2]")
        driver.wait_element("id=ui-id-2")
        self.verification.append(driver.get_text("id=ui-id-2"))
        driver.clickxpath("html/body/div[5]/div[3]/div/button[1]")
        driver.wait_element("id=dialog-auto-alert-tip",7)
        time.sleep(2)
        #aa = str(driver.get_text("id=dialog-auto-alert-tip")).split(":")
        number = str(driver.get_text("id=dialog-auto-alert-tip")).split(":")
        number = str(number[1])
        self.OddNumbers.append(number)
        print(self.OddNumbers[0])

        #通过入库单号查找进行签收操作
    def test_03_Sign(self):
        #--------------------------------海外仓入库签收---------------------------------------
        driver=self.driver
        driver.get("http://192.168.10.223:61605/")
        driver.send_keys("id=userName", "emswms")
        driver.send_keys("id=userPass", "td123456")
        driver.click("id=login")
        driver.wait_element("id=main-right-container-iframe",3)
        driver.js("leftMenu('250','签收','/receiving/sign/list?quick=250')")    #打开签收窗口
        driver.switch_to_frame("id=iframe-container-250")
        driver.send_keys("id=receiving_code",self.OddNumbers[0])
        driver.click("css=.baseBtn.submitToSearch")
        driver.click("css=.checkAll")
        driver.click("id=operate-sign-button")
        #driver.wait_element("id=ui-id-1",3)
        driver.click("css=html body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable.ui-resizable div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix div.ui-dialog-buttonset button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-focus")
        time.sleep(2)
        self.verification.append(driver.get_text("id=mask_layer_div"))
        print(self.verification[1])
        driver.switch_to_frame_out()

    #签收管理查看状态
    def test_04_Sign_management(self):
        driver = self.driver
        driver.js("leftMenu('251','签收管理','/receiving/sign-management/list?quick=251')")
        driver.switch_to_frame("id=iframe-container-251")
        driver.wait_element("id=receiving_code",3)
        driver.send_key("id=receiving_code",self.OddNumbers[0])
        driver.clickxpath(".//*[@id='search-module-baseSearch']/div/input")
        self.verification.append(driver.get_xpath(".//*[@id='table-module-list-data']/tr[1]/td[4]"))                    #签收状态
        self.verification.append(driver.get_xpath(".//*[@id='table-module-list-data']/tr[1]/td[7]"))                    #签收批次
        driver.switch_to_frame_out()




    #通过入库单号查询进行收货
    def test_05_Receiving(self):
        driver = self.driver
        driver.js("leftMenu('25','收货','/receiving/transfer/received?quick=25')")    #进入收货选项卡
        driver.switch_to_frame("name=iframe-container-25")
        driver.send_key("id=operationCode",self.OddNumbers[0])                #输入入库单号
        driver.click("id=toSearch")
        driver.clickxpath(".//*[@class='table-module']/tbody/tr/td/input")
        driver.click("id=overseasReceived")
        driver.clickxpath("html/body/div[7]/div[3]/div/button[1]")
        driver.wait_element("id=dialog-auto-alert-tip",3)
        self.verification.append(driver.get_text("id=dialog-auto-alert-tip"))
        driver.switch_to_frame_out()

    #收货管理
    def test_06_Receiving_management(self):
        driver = self.driver
        driver.js("leftMenu('22','收货管理','/receiving/receiving/list?quick=22')")  # 进入收货选项卡
        driver.switch_to_frame("name=iframe-container-22")
        driver.send_key("id=E1", self.OddNumbers[0])  # 输入入库单号
        driver.clickxpath(".//*[@id='search-module-baseSearch']/div/input")
        self.verification.append(driver.get_xpath(".//*[@id='table-module-list-data']/tr[1]/td[7]"))   #收货状态
        driver.switch_to_frame_out()

        #上架操作
    def test_07_Putaway(self):
        driver = self.driver
        driver.js("leftMenu('27','上架','/receiving/putaway-detail/putaway?quick=27')")
        driver.switch_to_frame("id=iframe-container-27")
        driver.send_key("id=operationCode", self.OddNumbers[0])  # 输入入库单号
        driver.click("id=toSearch")
        driver.click("text=选择货架")
        driver.js("selLocation('001-001-600')")
        self.verification.append(driver.get_attribute("css=.putawayLcCode.input_text",'value'))
        driver.clickxpath(".//*[@id='putawayForm']/table/tbody[1]/tr/td[1]/input")
        driver.click("id=submit-putaway")
        time.sleep(1)
        self.verification.append(driver.get_text("id=dialog-auto-alert-tip"))
        driver.switch_to_frame_out()

    def test_08_Putaway_management(self):
        driver = self.driver
        driver.js("leftMenu('23','上架管理','/receiving/Putaway-detail/list?quick=23')")
        driver.switch_to_frame("id=iframe-container-23")
        driver.send_key("id=E4", self.OddNumbers[0])  # 输入入库单号
        driver.clickxpath(".//*[@id='search-module-baseSearch']/div[2]/input")
        self.verification.append(driver.get_xpath(".//*[@id='table-module-list-data']/tr[1]/td[10]"))  # 上架状态
        self.verification.append(driver.get_xpath(".//*[@id='table-module-list-data']/tr/td[4]"))      #库位
        driver.switch_to_frame_out()
        print(self.verification)




    def test_09_check(self):
        self.assertEqual("审核",self.verification[0])
        self.assertEqual("操作成功", self.verification[1])
        self.assertEqual("签收完成", self.verification[2])
        self.assertEqual("签收完成", self.verification[3])
        self.assertEqual("操作成功", self.verification[4])
        self.assertEqual("状态：收货完成\n同步状态：未同步\n货运方式：空运", self.verification[5])
        self.assertEqual(self.verification[6], self.verification[9])
        self.assertEqual("操作成功", self.verification[7])
        self.assertEqual("已完成", self.verification[8])

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Warehousing("test_01_create_warehousing"))
    suite.addTest(Warehousing("test_02_examine_warehousing"))
    suite.addTest(Warehousing("test_03_Sign"))
    suite.addTest(Warehousing("test_04_Sign_management"))
    suite.addTest(Warehousing("test_05_Receiving"))
    suite.addTest(Warehousing("test_06_Receiving_management"))
    suite.addTest(Warehousing("test_07_Putaway"))
    suite.addTest(Warehousing("test_08_Putaway_management"))
    suite.addTest(Warehousing("test_09_check"))
    runner = unittest.TextTestRunner()

