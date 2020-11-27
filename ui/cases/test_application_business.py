'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 18:30
@File    : test_application_business.py
'''
import time,unittest
import pytest
from tools.operation import Operation
from tools.read_config import WebConfig
from ui import qiqiao


class TestAPPlicationBusiness(unittest.TestCase):
    '''测试应用主业务'''

    def setUp(self) -> None:
        url = WebConfig().pc_business()
        self.driver = qiqiao.Login().loginRuntimeByCookie(url)
        
    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_data(self):
        '''测试添加数据'''
        qiqiao.Application(self.driver).clickLeftMenu("基础表")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal("单行文本","自动化")
        qiqiao.Application(self.driver).clickSubmit()
        html = self.driver.page_source
        self.assertIn("自动化" ,html)


    def test_upload_pic(self):
        '''测试图片上传'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal("单行文本", "自动化2")
        qiqiao.UploadPic(self.driver).normal("图片上传","ceshi.png")
        time.sleep(1)
        qiqiao.Application(self.driver).clickSubmit()
        html = self.driver.page_source
        self.assertIn("ceshi.png", html)

    def test_upload_file(self):
        '''测试上传文件'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal("单行文本", "自动化1")
        qiqiao.UploadFile(self.driver).normal("文件上传","动画图片.gif")
        time.sleep(2)
        qiqiao.Application(self.driver).clickSubmit()
        html = self.driver.page_source
        self.assertIn("动画图片.gif",html)


    def test_search_by_line_text(self):
        '''通过单行文本筛选页面数据'''

        qiqiao.SingleLineText(self.driver).search("单行文本","测试数据")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)


    def test_search_by_multiline_text(self):
        '''通过多行文本筛选页面数据'''

        qiqiao.MultilineText(self.driver).search("多行文本","哈哈哈")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)

    def test_search_by_number(self):
        '''通过数字筛选页面数据'''

        qiqiao.Number(self.driver).search("数字",15)
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)


    def test_search_by_single_choice(self):
        '''通过单项选择筛选页面数'''

        qiqiao.Application(self.driver).clickExpand()
        qiqiao.SingleChoice(self.driver).search("单项下拉","东京")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)

    def test_search_by_multiple_choice(self):
        '''通过多项选择筛选页面数据'''

        qiqiao.Application(self.driver).clickExpand()
        qiqiao.MultipleChoices(self.driver).search("多项选择","奥迪")
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1", title)

    def test_search_by_date(self):
        '''通过日期筛选页面数据'''

        qiqiao.Application(self.driver).clickExpand()
        qiqiao.Date(self.driver).search("日期","2020-09-15","2020-09-17")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)


    def test_search_by_person_selector(self):
        '''通过人员选择筛选页面数据'''

        qiqiao.Application(self.driver).clickExpand()
        qiqiao.PersonnelSelection(self.driver).search("人员单选","刁惠云")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)

    def test_search_by_time(self):
        '''通过时间筛选页面数据'''
        qiqiao.Application(self.driver).clickExpand()
        qiqiao.Time(self.driver).search("时间","11:30","12:00")
        time.sleep(10)
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)

    def test_search_by_datetime(self):
        '''通过日期时间筛选页面数据'''
        qiqiao.Application(self.driver).clickExpand()
        qiqiao.DateTime(self.driver).search("日期时间","2020-09-15 00:00 至 2020-09-16 00:00")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)

    def test_search_by_department(self):
        '''通过部门选择筛选页面数据'''
        qiqiao.Application(self.driver).clickExpand()
        qiqiao.DepartmentRedio(self.driver).search("部门单选","产","创新技术中心->产品研发二部")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)

    def test_search_by_address(self):
        '''通过地址选择筛选页面数据'''
        qiqiao.Application(self.driver).clickExpand()
        qiqiao.AddressSelection(self.driver).search("地址选择器","河南省","郑州市","中原区")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)

    def test_search_by_score(self):
        '''通过评分字段筛选页面数据'''
        qiqiao.Application(self.driver).clickExpand()
        qiqiao.Score(self.driver).search("评分",5)
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("1",title)


    def test_search_by_creaperson(self):
        '''通过创建人筛选页面数据'''

        qiqiao.Application(self.driver).clickExpand()
        qiqiao.PersonnelSelection(self.driver).search("创建人","刁惠云")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("0",title)



    def test_search_by_createdate(self):
        '''通过创建日期筛选页面数据'''

        qiqiao.Application(self.driver).clickExpand()
        qiqiao.Date(self.driver).search("创建时间","2020-09-13","2020-09-14")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("0",title)


    def test_search_by_editdate(self):
        '''通过修改日期筛选页面数据'''
        qiqiao.Application(self.driver).clickExpand()
        qiqiao.Date(self.driver).search("修改时间","2020-09-13","2020-09-14")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("0",title)


    def test_combination_search(self):
        '''测试组合筛选页面数据'''
        qiqiao.Application(self.driver).clickExpand()
        qiqiao.Date(self.driver).search("修改时间","2020-10-26","2020-10-27")
        qiqiao.PersonnelSelection(self.driver).search("创建人",  "刁惠云")
        qiqiao.DepartmentRedio(self.driver).search("部门单选","产","创新技术中心->产品研发二部")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        title = qiqiao.Application(self.driver).getText(Operation().readXml('application','totaldata'))
        self.assertIn("0",title)


    def test_form_only_check(self):
        '''测试表单唯一校验'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal("单行文本","测试数据")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','prompt'))
        self.assertEqual(msg,"单行文本必须唯一！！！")



    def test_hide_left_menu(self):
        '''测试设置左侧页面不显示为菜单'''
        html = self.driver.page_source
        self.assertNotIn("不显示菜单",html)
