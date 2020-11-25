'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:58
@File    : personnel_selection.py
'''

import time
from tools.operation import Operation
from ui.base.ui_driver import UiDriver


class PersonnelSelection(UiDriver):
    '''基础组件-人员单选'''

    def search(self,filed_name,full_name):
        '''
        通过人员单选筛选页面数据
        :param filed_name: 人员选择字段名称
        :param full_name: 填写人员全名
        :return:
        '''
        name = full_name[0]
        loc = Operation().readXml("personnelselection","search").format(name=filed_name)
        self.sendKeys(loc,name)
        self.clickElement(Operation().readXml("personnelselection","personname").format(full_name))

    def normal(self,filed_name,full_name):
        '''
        人员单选非必填
        :param filed_name: 人员选择字段名称
        :param full_name: 填写人员全名
        :return:
        '''
        loc = Operation().readXml("personnelselection","normal").format(name=filed_name)
        self.clickElement(loc)
        name=full_name[0]
        self.sendKeys(Operation().readXml("personnelselection","input").format(name="组织选择器搜索框"),name)
        time.sleep(1)
        self.clickElement(Operation().readXml("personnelselection", "fullname").format(name=filed_name, fullname=full_name))
        self.clickElement(Operation().readXml("personnelselection","conf_btn").format(name=filed_name))

    def required(self,filed_name,full_name):
        '''
        人员单选必填
        :param filed_name: 人员选择字段名称
        :param full_name: 填写人员全名
        :return:
        '''
        loc = Operation().readXml("personnelselection","required").format(name=filed_name)
        self.clickElement(loc)
        name=full_name[0]
        self.sendKeys(Operation().readXml("personnelselection","input").format(name="组织选择器搜索框"),name)
        time.sleep(1)
        self.clickElement(Operation().readXml("personnelselection", "fullname").format(name=filed_name, fullname=full_name))
        self.clickElement(Operation().readXml("personnelselection","conf_btn").format(name=filed_name))


    def default(self,field_name):
        '''
        获取人员单选默认值
        :param field_name: 字段名称
        :return: 字段默认值
        '''
        loc = Operation().readXml("personnelselection","default").format(name=field_name)
        value = self.getText(loc)
        return value