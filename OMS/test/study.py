#-*- coding: utf-8 -*-
'''
@Time    : 2017/7/13 11:11
@Author  : 陈宇
@File    : test.py
@Software: PyCharm
@Describe: 
'''
import configparser
from OMS.Keyword.Element import Oms
#from OMS.Config.Element_list import uuu





'''conf = configparser.ConfigParser()
conf.read("F:\Automated use case\OMS\Config\Variable_Config.conf")

name = conf.get("section1", "name")
print(name)
name1 = conf.get("OddNumbers", "Warehouse_receipt_no")

print(name1)

conf.set("OddNumbers","Warehouse_receipt_no", "gfdgdfg")
conf.set("section1","name","ttrtrtrt")
conf.write(open("F:\Automated use case\OMS\Config\Variable_Config.conf","w"))
name = conf.get("section1", "name")
print(name)

a = "SKU:sku9bl8uh13ca 创建成功"
b = str(a.split(":")[1].split(" ")[0])
print(b)


def _init():
    global _global_dict
    _global_dict = {}


def set_value(key,value):
    _global_dict[key] = value'''


data = open("F:\\Automated use case\\OMS\\test\\test1","r+",encoding='utf-8')

user = data.read()
#print(user)

user_info = user.split("$")

print(user_info)

aa = {}
for i in user_info:
    bb = i.split(":")
    print(bb)
    print(bb[-1])
    aa[bb[0]]= bb[-1]

print(aa)





