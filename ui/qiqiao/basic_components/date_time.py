'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:56
@File    : date_time.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class DateTime(UiDriver):
    '''基础组件-日期时间'''
    def normal(self,fild_name,value):
        '''
        非必填类型输入日期时间'
        :param fild_name: 字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("datetime","normal").format(name=fild_name)
        self.sendKeys(loc,value)
        self.clickElement(Operation().readXml("datetime","label").format(name=fild_name))

    def delete(self,fild_name):
        '''
        删除日期时间已填写的数据
        :param fild_name: 日期时间字段名称
        :return:
        '''
        loc = Operation().readXml("datetime", "comment").format(name=fild_name)
        self.moveToElement(loc)
        loc_del = Operation().readXml("datetime", "delete").format(name=fild_name)
        self.clickElement(loc_del)


    def required(self,fild_name,value):
        '''
        必填类型输入日期时间
        :param fild_name: 字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("datetime","required").format(name=fild_name)
        self.sendKeys(loc,value)
        self.clickElement(Operation().readXml("datetime","label").format(name=fild_name))

    def search(self,filed_name,value):
        '''
        日期时间字段筛选输入日期时间
        :param filed_name: 字段名称
        :param value: 填写值
        :return:
        '''
        loc = Operation().readXml("datetime","search").format(name=filed_name)
        self.sendKeys(loc,value)
        self.clickElement(Operation().readXml("datetime","packup").format(name=filed_name))

    def sendValueTimeInSubForm(self,sub_form,filed_name,value):
        '''
        子表单的日期时间输入数据
        :param sub_form: 子表单名称
        :param filed_name: 日期时间字段名称
        :param value: 填写数据
        :return:
        '''
        loc =  Operation().readXml("date_time","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)