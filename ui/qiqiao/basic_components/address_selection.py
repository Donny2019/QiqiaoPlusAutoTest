'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:55
@File    : address_selection.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver

class AddressSelection(UiDriver):
    '''基础组件-地址选择器'''
    def search(self,field_name,province,city,region):
        '''
        列表筛选字段地址组件输入内容
        :param field_name: 字段名称
        :param province: 省份
        :param city: 城市
        :param region: 地区
        :return:
        '''
        loc = Operation().readXml("addressselection","search").format(name=field_name)
        self.clickElement(loc)
        province_loc = Operation().readXml("addressselection","province").format(field_name,province)
        city_loc = Operation().readXml("addressselection","city").format(field_name,city)
        region_loc = Operation().readXml("addressselection","region").format(field_name,region)
        self.clickElement(province_loc)
        self.clickElement(city_loc)
        self.clickElement(region_loc)

    def normal(self,field_name,province,city,region):
        '''
        地址选择器非必填输入值
        :param field_name:字段名称
        :param province: 省份
        :param city: 城市
        :param region: 地区
        :return:
        '''
        loc = Operation().readXml("addressselection","normal").format(name=field_name)
        self.clickElement(loc)
        province_loc = Operation().readXml("addressselection","province").format(field_name,province)
        city_loc = Operation().readXml("addressselection","city").format(field_name,city)
        region_loc = Operation().readXml("addressselection","region").format(field_name,region)
        self.clickElement(province_loc)
        self.clickElement(city_loc)
        self.clickElement(region_loc)

    def required(self,field_name,province,city,region):
        '''
        地址选择器必填输入值
        :param field_name: 字段名称
        :param province: 省份
        :param city: 城市
        :param region: 地区
        :return:
        '''
        loc = Operation().readXml("addressselection","required").format(name=field_name)
        self.clickElement(loc)
        province_loc = Operation().readXml("addressselection","province").format(field_name,province)
        city_loc = Operation().readXml("addressselection","city").format(field_name,city)
        region_loc = Operation().readXml("addressselection","region").format(field_name,region)
        self.clickElement(province_loc)
        self.clickElement(city_loc)
        self.clickElement(region_loc)