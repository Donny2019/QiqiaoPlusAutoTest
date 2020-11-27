'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:28
@File    : test_trigger_event.py
'''

import unittest,time
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig


class TestTriggerEvent(unittest.TestCase):
    '''测试触发事件'''
    def setUp(self) -> None:
        url = WebConfig().pc_business()
        self.driver = qiqiao.Login().loginRuntime(url)



    def tearDown(self) -> None:
        self.driver.quit()

    def test_insert_event(self):
        '''测试插入本表主表字段'''

        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInForm("主表字段",6)
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("目标表")
        time.sleep(2)
        html = self.driver.page_source
        self.assertIn("单行文本",html)
        self.assertIn("多行文本",html)
        self.assertIn("20",html)
        self.assertIn("中国",html)
        self.assertIn("北京",html)
        self.assertIn("奔驰",html)
        self.assertIn("奔驰S600,奔驰cls300,奔驰E300",html)
        self.assertIn("2020-10-12",html)
        self.assertIn("17:00",html)
        self.assertIn("2020-10-12 00:00",html)
        self.assertIn("ceshi.png",html)
        self.assertIn("曾嘉凌",html)
        self.assertIn("律强,邓基富",html)
        self.assertIn("事业一部",html)
        self.assertIn("质量部",html)
        self.assertIn("北京/北京市/东城区 12号公寓",html)
        self.assertIn("华为/mate30",html)
        self.assertIn("00002",html)
        qiqiao.Application(self.driver).delete_all_data("删除")

    def test_insert_foreign_key_event(self):
        '''测试插入主表外键字段'''
        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInForm("外键字段",5)
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("目标表")
        time.sleep(2)
        html = self.driver.page_source
        self.assertIn("外键数据",html)
        self.assertIn("多行文本",html)
        self.assertIn("20",html)
        self.assertIn("中国",html)
        self.assertIn("北京",html)
        self.assertIn("奔驰",html)
        self.assertIn("奔驰S600,奔驰cls300,奔驰E300",html)
        self.assertIn("2020-10-12",html)
        self.assertIn("18:38",html)
        self.assertIn("2020-10-12 00:00",html)
        self.assertIn("ceshi.png",html)
        self.assertIn("曾嘉凌",html)
        self.assertIn("律强,邓基富",html)
        self.assertIn("技术委员会",html)
        self.assertIn("人力资源部",html)
        self.assertIn("天津/天津市/和平区 20公寓",html)
        self.assertIn("苹果/iphone12",html)
        self.assertIn("00001",html)
        qiqiao.Application(self.driver).delete_all_data("删除")


    def test_insert_subform_event(self):
        '''测试插入事件插入子表单数据'''

        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInForm("子表字段",4)
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("目标表")
        time.sleep(2)
        html = self.driver.page_source
        self.assertIn("子表数据1",html)
        self.assertIn("子表2多行文本",html)
        self.assertIn("22",html)
        self.assertIn("中国",html)
        self.assertIn("纽约",html)
        self.assertIn("奔驰",html)
        self.assertIn("宝马X3,宝马X5,宝马X6",html)
        self.assertIn("2020-10-12",html)
        self.assertIn("18:56",html)
        self.assertIn("2020-10-12 00:00",html)
        self.assertIn("ceshi.png",html)
        self.assertIn("曾嘉凌",html)
        self.assertIn("孙奥博,孙邦原",html)
        self.assertIn("技术委员会",html)
        self.assertIn("质量委员会",html)
        self.assertIn("山西省/太原市/小店区 呵呵呵",html)
        self.assertIn("华为/mate30",html)
        self.assertIn("00001",html)
        qiqiao.Application(self.driver).delete_all_data("删除")

    def test_insert_child_table(self):
        '''测试插入子表关联字段数据'''

        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInForm("子表关联",3)
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("目标表")
        time.sleep(2)
        html = self.driver.page_source
        self.assertIn("子表数据1",html)
        self.assertIn("子表2多文本",html)
        self.assertIn("22",html)
        self.assertIn("中国",html)
        self.assertIn("纽约",html)
        self.assertIn("奔驰",html)
        self.assertIn("宝马X3,宝马X5,宝马X6",html)
        self.assertIn("2020-10-12",html)
        self.assertIn("18:56",html)
        self.assertIn("2020-10-12 00:00",html)
        self.assertIn("ceshi.png",html)
        self.assertIn("曾嘉凌",html)
        self.assertIn("孙奥博,孙邦原",html)
        self.assertIn("技术委员会",html)
        self.assertIn("质量委员会",html)
        self.assertIn("山西省/太原市/小店区",html)
        self.assertIn("华为/mate30",html)
        self.assertIn("00001",html)
        qiqiao.Application(self.driver).delete_all_data("删除")

    def test_insert_mutil_table(self):
        '''测试插入多表字段触发事件'''

        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInForm("多表字段",2)
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("目标表")
        time.sleep(2)
        html = self.driver.page_source
        self.assertIn("消息通知测试",html)
        self.assertIn("测试数据显示多行文本",html)
        self.assertIn("15",html)
        self.assertIn("美国",html)
        self.assertIn("纽约",html)
        self.assertIn("宝马",html)
        self.assertIn("奔驰S600,奔驰cls300,奔驰E300",html)
        self.assertIn("2020-09-14",html)
        self.assertIn("11:45",html)
        self.assertIn("2020-09-13 00:00",html)
        self.assertIn("大写.PNG",html)
        self.assertIn("孙财和",html)
        self.assertIn("王栋一",html)
        self.assertIn("事业二部",html)
        self.assertIn("系统运维部",html)
        self.assertIn("天津/天津市/和平区",html)
        self.assertIn("华为/mate30",html)
        self.assertIn("00006",html)
        qiqiao.Application(self.driver).delete_all_data("删除")

    def test_delete_event(self):
        '''测试触发删除事件'''
        qiqiao.Application(self.driver).clickLeftMenu("删除事件目标表")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal("单行文本","待删除数据")
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInTitle("删除事件")
        qiqiao.Application(self.driver).clickSubmit()
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("删除事件目标表")
        title = qiqiao.Application(self.driver).getText("xpath=>//span[@class='el-pagination__total']")
        self.assertIn("0",title)


    def test_update_event(self):
        '''测试触发事件更新数据'''
        qiqiao.Application(self.driver).clickLeftMenu("更新事件目标表")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal("单行文本","待更新数据")
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInForm("更新事件",6)
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("更新事件目标表")
        time.sleep(2)
        html = self.driver.page_source
        self.assertIn("主表字段",html)
        self.assertIn("多行文本",html)
        self.assertIn("20",html)
        self.assertIn("中国",html)
        self.assertIn("北京",html)
        self.assertIn("奔驰",html)
        self.assertIn("奔驰S600,奔驰cls300,奔驰E300",html)
        self.assertIn("2020-10-12",html)
        self.assertIn("17:00",html)
        self.assertIn("2020-10-12 00:00",html)
        self.assertIn("ceshi.png",html)
        self.assertIn("曾嘉凌",html)
        self.assertIn("律强,邓基富",html)
        self.assertIn("事业一部",html)
        self.assertIn("质量部",html)
        self.assertIn("北京/北京市/东城区 12号公寓",html)
        self.assertIn("华为/mate30",html)
        self.assertIn("00002",html)
        qiqiao.Application(self.driver).deleteAllData("删除")


    def test_msg_event(self):
        '''测试触发事件消息通知——(请在手机端登录企业微信查看是否收到消息通知和群机器人测试结果)'''

        qiqiao.Application(self.driver).clickLeftMenu("触发事件")
        qiqiao.Application(self.driver).clickButtonInForm("消息通知",1)
        self.assertEqual(0,1)