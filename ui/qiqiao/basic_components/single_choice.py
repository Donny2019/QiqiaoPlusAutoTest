'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:59
@File    : single_choice.py
'''
import time
from tools.operation import Operation
from ui.base.ui_driver import UiDriver




class SingleChoice(UiDriver):
    '''基础组件-单项选择'''
    def chekedNormal(self,fild_name,num):
        '''勾选类型非必填'''
        loc = Operation().readXml("singlechoice","chekednormal").format(name=fild_name,index=num)
        self.clickElement(loc)

    def chekedRequired(self,fild_name,num):
        '''勾选类型必填'''
        loc = Operation().readXml("singlechoice","chekedrequired").format(name=fild_name,index=num)
        self.clickElement(loc)

    def dropDownNormal(self, filed_name,value):
        '''下拉类型非必填输入值'''
        loc = Operation().readXml("singlechoice","dropdown").format(name=filed_name)
        self.clickElement(loc)
        self.clickElement(Operation().readXml("singlechoice","dropvalue").format(feildname=filed_name,name=value))

    def dropDownRequired(self, filed_name,value):
        '''下拉类型必填输入值'''
        loc = Operation().readXml("singlechoice","dropdown").format(name=filed_name)
        self.clickElement(loc)
        self.clickElement(Operation().readXml("singlechoice","dropvalue").format(feildname=filed_name,name=value))

    def search(self,filed_name,value):
        '''使用单项选择字段筛选页面数据'''
        loc = Operation().readXml("singlechoice","search").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement(Operation().readXml("singlechoice","value").format(name=value))
        self.clickElement(Operation().readXml("singlechoice","packup").format(name=filed_name))

    def sendValueInSubForm(self,sub_form,filed_name,value):
        '''子表单的单项选择输入数据'''
        loc =  Operation().readXml("singlechoice","subForm").format(form=sub_form,feild=filed_name)
        self.sendKeys(loc,value)