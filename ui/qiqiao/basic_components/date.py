'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:56
@File    : date.py
'''
from tools.operation import Operation
from ui.base.ui_driver import UiDriver


class Date(UiDriver):
    '''基础组件-日期'''
    def normal(self,field_name,value):
        '''
        非必填类型输入日期
        :param fild_name:字段名称
        :param value:输入日期值 eg:2019-12-20
        :return:
        '''
        loc = Operation().readXml("date","normal").format(name=field_name)
        self.sendKeys(loc,value)
        self.clickElement(Operation().readXml("date","normallabel").format(name=field_name))

    def required(self,field_name,value):
        '''
        必填类型输入日期
        :param field_name: 字段名称
        :param value: 输入日期值 eg:2019-12-20
        :return:
        '''
        loc = Operation().readXml("date","required").format(name=field_name)
        self.sendKeys(loc,value)
        self.clickElement(Operation().readXml("date","label").format(name=field_name))
    def delete(self,field_name):
        '''
        删除日期字段已填写的值
        :param field_name: 字段名称
        :return:
        '''
        loc=Operation().readXml("date","comment").format(name=field_name)
        self.moveToElement(loc)
        self.clickElement(Operation().readXml('date','delete').format(name=field_name))
    def search(self,field_name,start,end):
        '''
        使用日期字段筛选页面数据
        :param field_name: 字段名称
        :param start: 开始时间
        :param end: 结束时间
        :return:
        '''
        start_loc = Operation().readXml("date","startTime").format(name=field_name)
        self.sendKeys(start_loc,start)
        end_loc = Operation().readXml("date","endTime").format(name=field_name)
        self.sendKeys(end_loc,end)
        self.clickElement(Operation().readXml("date","packup").format(name=field_name))

    def getDefaultValue(self,field_name):
        '''
        获取日期组件的默认值
        :param field_name: 字段名称
        :return:
        '''
        self.clickElement(Operation().readXml('date','default').format(name=field_name))
        year = self.getText(Operation().readXml('date','year'))[0:4]
        month = str(self.getText(Operation().readXml('date','month'))).split(" ")[0]
        day = self.getText(Operation().readXml('date','day'))
        if int(month)>=10 and int(day)>=10:
            value = year+"-"+month+"-"+day
            return value
        elif int(month)<10 and int(day)<10:
            value = year + "-" + "0" + month + "-" + "0" + day
            return value
        elif int(month)<10 and int(day)>=10:
            value = year + "-" + "0" + month + "-"+ day
            return value
        elif int(month)>=10 and int(day)<10:
            value = year + "-" + month + "-"+ "0" +day
            return value


    def sendValueInSubForm(self,sub_form,field_name,value):
        '''
        子表单日期输入数据
        :param sub_form: 子表单名称
        :param field_name: 日期字段名称
        :param value: 输入值
        :return:
        '''
        loc =  Operation().readXml("date","subForm").format(form=sub_form,feild=field_name)
        self.sendKeys(loc,value)