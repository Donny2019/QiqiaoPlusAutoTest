'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:28
@File    : test_single_line_text.py
'''
import time
import unittest
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig


class TestSingleLineText(unittest.TestCase):
    '''测试单行文本'''
    def setUp(self) -> None:
        url = WebConfig().singlelinetext()
        self.driver = qiqiao.Login().loginRuntime(url)


    def tearDown(self) -> None:
        self.driver.quit()


    def test_required(self):
        '''测试单行文本必填'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        error_msg = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(error_msg,"不能为空")



    def test_onlyone(self):
        '''测试单行文本唯一校验'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).required("必填_唯一","测试")
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,"[必填_唯一]值必须唯一")


    def test_length_limit(self):
        '''测试单行文本长度限制'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).required("必填_唯一", "测试")
        qiqiao.SingleLineText(self.driver).normal("字符2到10","道")
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','requiredmsg'))
        self.assertEqual(msg,"字符长度必须在2和10之间")

    def test_english_length_limit(self):
        '''测试单行文本输入英文并限制长度'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).required("必填_唯一", "测试")
        qiqiao.SingleLineText(self.driver).normal("英文5到10","Donn")
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','requiredmsg'))
        self.assertEqual(msg, "字符长度必须在5和10之间")



    def test_input_number_or_english(self):
        '''测试单行文本输入英文或数字'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).required("必填_唯一", "测试")
        qiqiao.SingleLineText(self.driver).normal("数字或英文2到10", "道一")
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','requiredmsg'))
        self.assertEqual(msg, "请输入数字或英文")



    def test_default_value(self):
        '''测试单行文本默认值'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        default = qiqiao.Application(self.driver).getAttribute(Operation().readXml("singlelinetext","normal").format(name="默认"),"title")
        self.assertEqual(default,"道一七巧测试")


    def test_data_linkage(self):
        '''测试单行文本数据联动'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).required("必填_唯一", "道一")
        time.sleep(1)
        link_value = qiqiao.SingleLineText(self.driver).getLinkedValue("数据联动")
        self.assertEqual(link_value, "18")