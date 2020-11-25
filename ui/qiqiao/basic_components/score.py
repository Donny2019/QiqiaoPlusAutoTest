'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:59
@File    : score.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver
import time

class Score(UiDriver):
    '''基础组件-评分'''
    def search(self,filed_name,value):
        '''使用评分字段筛选页面数据'''
        loc = Operation().readXml("score","search").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        self.clickElement(Operation().readXml("score","scorenumber").format(name=value))
        self.clickElement(Operation().readXml("score","packup").format(name=filed_name))


    def normal(self,feild_name,value):
        '''
        非必填评分组件输入值
        :param feild_name: 评分组件字段名称
        :param value: 填写的值
        :return:
        '''
        loc = Operation().readXml('score','normal').format(name=feild_name,score=value)
        self.clickElement(loc)


    def required(self,feild_name,value):
        '''
        必填评分组件输入值
        :param feild_name: 评分组件字段名称
        :param value: 填写的值
        :return:
        '''
        loc = Operation().readXml('score','required').format(name=feild_name,score=value)
        self.clickElement(loc)