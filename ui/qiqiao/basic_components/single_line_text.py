'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:59
@File    : single_line_text.py
'''
from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class SingleLineText(UiDriver):
    '''基础组件-单行文本'''
    def normal(self,fild_name,value):
        '''非必填类型单行文本输入内容'''
        loc = Operation().readXml("singlelinetext","normal").format(name=fild_name)
        self.sendKeys(loc,value)

    def required(self,fild_name,value):
        '''必填类型单行文本输入内容'''
        loc = Operation().readXml("singlelinetext","required").format(name=fild_name)
        self.sendKeys(loc,value)

    def search(self,filed_name,value):
        '''单行文本筛选数据输入内容'''
        loc = Operation().readXml("singlelinetext","search").format(name=filed_name)
        self.sendKeys(loc,value)

    def getLinkedValue(self,filed_name):
        '''获取联动值'''
        loc = Operation().readXml('singlelinetext','linked').format(name=filed_name)
        value = self.getAttribute(loc,'title')
        return value