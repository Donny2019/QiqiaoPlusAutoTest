'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:26
@File    : test_department_radio.py
'''
import time
import unittest
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig


class TestDepartmentRadio(unittest.TestCase):
    '''测试部门单选'''
    def setUp(self) -> None:
        url = WebConfig().departmentradio()
        self.driver = qiqiao.Login().loginRuntime(url)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_required(self):
        '''测试部门单选必填'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg', 'requiredmsg'))
        self.assertEqual("不能为空", msg)

    def test_limit_user(self):
        '''测试限制范围用户所属部门'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml("departmentradio","normal").format(name="用户所属部门"))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn("产品研发二部",html)
        self.assertNotIn("技术委员会",html)

    def test_limit_customer(self):
        '''测试限制范围用户自定义'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml("departmentradio","normal").format(name="自定义"))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn("系统运维部",html)
        self.assertNotIn("技术委员会",html)


    def test_default_user(self):
        '''测试默认值为当前用户'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        value = qiqiao.DepartmentRedio(self.driver).default("用户所属部门_")
        self.assertEqual("创新技术中心->产品研发二部",value)

    def test_default_customer(self):
        '''测试默认值为用户自定义'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        value = qiqiao.DepartmentRedio(self.driver).default("自定义部门")
        self.assertEqual("员工成功部",value)
