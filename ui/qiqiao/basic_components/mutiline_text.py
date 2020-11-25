'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:58
@File    : mutiline_text.py
'''
from tools.operation import Operation
from ui.base.ui_driver import UiDriver



class MultilineText(UiDriver):
    '''基础组件-多行文本'''

    def normal(self, fild_name, value):
        '''
        非必填多行文本输入内容
        :param fild_name: 字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("multipletext", "normal").format(name=fild_name)
        self.clear(loc)
        self.sendKeys(loc, value)

    def required(self, fild_name, value):
        '''
        必填多行文本输入内容
        :param fild_name: 字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("multipletext", "required").format(name=fild_name)
        self.clear(loc)
        self.sendKeys(loc, value)

    def search(self, filed_name, value):
        '''
        使用多行文本字段筛选页面数据
        :param filed_name: 字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("multipletext", "search").format(name=filed_name)
        self.clear(loc)
        self.sendKeys(loc, value)

    def sendValueInSubForm(self, sub_form, filed_name, value):
        '''
        子表单的多行文本输入数据
        :param sub_form: 子表单名称
        :param filed_name: 字段名称
        :param value: 填写值
        :return:
        '''

        loc = Operation().readXml("multipletext", "subForm").format(subname=sub_form, fieldname=filed_name)
        self.sendKeys(loc,value)
