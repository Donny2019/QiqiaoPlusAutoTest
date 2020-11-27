'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:27
@File    : test_multiline_text.py
'''
import unittest
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig
import  time,unittest


class TestMultilineText(unittest.TestCase):
    '''测试多行文本'''
    def setUp(self) -> None:
        url = WebConfig().multilinetext()
        self.driver = qiqiao.Login().loginRuntime(url)


    def tearDown(self) -> None:
        self.driver.quit()

    def test_required(self):
        '''测试多行文本必填'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(0.5)
        qiqiao.Application(self.driver).clickSubmit()
        msg  = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg,"不能为空")


    def test_length_limit(self):
        '''测试多行文本长度限制'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.MultilineText(self.driver).required("必填_提示","必填")
        qiqiao.MultilineText(self.driver).normal("长度10到15","测试长度限制")
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg,"字符长度必须在10和15之间")



    def test_default(self):
        '''测试多行文本默认值'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        msg  = qiqiao.Application(self.driver).getAttribute(Operation().readXml("multipletext","normal").format(name="默认值"),"title")
        self.assertEqual(msg,"道一云七巧测试")


    def test_data_linkage(self):
        '''测试多行文本数据联动'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.MultilineText(self.driver).required("必填_提示","多行文本")
        time.sleep(1)
        link_value = qiqiao.Application(self.driver).getAttribute(Operation().readXml("multipletext", "linked").format(name="数据联动"),
                                                          "title")
        self.assertEqual(link_value, "18")