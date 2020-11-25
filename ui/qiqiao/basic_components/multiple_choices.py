'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:57
@File    : multiple_choices.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver
import time

class MultipleChoices(UiDriver):
    '''基础组件-多项选择'''

    def checkedNormal(self, fild_name, *args):
        '''
        非下拉多项选择输入值
        :param fild_name: 字段名称
        :param args: 选项值 eg:checkedNormal('多项选择','中国','美国')
        :return:
        '''
        ''''''
        for i in args:
            loc = Operation().readXml("multiplechoices", "checkednormal").format(name=fild_name, index=i)
            self.clickElement(loc)

    def checkedRequired(self, fild_name, *args):
        '''
        非下拉多项选择输入值必填
        :param fild_name: 字段名称
        :param args: 选项值
        :return:
        '''
        for i in args:
            loc = Operation().readXml("multiplechoices", "checkedrequired").format(name=fild_name, index=i)
            self.clickElement(loc)

    def dropDownNormal(self, fild_name, *args):
        '''
        下拉类型多项选择输入值
        :param fild_name: 字段名称
        :param args: 选项值
        :return:
        '''
        loc = Operation().readXml("multiplechoices", "dropdownnormal").format(name=fild_name)
        self.clickElement(loc)
        time.sleep(0.5)
        for value in args:
            self.clickElement(Operation().readXml("multiplechoices", "selectorname").format(feildname=fild_name,name=value))
        self.clickElement(Operation().readXml("multiplechoices", "packupselector").format(name=fild_name))

    def dropDownRequired(self, fild_name, *args):
        '''
        必填下拉类型多项选择输入值
        :param fild_name: 字段名称
        :param args: 选项值
        :return:
        '''
        loc = Operation().readXml("multiplechoices", "drowndownrequired").format(name=fild_name)
        self.clickElement(loc)
        time.sleep(0.5)
        for value in args:
            self.clickElement(Operation().readXml("multiplechoices", "selectorname").format(feildname=fild_name,name=value))
        self.clickElement(Operation().readXml("multiplechoices", "requiredpackupselector").format(name=fild_name))

    def search(self, filed_name, value):
        '''
        使用多项选择字段筛选页面数据
        :param filed_name: 字段名称
        :param value: 搜索值
        :return:
        '''
        loc = Operation().readXml("multiplechoices", "search").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement(Operation().readXml("multiplechoices", "seachvalue").format(name=value))
        self.clickElement(Operation().readXml("multiplechoices", "packup").format(name=filed_name))
        self.clickElement("xpath=>//button[@data-mark='筛选条件搜索按钮']")

    def sendValueInSubForm(self, sub_form, filed_name, value):
        '''
        子表单的多项选择输入数据
        :param sub_form: 子表单名称
        :param filed_name: 字段名称
        :param value: 输入值
        :return:
        '''
        loc = Operation().readXml("multiplechoices", "subForm").format(form=sub_form, feild=filed_name)
        self.sendKeys(loc, value)

