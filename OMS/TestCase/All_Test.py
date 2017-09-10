#-*- coding: utf-8 -*-
'''
@Time    : 2017/7/13 18:25
@Author  : 陈宇
@File    : All_Test.py
@Software: PyCharm
@Describe: 
'''
import unittest,HTMLTestRunner,os,sys,doctest
case_path = os.path.dirname(os.path.abspath(__file__))
case_path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sys.path.append(case_path)

from OMS.TestCase import ProductManagement as package


#suite = doctest.DocTestSuite()
#罗列要执行的文件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(package.Create_product.Create_Product))
suite.addTest(unittest.makeSuite(package.Warehousing_application.Warehousing))
#unittest.TextTestRunner(verbosity=2).run(suite)


filename = case_path1 + "\\Report\\result.html"




fp = open(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Report_title',
    description='Report_description')
runner.run(suite)