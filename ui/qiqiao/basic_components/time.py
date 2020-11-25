'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:59
@File    : time.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class Time(UiDriver):
    '''基础组件-时间'''

    def normal(self,fild_name,value):
        '''时间输入值'''
        loc = Operation().readXml("time","normal").format(name=fild_name)
        self.sendKeys(loc,value)
        self.clickElement(Operation().readXml("time","label").format(name=fild_name))

    def required(self,fild_name,value):
        '''必填时间输入值'''
        loc = Operation().readXml("time","required").format(name=fild_name)
        self.sendKeys(loc,value)
        self.clickElement(Operation().readXml("time","label").format(name=fild_name))

    def search(self,filed_name,start_time,end_time):
        '''使用时间字段筛选页面数据'''
        start_loc = Operation().readXml("time","startTime").format(name=filed_name)
        self.clickElement(start_loc)
        self.clear(start_loc)
        self.sendKeys(start_loc,start_time)
        end_loc = Operation().readXml("time","endTime").format(name=filed_name)
        self.clickElement(end_loc)
        self.clear(end_loc)
        self.sendKeys(end_loc,end_time)
        self.clickElement(Operation().readXml("time","packup").format(name=filed_name))


    def sendValueToTimeInSubForm(self,sub_form,filed_name,value):
        '''子表单的时间输入数据'''
        loc =  Operation().readXml("time","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)