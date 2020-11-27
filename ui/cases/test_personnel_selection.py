'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:27
@File    : test_personnel_selection.py
'''

import time
import unittest
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig

class TestPersonnelSelection(unittest.TestCase):
    '''测试人员单选'''
    def setUp(self) -> None:
        url = WebConfig().personnelselection()
        self.driver = qiqiao.Login().loginRuntime(url)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_required(self):
        '''测试人员单选必填'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','requiredmsg'))
        self.assertEqual("不能为空", msg)


    def test_limit_tab(self):
        '''测试限制人员范围为标签'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml("personnelselection","normal").format(name="标签为测试"))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn("王栋一",html)
        self.assertNotIn("孙超",html)

    def test_limit_user_department(self):
        '''测试限制人员范围为用户所属部门'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml("personnelselection","normal").format(name="用户所属部门"))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn("王栋一",html)
        self.assertIn("卢益清",html)
        self.assertNotIn("孙超",html)

    def test_limit_department(self):
        '''测试限制人员范围为部门'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml("personnelselection","normal").format(name="限制部门"))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn("朱浪锋",html)
        self.assertIn("欧小春",html)
        self.assertNotIn("卢益清",html)
        self.assertNotIn("孙超",html)

    def test_limit_customize(self):
        '''测试限制人员范围为自定义'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml("personnelselection","normal").format(name="自定义"))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn("刁惠云",html)
        self.assertIn("罗琳月",html)

    def test_default_user(self):
        '''测试默认值为当前用户'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        value = qiqiao.PersonnelSelection(self.driver).default("当前用户")
        self.assertEqual("王栋一",value)

    def test_default_customize(self):
        '''测试默认值为用户自定义'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        value = qiqiao.PersonnelSelection(self.driver).default("用户自定义")
        self.assertEqual("刁惠云",value)