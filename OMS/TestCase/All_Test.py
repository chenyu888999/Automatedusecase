#-*- coding: utf-8 -*-
'''
@Time    : 2017/7/13 18:25
@Author  : 陈宇
@File    : All_Test.py
@Software: PyCharm
@Describe: 
'''

from OMS.TestCase.ProductManagement.Create_product import Create_Product
from OMS.TestCase.ProductManagement.Warehousing_application import Warehousing
import unittest, doctest,HTMLTestRunner


suite = doctest.DocTestSuite()
#罗列要执行的文件
suite.addTest(unittest.makeSuite(Create_Product))
suite.addTest(unittest.makeSuite(Warehousing))
#unittest.TextTestRunner(verbosity=2).run(suite)


filename = 'F:\\Automated use case\\OMS\\Report\\result.html'
fp = open(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Report_title',
    description='Report_description')
runner.run(suite)