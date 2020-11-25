'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:57
@File    : multiple_persons.py
'''

import time
from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class MultiplePersonnel(UiDriver):
    '''基础组件-人员多选'''


    def search(self, filed_name,full_name):
        '''
        通过人员多选筛选页面数据
        :param filed_name: 字段名称
        :param full_name: 全名
        :return:
        '''
        loc = Operation().readXml("multiplepersonnelselection", "search").format(name=filed_name)
        name = full_name[0]
        self.sendKeys(loc, name)
        self.clickElement(Operation().readXml("multiplepersonnelselection", "personname").format(full_name))

    def normal(self, filed_name, *args):
        '''
        非必填人员多选输入值
        :param filed_name: 字段名称
        :param args: 填写人员全名，可填写多个值
        :return:
        '''
        loc = Operation().readXml("multiplepersonnelselection", "normal").format(name=filed_name)
        self.clickElement(loc)
        for fullname in args:
            name=fullname[0]
            self.clickElement(Operation().readXml("multiplepersonnelselection", "input").format(name="组织选择器搜索框"))
            self.sendKeys(Operation().readXml("multiplepersonnelselection", "input").format(name="组织选择器搜索框"), name)
            time.sleep(2)
            self.clickElement(Operation().readXml("multiplepersonnelselection", "fullname").format(name=filed_name,fullname=fullname))
        time.sleep(1)
        self.clickElement(Operation().readXml("multiplepersonnelselection", "conf_btn").format(name=filed_name))

    def required(self, filed_name, *args):
        '''
        必填人员多选输入值
        :param filed_name: 字段名称
        :param args: 填写值，可填写多个值
        :return:
        '''
        loc = Operation().readXml("multiplepersonnelselection", "required").format(name=filed_name)
        self.clickElement(loc)
        for fullname in args:
            name=fullname[0]
            self.clickElement(Operation().readXml("multiplepersonnelselection", "input").format(name="组织选择器搜索框"))
            self.sendKeys(Operation().readXml("multiplepersonnelselection", "input").format(name="组织选择器搜索框"), name)
            time.sleep(0.5)
            self.clickElement(Operation().readXml("multiplepersonnelselection", "fullname").format(name=filed_name,fullname=fullname))
        self.clickElement(Operation().readXml("multiplepersonnelselection", "conf_btn").format(name=filed_name))