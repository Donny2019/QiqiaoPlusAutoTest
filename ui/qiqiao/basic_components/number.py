'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:58
@File    : number.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver


class Number(UiDriver):
    '''基础组件-数字'''
    def normal(self,fild_name,value):
        '''
        非必填数据输入值
        :param fild_name: 数字字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("number","normal").format(name=fild_name)
        self.sendKeys(loc,value)


    def required(self,fild_name,value):
        '''
        必填数据输入值
        :param fild_name: 数字字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("number","required").format(name=fild_name)
        self.sendKeys(loc,value)

    def search(self,filed_name,value):
        '''
        使用数字字段筛选页面数据
        :param filed_name: 数字字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("number","search").format(name=filed_name)
        self.sendKeys(loc,value)


    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''
        子表单的数字输入数据
        :param sub_form: 子表单名称
        :param filed_name: 数字字段名称
        :param value: 填写值
        :return:
        '''
        loc =  Operation().readXml("number","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)