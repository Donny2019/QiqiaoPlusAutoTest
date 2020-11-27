'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:27
@File    : test_number.py
'''
import time
import unittest
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig


class TestNumber(unittest.TestCase):
    '''测试数字组件'''

    def setUp(self) -> None:
        url = WebConfig().number()
        self.driver = qiqiao.Login().loginRuntime(url)

    def tearDown(self) -> None:
        self.driver.quit()



    def test_required(self):
        '''测试数字组件必填'''

        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Number(self.driver).normal("整数100到200",120)
        time.sleep(0.5)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg, "不能为空")

    def test_onlyone(self):
        '''测试数字组件唯一'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Number(self.driver).required("必填唯一",100)
        qiqiao.Number(self.driver).normal("整数100到200", 120)
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText("xpath=>//p[@class='el-message__content']")
        self.assertEqual(msg,"[必填唯一]值必须唯一")


    def test_limit_size(self):
        '''测试数字组件限制范围'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Number(self.driver).required("必填唯一", 100)
        qiqiao.Number(self.driver).normal("整数100到200",20)
        time.sleep(0.5)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg, "整数100到200的值必须在100和200之间")


    def test_default_value(self):
        '''测试数字组件默认值'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        default = qiqiao.Application(self.driver).getAttribute(Operation().readXml("number","normal").format(name="默认100"),"title")
        self.assertEqual(default,"100")

    def test_data_linkage(self):
        '''测试数字组件数据联动'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Number(self.driver).required("必填唯一", 20)
        time.sleep(1)
        link_value = qiqiao.Application(self.driver).getAttribute(Operation().readXml("number", "linked").format(name="数据联动"),
                                                          "title")
        self.assertEqual(link_value, "18.00")
