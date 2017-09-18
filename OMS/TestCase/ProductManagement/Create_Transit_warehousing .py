#-*- coding: utf-8 -*-
'''
@Time    : 2017/9/2 15:13
@Author  : 陈宇
@File    : casecreate.py
@Software: PyCharm
@Describe: 中转创建中转入库单、审核订单
'''

from selenium import webdriver
#from OMS.ElementKey.BaseKey.BasePage import BasePage
from OMS.ElementKey.UIPage.Create_Warehousing_page import Create_ware_page
from OMS.Config.Element_list import _const
import time,unittest,os
from flaky import flaky


file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class create_warehousing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "http://192.168.10.223:61604/"
        self.username = "baker"
        self.password = "Baker888999"
        self.title = "中邮海外仓 - cpws"



    @flaky(max_runs=3)
    def test01_create_oms(self):
        #初始化对象
        create_page = Create_ware_page(self.driver, self.url, self.title)
        #打开中邮oms
        create_page.open_url()
        #输入用户名和密码并提交
        create_page.input_username(self.username)
        create_page.input_password(self.password)
        create_page.click_submit()
        #打开创建入库单页面并跳转frame
        create_page.open_create_ware_page()
        create_page.switch_create_frame()
        #选择中转入库
        create_page.click_Transshipment_button()
        #选择头程仓库
        create_page.select_Destination_warehouse("CNTC")
        #选择目的仓库
        create_page.select_Transit_warehouse("USEA")
        #填写商品属性
        create_page.input_Delivery_commodity_attribute(10,10)
        #填写头程派送方式
        create_page.select_Head_delivery_mode("FEDEX-GROUND")
        #填写货运方式
        create_page.select_Freight_transportation_mode('0')
        #填写关税类型
        create_page.select_Tariff_type("P")
        #填写报关类型
        create_page.select_Customs_declaration_type("N")
        #填写参考编号、派送方式、跟踪号
        create_page.input_Reference_number(create_page.RandomNumber(8))
        create_page.input_delivery_mode(create_page.RandomNumber(8))
        create_page.input_Tracking_number(create_page.RandomNumber(8))
        #选择预计到达时间
        create_page.time_handle("2017-5-5")
        create_page.click_time()
        # 上传单证
        create_page.script("document.getElementById('fileField').click()")
        create_page.update("文件上传",file_path + "\Test_File\单证文件.xls")
        # 上传制造商资料
        create_page.script("document.getElementById('import_manufacture_datas').click()")
        create_page.update("文件上传", file_path+ "\Test_File\制造商文件.xls")
        # 上传报关文件
        create_page.script("document.getElementById('customs_document').click()")
        create_page.update("文件上传", file_path+ "\Test_File\报关图片.png")

        #填写入库商品信息
        create_page.input_Inbound_commodity_information(1,"SKU0GOXBDAQ3I",20)
        create_page.click_add_button()
        create_page.commit()
        #截图并获取入库单号并做校验
        create_page.up_get_screen()
        text = create_page.get_rv()
        self.assertEqual(text[0][0],"创建入库单成功")
        #写入入库单号
        create_page.write_conf("OddNumbers","Warehouse_receipt",text[0][1])

    def test02_Transfer_order(self):
        create_page = Create_ware_page(self.driver, self.url, self.title)
        create_page.open_url()
        # 输入用户名和密码并提交
        create_page.input_username(self.username)
        create_page.input_password(self.password)
        create_page.click_submit()
        create_page.open_was_manage()
        create_page.switch_man_frame()
        sucess_info = create_page.Submit_audit()
        rv = create_page.read_conf("OddNumbers", "Warehouse_receipt")
        print(type(sucess_info))
        print(type(rv))
        self.assertEqual(sucess_info, "入库单审核成功:%s" % rv)




    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    #suite = unittest.TestSuite()
    #suite.addTest(create_warehousing("test01_create_oms"))
    #suite.addTest(create_warehousing("test02_Transfer_order"))
    #runner = unittest.TextTestRunner()