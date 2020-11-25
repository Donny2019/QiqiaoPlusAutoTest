'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:56
@File    : department_radio.py
'''
from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class DepartmentRedio(UiDriver):
    '''基础组件-部门单选'''
    def search(self,file_name,search,full_name):
        '''
        使用部门单选字段筛选页面数据
        :param file_name: 字段名称
        :param search: 搜索值
        :param full_name: 部门全名
        :return:
        '''
        loc = Operation().readXml("departmentradio","search").format(name=file_name)
        self.sendKeys(loc,search)
        self.clickElement(Operation().readXml("departmentradio","departname").format(full_name))


    def normal(self,filed_name,department):
        '''
        非必填类型部门单选输入值
        :param filed_name:
        :param department:
        :return:
        '''
        loc = Operation().readXml('departmentradio','normal').format(name=filed_name)
        self.clickElement(loc)
        seach_loc = Operation().readXml('departmentradio','departmentsearch')
        self.sendKeys(seach_loc,department[0])
        self.clickElement(Operation().readXml('departmentradio','value').format(value=department))
        self.clickElement(Operation().readXml('departmentradio','confim').format(name=filed_name))


    def default(self,feild_name):
        '''
        获取默认值
        :param feild_name: 部门单选字段名称
        :return: 返回填写值
        '''
        value = self.getText(Operation().readXml("departmentradio","default").format(name=feild_name))
        return value

