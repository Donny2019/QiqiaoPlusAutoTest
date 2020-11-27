'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:27
@File    : test_multiple_choices.py
'''

import time
from ui import qiqiao
from tools.read_config import WebConfig
import unittest



class TestMultipleChoices(unittest.TestCase):
    '''测试多项选择'''
    @classmethod
    def setUp(self) -> None:
        url = WebConfig().multiplechoice()
        self.driver = qiqiao.Login().loginRuntime(url)


    def tearDown(self) -> None:
        self.driver.quit()

    def test_required(self):
        '''测试多项选择必填'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.MultipleChoices(self.driver).checkedNormal("数量2到4", 1, 2, 3, 4,)
        qiqiao.Application(self.driver).clickSubmit()
        error_msg = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(error_msg,'不能为空')


    def test_limit_quantity(self):
        '''测试多项选择限制数量'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.MultipleChoices(self.driver).checkedRequired("必填_提示",1)
        qiqiao.MultipleChoices(self.driver).checkedNormal("数量2到4",1,2,3,4,5)
        error_msg = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(error_msg,'选择的数量必须在2和4之间')

    def test_linke_option(self):
        '''测试多项选择关联选项'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.MultipleChoices(self.driver).checkedRequired("必填_提示",1)
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn("关联现实", html)
        self.assertIn("关联未来", html)
        self.assertIn("关联现在", html)