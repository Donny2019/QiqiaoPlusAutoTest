'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 14:27
@File    : test_date.py
'''
import datetime,unittest
import time
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig


class TestDate(unittest.TestCase):
    '''测试日期组件属性'''
    def setUp(self) -> None:
        url = WebConfig().date()
        self.driver = qiqiao.Login().loginRuntimeByCookie(url)
    def tearDown(self) -> None:
        self.driver.quit()

    def test_required(self):
        '''测试必填'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickSubmit()
        error_loc = Operation().readXml('msg','requiredmsg')
        msg = qiqiao.Application(self.driver).getText(error_loc)
        self.assertEqual("不能为空",msg)

    def test_default_value(self):
        '''获取默认值'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        value = qiqiao.Date(self.driver).getDefaultValue("默认2019920")
        self.assertEqual(value,'2019-09-20')
    def test_default_tody(self):
        '''测试日期设置默认值为当天'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Tab(self.driver).clickTab("默认填写当天")
        value = qiqiao.Date(self.driver).getDefaultValue("默认填写当天")
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        self.assertEqual(value,now_time)

    def test_default_three_days_ago(self):
        '''测试日期设置默认值为当天前三天'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Tab(self.driver).clickTab("默认填写前3天")
        value = qiqiao.Date(self.driver).getDefaultValue("默认前3天")
        now_time = datetime.datetime.now()
        offset = datetime.timedelta(days=-3)
        re_date = (now_time+offset).strftime('%Y-%m-%d')
        self.assertEqual(value,re_date)

    def test_default_next_three_days(self):
        '''测试日期设置默认值为当天后三天'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Tab(self.driver).clickTab("默认填写后3天")
        value = qiqiao.Date(self.driver).getDefaultValue("默认后3天")
        now_time = datetime.datetime.now()
        offset = datetime.timedelta(days=+3)
        re_date = (now_time+offset).strftime('%Y-%m-%d')
        self.assertEqual(value,re_date)

    def test_date_limit_more(self):
        '''测试日期限制逻辑大于'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Date(self.driver).required("必填_提示",'2019-09-20')
        qiqiao.Tab(self.driver).clickTab("大于920")
        qiqiao.Date(self.driver).normal("大于920","2019-09-10")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,'大于920')

    def test_date_limit_less(self):
        '''测试日期限制逻辑小于'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Date(self.driver).required("必填_提示",'2019-09-20')
        qiqiao.Tab(self.driver).clickTab("大于920")
        qiqiao.Date(self.driver).normal("大于920","2020-09-10")
        qiqiao.Tab(self.driver).clickTab("小于920")
        qiqiao.Date(self.driver).normal("小于920","2020-09-10")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,'小于920')

    def test_date_limit_equal(self):
        '''测试日期限制逻辑等于'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Date(self.driver).required("必填_提示",'2019-09-20')
        qiqiao.Tab(self.driver).clickTab("大于920")
        qiqiao.Date(self.driver).normal("大于920","2020-09-10")
        qiqiao.Tab(self.driver).clickTab("小于920")
        qiqiao.Date(self.driver).normal("小于920","2019-09-10")
        qiqiao.Tab(self.driver).clickTab("等于920")
        qiqiao.Date(self.driver).normal("等于920","2019-09-10")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,'等于920')

    def test_date_limit_not_equal(self):
        '''测试日期限制逻辑不等于'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Date(self.driver).required("必填_提示",'2019-09-20')
        qiqiao.Tab(self.driver).clickTab("大于920")
        qiqiao.Date(self.driver).normal("大于920","2020-09-10")
        qiqiao.Tab(self.driver).clickTab("小于920")
        qiqiao.Date(self.driver).normal("小于920","2019-09-10")
        qiqiao.Tab(self.driver).clickTab("等于920")
        qiqiao.Date(self.driver).normal("等于920","2019-09-20")
        qiqiao.Tab(self.driver).clickTab("不等于920")
        qiqiao.Date(self.driver).normal("不等于920","2019-09-20")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,'不等于920')

    def test_date_limit_greater_and_equal(self):
        '''测试日期限制逻辑大于等于'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Date(self.driver).required("必填_提示",'2019-09-20')
        qiqiao.Tab(self.driver).clickTab("大于920")
        qiqiao.Date(self.driver).normal("大于920","2020-09-10")
        qiqiao.Tab(self.driver).clickTab("小于920")
        qiqiao.Date(self.driver).normal("小于920","2019-09-10")
        qiqiao.Tab(self.driver).clickTab("等于920")
        qiqiao.Date(self.driver).normal("等于920","2019-09-20")
        qiqiao.Tab(self.driver).clickTab("不等于920")
        qiqiao.Date(self.driver).normal("不等于920","2019-09-21")
        qiqiao.Tab(self.driver).clickTab("大于等于920")
        qiqiao.Date(self.driver).normal("大于等于920","2019-09-11")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,'大于等于920')

    def test_date_limit_less_and_equal(self):
        '''测试日期限制逻辑小于等于'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Date(self.driver).required("必填_提示",'2019-09-20')
        qiqiao.Tab(self.driver).clickTab("大于920")
        qiqiao.Date(self.driver).normal("大于920","2020-09-10")
        qiqiao.Tab(self.driver).clickTab("小于920")
        qiqiao.Date(self.driver).normal("小于920","2019-09-10")
        qiqiao.Tab(self.driver).clickTab("等于920")
        qiqiao.Date(self.driver).normal("等于920","2019-09-20")
        qiqiao.Tab(self.driver).clickTab("不等于920")
        qiqiao.Date(self.driver).normal("不等于920","2019-09-21")
        qiqiao.Tab(self.driver).clickTab("大于等于920")
        qiqiao.Date(self.driver).normal("大于等于920","2019-09-21")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,'小于等于920')