'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:03
@File    : subform.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class Subform(UiDriver):
    '''关联组件-子表单'''
    def addOneLineData(self,sub_name):
        '''
        根据子表单名称，点击对应子表单添加一行按钮
        :param sub_name: 子表单名称
        :return:
        '''
        loc = Operation().readXml('subform','addoneline').format(name=sub_name)
        self.clickElement(loc)


    def addBtn(self,sub_name):
        '''
        根据子表单名称，点击对应子表单的添加按钮
        :param sub_name: 子表单名称
        :return:
        '''
        loc = Operation().readXml('subform','addbtn').format(name=sub_name)
        self.clickElement(loc)

    def editBtn(self,sub_name,index):
        '''
        根据子表单名称，点击对应子表单数据的编辑按钮
        :param sub_name: 子表单名称
        :param index: 第几条子表数据
        :return:
        '''
        index = int(index)-1
        self.moveToElement(Operation().readXml('subform','drop').format(sub=sub_name,num=index))
        self.clickElement(Operation().readXml('subform','editbtn').format(sub=sub_name,num=index))


    def deleteBtn(self,sub_name,index):
        '''
        根据子表单名称，点击对应子表单数据的删除按钮
        :param sub_name: 子表单名称
        :param index: 第几条数据
        :return:
        '''
        index = int(index) -1
        self.moveToElement(Operation().readXml('subform', 'drop').format(sub=sub_name, num=index))
        self.clickElement(Operation().readXml('subform', 'deletebtn').format(sub=sub_name, num=index))

