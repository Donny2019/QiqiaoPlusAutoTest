'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:02
@File    : foreign_key_selection.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver



class ForergnKeySelection(UiDriver):
    '''关联组件-外键选择'''

    def normal(self,fild_name,value):
        '''
        非必填类型输入内容
        :param fild_name: 字段名字
        :param value: 写入值
        :return:
        '''
        loc = Operation().readXml('foreignkeyselection','normal').format(name=fild_name)
        self.clickElement(loc)
        loc1 = Operation().readXml('foreignkeyselection','input').format(name=fild_name)
        self.sendKeys(loc1,value)
        loc2 = Operation().readXml('foreignkeyselection','option').format(option=value)
        self.clickElement(loc2)


    def required(self,fild_name,value):
        '''
        必填类型外键选择输入内容
        :param fild_name: 字段名
        :param value: 输入值
        :return:
        '''
        loc = Operation().readXml('foreignkeyselection','required').format(name=fild_name)
        self.clickElement(loc)
        loc1 = Operation().readXml('foreignkeyselection','input').format(name=fild_name)
        self.sendKeys(loc1,value)
        loc2 = Operation().readXml('foreignkeyselection','option').format(option=value)
        self.clickElement(loc2)


