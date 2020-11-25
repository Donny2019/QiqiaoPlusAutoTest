'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:57
@File    : multiple_departments.py
'''

import time
from tools.operation import Operation
from ui.base.ui_driver import UiDriver




class MultipleDepartments(UiDriver):
    '''基础组件-部门多选'''
    def normal(self,feild_name,*args):
        '''
        非必填部门多选输入值
        :param feild_name: 部门多选字段名称
        :param args: 输入部门
        :return:
        '''
        loc = Operation().readXml('multipledepartments','normal').format(name=feild_name)
        self.clickElement(loc)
        for name in args:
            self.clickElement(Operation().readXml('multipledepartments','departmentsearch'))
            self.sendKeys(Operation().readXml('multipledepartments','departmentsearch'),name)
            time.sleep(1)
            self.clickElement(Operation().readXml('multipledepartments','value').format(name=feild_name,value=name))

        self.clickElement(Operation().readXml('multipledepartments','confim').format(name=feild_name))


    def required(self,feild_name,*args):
        '''
        必填部门多选字段输入内容
        :param feild_name: 部门多选字段名称
        :param args: 填写的部门名称
        :return:
        '''
        loc = Operation().readXml('multipledepartments','required').format(name=feild_name)
        self.clickElement(loc)
        for name in args:
            self.sendKeys(Operation().readXml('multipledepartments','departmentsearch'),name)
            self.clickElement(Operation().readXml('multipledepartments','value').format(name=feild_name,value=name))
        self.clickElement(Operation().readXml('multipledepartments','confim').format(name=feild_name))