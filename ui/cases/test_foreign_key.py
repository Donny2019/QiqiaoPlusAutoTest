'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:26
@File    : test_foreign_key.py
'''
import datetime
import time
import unittest
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig

class TestForeignKey(unittest.TestCase):
    '''测试外键选择组件'''
    def setUp(self) -> None:
        url = WebConfig().foreignkey()
        self.driver = qiqiao.Login().loginRuntime(url)


    def tearDown(self) -> None:
        self.driver.quit()

    def test_show_feild(self):
        '''测试外键附加显示字段'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection','normal').format(name='外键选择'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('青青子衿悠悠我心',html)

    def test_filter_singletext(self):
        '''测试单行文本筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection','normal').format(name='单行文本'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('筛选单行文本数据',html)
        self.assertNotIn('筛选单行文本被过滤数据',html)

    def test_filter_multipletext(self):
        '''测试多行文本筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='多行文本'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('应该显示的数据', html)
        self.assertNotIn('不应该显示的数据', html)

    def test_filter_number(self):
        '''测试数字筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='数字'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('数字应该显示的数据', html)
        self.assertNotIn('数字不应该显示的数据', html)

    def test_filter_singlechoice(self):
        '''测试单项选择筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='单项选择'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('单项选择应该显示的数据', html)
        self.assertNotIn('单项选择不应该显示的数据', html)

    def test_filter_multiplechoices(self):
        '''测试多项选择筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='多项选择'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('多项选择应该显示的数据', html)
        self.assertNotIn('多项选择不应该显示的数据', html)

    def test_filter_date(self):
        '''测试日期筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='日期'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('日期应该显示的数据', html)
        self.assertNotIn('日期不应该显示的数据', html)

    def test_filter_date_type_day(self):
        '''测试日类型日期变量逻辑'''
        qiqiao.Application(self.driver).clickLeftMenu("字段条件")
        time.sleep(0.3)
        qiqiao.Application(self.driver).clickLeftMenu("日类型日期")
        qiqiao.Application(self.driver).clickButtonInForm("编辑",2)
        now_time = datetime.datetime.now()
        qiqiao.Date(self.driver).delete('变量本周')
        qiqiao.Date(self.driver).normal('变量本周',now_time.strftime('%Y-%m-%d'))
        offset = datetime.timedelta(days=-7)
        re_date = (now_time+offset).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('变量上周')
        qiqiao.Date(self.driver).normal('变量上周',re_date)
        qiqiao.Date(self.driver).delete('变量本月')
        qiqiao.Date(self.driver).normal('变量本月',now_time.strftime('%Y-%m-%d'))
        month = datetime.timedelta(days=-30)
        re_month = (now_time+month).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('变量上月')
        qiqiao.Date(self.driver).normal('变量上月',re_month)
        qiqiao.Date(self.driver).delete('变量今年')
        qiqiao.Date(self.driver).normal('变量今年',now_time.strftime('%Y-%m-%d'))
        year = datetime.timedelta(days=-365)
        re_year = (now_time+year).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('变量去年')
        qiqiao.Date(self.driver).normal('变量去年',re_year)
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='日类型日期'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('日类型日期应该显示数据', html)
        self.assertNotIn('日类型日期不应该显示数据', html)

    def test_filter_date_type_month(self):
        '''测试月类型日期外键筛选数据'''
        qiqiao.Application(self.driver).clickLeftMenu("字段条件")
        time.sleep(0.3)
        qiqiao.Application(self.driver).clickLeftMenu("月类型日期")
        qiqiao.Application(self.driver).clickButtonInForm("编辑",2)
        now_time = datetime.datetime.now()
        qiqiao.Date(self.driver).delete('变量今年')
        qiqiao.Date(self.driver).normal('变量今年',now_time.strftime('%Y-%m-%d'))
        ago_year = datetime.timedelta(days=-369)
        past_year = (now_time+ago_year).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('变量去年')
        qiqiao.Date(self.driver).normal('变量去年',past_year)
        ago_month = datetime.timedelta(days=-31)
        past_month = (now_time+ago_month).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('过去1月')
        qiqiao.Date(self.driver).normal('过去1月',past_month)
        ago = datetime.timedelta(days=-365)
        past = (now_time + ago).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('过去1年')
        qiqiao.Date(self.driver).normal('过去1年',past)
        future = (now_time+datetime.timedelta(days=+31)).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('未来1月')
        qiqiao.Date(self.driver).normal('未来1月',future)
        future_year = (now_time+datetime.timedelta(days=+365)).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('未来1年')
        qiqiao.Date(self.driver).normal('未来1年',future_year)
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='月类型日期'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('月类型应该显示的数据', html)
        self.assertNotIn('月类型不应该显示的数据', html)


    def test_filter_date_type_year(self):
        '''测试年类型日期筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("字段条件")
        time.sleep(0.3)
        qiqiao.Application(self.driver).clickLeftMenu("年类型日期")
        qiqiao.Application(self.driver).clickButtonInForm("编辑",2)
        now_time = datetime.datetime.now()
        ago = datetime.timedelta(days=-365)
        past = (now_time + ago).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('过去一年')
        qiqiao.Date(self.driver).normal('过去一年',past)
        future_year = (now_time + datetime.timedelta(days=+365)).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('未来一年')
        qiqiao.Date(self.driver).normal('未来一年',future_year)
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='年类型日期'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('年类型日期应用显示数据', html)
        self.assertNotIn('年类型日期不应该显示数据', html)

    def test_filter_date_type_equel_param(self):
        '''测试日期逻辑等于变量筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("字段条件")
        time.sleep(0.3)
        qiqiao.Application(self.driver).clickLeftMenu("日期等于变量")
        qiqiao.Application(self.driver).clickButtonInForm("编辑",2)
        now_time = datetime.datetime.now()
        qiqiao.Date(self.driver).delete('等于今天')
        qiqiao.Date(self.driver).normal('等于今天',now_time.strftime('%Y-%m-%d'))
        yesteday = (now_time+datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('等于昨天')
        qiqiao.Date(self.driver).normal('等于昨天',yesteday)
        tomorrow = (now_time+datetime.timedelta(days=+1)).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('等于明天')
        qiqiao.Date(self.driver).normal('等于明天',tomorrow)
        before_yesteday = (now_time+datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('等于前天')
        qiqiao.Date(self.driver).normal('等于前天',before_yesteday)
        after_tomorrow = (now_time+datetime.timedelta(days=+2)).strftime('%Y-%m-%d')
        qiqiao.Date(self.driver).delete('等于后天')
        qiqiao.Date(self.driver).normal('等于后天',after_tomorrow)
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='日期等于变量'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('日期等于变量应该显示数据', html)
        self.assertNotIn('日期等于变量不应该显示数据', html)

    def test_filter_time(self):
        '''测试时间组件筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='时间'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('时间应该显示数据', html)
        self.assertNotIn('时间不应该显示数据', html)

    def test_filter_datetime(self):
        '''测试日期时间筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='日期时间'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('日期时间应该显示数据', html)
        self.assertNotIn('日期时间不应该显示数据', html)

    def test_filter_date_time(self):
        '''测试日期时间范围变量筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("字段条件")
        time.sleep(0.3)
        qiqiao.Application(self.driver).clickLeftMenu("范围变量")
        qiqiao.Application(self.driver).clickButtonInForm("编辑",2)
        now_time = datetime.datetime.now()
        qiqiao.DateTime(self.driver).delete('今天')
        qiqiao.DateTime(self.driver).normal('今天',now_time.strftime('%Y-%m-%d %H:%M'))
        yesteday = (now_time + datetime.timedelta(days=-1)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('昨天')
        qiqiao.DateTime(self.driver).normal('昨天',yesteday)
        tomorrow = (now_time + datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('明天')
        qiqiao.DateTime(self.driver).normal('明天', tomorrow)
        before_yesteday = (now_time + datetime.timedelta(days=-2)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('前天')
        qiqiao.DateTime(self.driver).normal('前天', before_yesteday)
        after_tomorrow = (now_time + datetime.timedelta(days=+2)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('后天')
        qiqiao.DateTime(self.driver).normal('后天', after_tomorrow)
        qiqiao.DateTime(self.driver).delete('本周')
        qiqiao.DateTime(self.driver).normal('本周', now_time.strftime('%Y-%m-%d %H:%M'))
        past_week = (now_time+datetime.timedelta(days=-7)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('上周')
        qiqiao.DateTime(self.driver).normal('上周', past_week)
        qiqiao.DateTime(self.driver).delete('本月')
        qiqiao.DateTime(self.driver).normal('本月', now_time.strftime('%Y-%m-%d %H:%M'))
        past_month = (now_time+datetime.timedelta(days=-31)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('上月')
        qiqiao.DateTime(self.driver).normal('上月', past_month)
        qiqiao.DateTime(self.driver).normal('今年',now_time.strftime('%Y-%m-%d %H:%M'))
        past_year = (now_time+datetime.timedelta(days=-365)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('去年')
        qiqiao.DateTime(self.driver).normal('去年', past_year)
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='范围变量'))
        time.sleep(0.5)
        html = self.driver.page_source
        self.assertIn('范围变量应该显示数据', html)
        self.assertNotIn('范围变量不应该显示数据', html)
        datetime.timedelta()


    def test_filter_limit(self):
        '''测试范围过去筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("字段条件")
        time.sleep(0.3)
        qiqiao.Application(self.driver).clickLeftMenu("范围过去")
        qiqiao.Application(self.driver).clickButtonInForm("编辑",2)
        now_time = datetime.datetime.now()
        past_year = (now_time+datetime.timedelta(days=-365)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('过去1年')
        qiqiao.DateTime(self.driver).normal('过去1年',past_year)
        past_month = (now_time+datetime.timedelta(days=-31)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('过去1月')
        qiqiao.DateTime(self.driver).normal('过去1月', past_month)
        past_day = (now_time+datetime.timedelta(days=-1)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('过去1天')
        qiqiao.DateTime(self.driver).normal('过去1天', past_day)
        past_week = (now_time+datetime.timedelta(days=-7)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('过去1周')
        qiqiao.DateTime(self.driver).normal('过去1周', past_week)
        past_hour = (now_time+datetime.timedelta(minutes=-60)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('过去1小时')
        qiqiao.DateTime(self.driver).normal('过去1小时', past_hour)
        past_minutes = (now_time+datetime.timedelta(minutes=-1)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('过去1分钟')
        qiqiao.DateTime(self.driver).normal('过去1分钟', past_minutes)
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='范围过去'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('范围过去应该显示的数据', html)
        self.assertNotIn('范围过去不应该显示数据', html)

    def test_filter_future(self):
        '''测试范围未来筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("字段条件")
        time.sleep(0.3)
        qiqiao.Application(self.driver).clickLeftMenu("范围未来")
        qiqiao.Application(self.driver).clickButtonInForm("编辑",2)
        now_time = datetime.datetime.now()
        future_year = (now_time+datetime.timedelta(days=+365)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('未来1年')
        qiqiao.DateTime(self.driver).normal('未来1年',future_year)
        future_month = (now_time+datetime.timedelta(days=+31)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('未来1月')
        qiqiao.DateTime(self.driver).normal('未来1月', future_month)
        future_day = (now_time+datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('未来1天')
        qiqiao.DateTime(self.driver).normal('未来1天', future_day)
        future_week = (now_time+datetime.timedelta(days=+7)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('未来1周')
        qiqiao.DateTime(self.driver).normal('未来1周', future_week)
        future_hour = (now_time+datetime.timedelta(minutes=+60)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('未来1小时')
        qiqiao.DateTime(self.driver).normal('未来1小时', future_hour)
        future_minutes = (now_time+datetime.timedelta(minutes=+10)).strftime('%Y-%m-%d %H:%M')
        qiqiao.DateTime(self.driver).delete('未来1分钟')
        qiqiao.DateTime(self.driver).normal('未来1分钟', future_minutes)
        qiqiao.Application(self.driver).clickSubmit()
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='范围未来'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('范围未来应该显示数据', html)
        self.assertNotIn('范围未来不应该显示的数据', html)

    def test_filter_personal_selecter(self):
        '''测试人员单选筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='人员单选'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('人员单选应该显示的数据', html)
        self.assertNotIn('人员单选不应该显示的数据', html)

    def test_filter_department(self):
        '''测试部门单选筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='部门单选'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('部门单选应该显示的数据', html)
        self.assertNotIn('部门单选不应该显示的数据', html)

    def test_filter_departments(self):
        '''测试部门多选筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='部门多选'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('部门多选应该显示的数据', html)
        self.assertNotIn('部门多选不应该的数据', html)

    def test_filter_address(self):
        '''测试地址选择筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='地址选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('地址选择应该显示的数据', html)
        self.assertNotIn('地址选择不应该显示的数据', html)

    def test_filter_score(self):
        '''测试地址选择筛选外键数据'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("全局筛选条件")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='评分'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('评分应该显示的数据', html)
        self.assertNotIn('评分不应该显示的数据', html)


    def test_linked_singletext(self):
        '''测试联动筛选单行文本'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("单行文本联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal('等于道一','道一')
        qiqiao.SingleLineText(self.driver).normal('不等于道一','哈哈哈')
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection','normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('筛选单行文本数据',html)
        self.assertNotIn('筛选单行文本被过滤数据',html)


    def test_linked_number(self):
        '''测试联动筛选数字'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("数字联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Number(self.driver).normal('等于5',5)
        qiqiao.Number(self.driver).normal('不等于5',8)
        qiqiao.Number(self.driver).normal('大于5',9)
        qiqiao.Number(self.driver).normal('小于5',4)
        qiqiao.Number(self.driver).normal('大于等于5',5)
        qiqiao.Number(self.driver).normal('小于等于5',5)
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('数字应该显示的数据', html)
        self.assertNotIn('数字不应该显示的数据', html)

    def test_linked_singlechoice(self):
        '''测试联动筛选单项选择'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("单项选择联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleChoice(self.driver).dropDownNormal('等于中国','中国')
        qiqiao.SingleChoice(self.driver).dropDownNormal('不等于中国','日本')
        qiqiao.SingleChoice(self.driver).dropDownNormal('等于任意一个','美国')
        qiqiao.SingleChoice(self.driver).dropDownNormal('不等于任意一个','美国')
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('单项选择应该显示的数据', html)
        self.assertNotIn('单项选择不应该显示的数据', html)

    def test_linked_multiplechoices(self):
        '''测试联动筛选多项选择'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("多项选择联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.MultipleChoices(self.driver).dropDownNormal('等于','北京')
        qiqiao.MultipleChoices(self.driver).dropDownNormal('不等于','北京','上海')
        qiqiao.MultipleChoices(self.driver).dropDownNormal('包含','北京','上海')
        qiqiao.MultipleChoices(self.driver).dropDownNormal('不包含','北京')
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('多项选择应该显示的数据', html)
        self.assertNotIn('多项选择不应该显示的数据', html)

    def test_linked_date(self):
        '''测试日期联动筛选'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("日期联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Date(self.driver).normal('等于','2020-06-06')
        time.sleep(1)
        qiqiao.Date(self.driver).normal('不等于','2020-11-04')
        time.sleep(1)
        qiqiao.Date(self.driver).normal('大于','2020-06-09')
        time.sleep(1)
        qiqiao.Date(self.driver).normal('小于','2020-11-02')
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('日期应该显示的数据', html)
        self.assertNotIn('日期不应该显示的数据', html)


    def test_linked_personal_selecter(self):
        '''测试联动筛选人员单选'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("人员单选联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.PersonnelSelection(self.driver).normal('等于','刁惠云')
        qiqiao.PersonnelSelection(self.driver).normal('不等于','吴健伦')
        qiqiao.PersonnelSelection(self.driver).normal('等于任意一个','罗琳月')
        qiqiao.PersonnelSelection(self.driver).normal('不等于任意一个','王浩')
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('人员单选应该显示的数据', html)
        self.assertNotIn('人员单选不应该显示的数据', html)

    def test_linked_personals(self):
        '''测试联动筛选人员多选'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        qiqiao.Application(self.driver).clickLeftMenu("人员多选联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.MultiplePersonnel(self.driver).normal('等于','刁惠云','罗琳月')
        time.sleep(1)
        qiqiao.MultiplePersonnel(self.driver).normal('不等于','孙铋舰','孙财和')
        time.sleep(1)
        qiqiao.MultiplePersonnel(self.driver).normal('包含','孙奥博','孙保民')
        time.sleep(1)
        qiqiao.MultiplePersonnel(self.driver).normal('不包含','李四','孙岑')
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('人员多选应该显示的数据', html)
        self.assertNotIn('人员多选不应该显示的数据', html)


    def test_linked_department(self):
        '''测试部门外键联动'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("部门选择联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        qiqiao.DepartmentRedio(self.driver).normal('等于','创新技术中心')
        qiqiao.DepartmentRedio(self.driver).normal('不等于','员工成功部')
        qiqiao.MultipleDepartments(self.driver).normal('等于任意一个','事业二部','董办')
        qiqiao.MultipleDepartments(self.driver).normal('不等于任意一个','创新技术中心','事业二部')
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('部门单选应该显示的数据', html)
        self.assertNotIn('部门单选不应该显示的数据', html)

    def test_linked_score(self):
        '''测试评分数据联动'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("评分联动")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        qiqiao.Score(self.driver).normal('等于',3)
        qiqiao.Score(self.driver).normal('不等于',5)
        qiqiao.Score(self.driver).normal('大于',3)
        qiqiao.Score(self.driver).normal('小于',5)
        qiqiao.Score(self.driver).normal('大于等于',3)
        qiqiao.Score(self.driver).normal('小于等于',3)
        qiqiao.Application(self.driver).clickElement(Operation().readXml('foreignkeyselection', 'normal').format(name='外键选择'))
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn('评分应该显示的数据', html)
        self.assertNotIn('评分不应该显示的数据', html)

    def test_foreign_deliver(self):
        '''测试外键选择字段值传递'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("外键字段传递")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        qiqiao.ForergnKeySelection(self.driver).normal('外键选择','测试数据')
        time.sleep(2)
        qiqiao.Application(self.driver).clickSubmit()
        time.sleep(3)
        html = self.driver.page_source
        self.assertIn('测试数据',html)
        self.assertIn('青青子衿悠悠我心',html)
        self.assertIn('30',html)
        self.assertIn('40',html)
        self.assertIn('50.00',html)
        self.assertIn('50.0%',html)
        self.assertIn('95',html)
        self.assertIn('美国',html)
        self.assertIn('北京',html)
        self.assertIn('宝马',html)
        self.assertIn('奔驰s600',html)
        self.assertIn('2020-10-29',html)
        self.assertIn('15:23',html)
        self.assertIn('2020-10-29 00:00',html)
        self.assertIn('苹果.jpg',html)
        self.assertIn('孙奥博',html)
        self.assertIn('孙洁',html)
        self.assertIn('孙慧颖',html)
        self.assertIn('系统运维部',html)
        self.assertIn('创新技术中心',html)
        self.assertIn('山西省/太原市/小店区 南派12号',html)
        qiqiao.Application(self.driver).deleteAllData('删除')

    def test_foreign_value_deliver(self):
        '''测试外键选择传递外键关联字段'''
        qiqiao.Application(self.driver).clickLeftMenu("外键选择")
        time.sleep(1)
        qiqiao.Application(self.driver).clickLeftMenu("外键字段传递")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        time.sleep(1)
        qiqiao.ForergnKeySelection(self.driver).normal('外键字段','测试数据')
        time.sleep(2)
        qiqiao.Application(self.driver).clickSubmit()
        time.sleep(3)
        html = self.driver.page_source
        self.assertIn('测试数据',html)
        self.assertIn('青青子衿悠悠我心',html)
        self.assertIn('30',html)
        self.assertIn('40',html)
        self.assertIn('50.00',html)
        self.assertIn('50.0%',html)
        self.assertIn('95',html)
        self.assertIn('美国',html)
        self.assertIn('北京',html)
        self.assertIn('宝马',html)
        self.assertIn('奔驰s600',html)
        self.assertIn('2020-10-29',html)
        self.assertIn('15:23',html)
        self.assertIn('2020-10-29 00:00',html)
        self.assertIn('苹果.jpg',html)
        self.assertIn('孙奥博',html)
        self.assertIn('孙洁',html)
        self.assertIn('孙慧颖',html)
        self.assertIn('系统运维部',html)
        self.assertIn('创新技术中心',html)
        self.assertIn('山西省/太原市/小店区 南派12号',html)
        qiqiao.Application(self.driver).deleteAllData('删除')
