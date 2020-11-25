'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:00
@File    : tab.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class Tab(UiDriver):
    '''布局组件-选项卡'''
    def clickTab(self,tab_name):
        '''点击选项卡'''
        loc = Operation().readXml('tab','element').format(tab_name=tab_name)
        self.clickElement(loc)
