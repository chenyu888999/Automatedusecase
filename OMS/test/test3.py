#-*- coding: utf-8 -*-
'''
@Time    : 2017/8/16 16:07
@Author  : 陈宇
@File    : ttt.py
@Software: PyCharm
@Describe: 
'''


from nose import with_setup


def setup_module(module):
    print('setup_module 函数执行于一切开始之前')

def setup_deco():
    print('setup_deco 将用于 with_setup')

def teardown_deco():
    print('teardown_deco 也将用于 with_setup')

@with_setup(setup_deco,teardown_deco)
def test_2b_decorated():
    print("ppppppppppppp")

class TestUM():
    def setup(self):
        print('setup 方法执行于本类中每条用例之前')

    @classmethod
    def setup_class(cls):
        print('setup_class 类方法执行于本类中任何用例开始之前,且仅执行一次')

    def test_strings(self):
        assert("aaaaaaaaaaaaaaaaaaaaa")