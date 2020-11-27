'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:26
@File    : test_form_comment.py
'''

import unittest,time
from ui import qiqiao
from tools.read_config import WebConfig
from setting.globalset import UiPath



class TestFormComment(unittest.TestCase):
    '''测试表单评论'''
    def setUp(self) -> None:
        url = WebConfig().pc_business()
        self.driver = qiqiao.Login().loginRuntime(url)


    def tearDown(self) -> None:
        self.driver.quit()

    def test_aaaaaa(self):
        '''添加待评论数据'''
        qiqiao.Application(self.driver).clickLeftMenu("基础表")
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.SingleLineText(self.driver).normal("单行文本", "自动化")
        qiqiao.Application(self.driver).clickSubmit()
        html = self.driver.page_source
        self.assertIn("自动化", html)

    def test_comment_requried(self):
        '''测试表单评论必填'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        qiqiao.Application(self.driver).submitComment()
        time.sleep(0.5)
        msg = qiqiao.Application(self.driver).getText("xpath=>//p[@class='el-message__content']")
        self.assertEqual(msg, "评论内容为必填")

    def test_add_comment(self):
        '''测试添加评论'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        now = time.time()
        value = str(now) + "测试填写表单评论"
        qiqiao.RichText(self.driver).comment(value)
        qiqiao.Application(self.driver).submitComment()
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn(value, html)

    def test_upload_annex(self):
        '''测试表单评论添加附件'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        qiqiao.RichText(self.driver).comment("自动化上传图片")
        filename = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) + ".png"
        file_path = UiPath.screenshot_path + "\\" + filename
        qiqiao.Application(self.driver).getScreenshot(file_path)
        qiqiao.Application(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        qiqiao.Application(self.driver).submitComment()
        html = self.driver.page_source
        self.assertIn(filename, html)

    def test_delete_comment(self):
        '''测试删除评论'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        qiqiao.RichText(self.driver).comment("自动化上传图片")
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time())) + ".png"
        file_path = UiPath.screenshot_path + "\\" + filename
        qiqiao.Application(self.driver).getScreenshot(file_path)
        qiqiao.Application(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        up_time = time.strftime("%Y-%m-%d_%H:%M_%S", time.localtime(time.time()))
        tt = up_time.split("_")
        loc_time = tt[0] + " " + tt[1]
        qiqiao.Application(self.driver).submitComment()
        qiqiao.Application(self.driver).F5()
        qiqiao.Application(self.driver).acceptAlert()
        time.sleep(1)
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        time.sleep(1)
        qiqiao.Application(self.driver).delete_comment(loc_time)
        time.sleep(1)
        html = self.driver.page_source
        self.assertNotIn(filename, html)

    def test_edit_comment(self):
        '''测试评论编辑页面上传附件'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        qiqiao.RichText(self.driver).comment("自动化上传图片")
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time())) + ".png"
        file_path = UiPath.screenshot_path + "\\" + filename
        qiqiao.Application(self.driver).getScreenshot(file_path)
        qiqiao.Application(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        up_time = time.strftime("%Y-%m-%d_%H:%M_%S", time.localtime(time.time()))
        tt = up_time.split("_")
        loc_time = tt[0] + " " + tt[1]
        qiqiao.Application(self.driver).submitComment()
        qiqiao.Application(self.driver).F5()
        qiqiao.Application(self.driver).acceptAlert()
        time.sleep(1)
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        qiqiao.Application(self.driver).edit_comment(loc_time)
        filename1 = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) + ".png"
        file_path1 = UiPath.screenshot_path + "\\" + filename1
        qiqiao.Application(self.driver).getScreenshot(file_path1)
        qiqiao.Application(self.driver).editCommentPageAddAnnex(file_path1)
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn(filename1, html)

    def test_edit_delete_annex(self):
        '''测试评论编辑页面删除附件'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        qiqiao.RichText(self.driver).comment("自动化上传图片")
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time())) + ".png"
        file_path = UiPath.screenshot_path + "\\" + filename
        qiqiao.Application(self.driver).getScreenshot(file_path)
        qiqiao.Application(self.driver).commentAddAnnex(file_path)
        time.sleep(1)
        up_time = time.strftime("%Y-%m-%d_%H:%M_%S", time.localtime(time.time()))
        tt = up_time.split("_")
        loc_time = tt[0] + " " + tt[1]
        qiqiao.Application(self.driver).submitComment()
        qiqiao.Application(self.driver).F5()
        qiqiao.Application(self.driver).acceptAlert()
        time.sleep(1)
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        time.sleep(1)
        qiqiao.Application(self.driver).edit_comment(loc_time)
        qiqiao.Application(self.driver).editCommentPageDeleteAnnex()
        time.sleep(1)
        html = self.driver.page_source
        self.assertNotIn(filename, html)

    def test_comment_upload_file(self):
        '''测试评论上传文件'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time())) + ".png"
        file_path = UiPath.screenshot_path + "\\" + filename
        qiqiao.Application(self.driver).getScreenshot(file_path)
        qiqiao.Application(self.driver).commentUploadFile(file_path)
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn(filename, html)

    def test_comment_insert_pic(self):
        '''测试评论富文本插入图片'''
        qiqiao.Application(self.driver).clickButtonInForm("详情", 1)
        filename = time.strftime("%Y-%m-%d_%H-%M_%S", time.localtime(time.time())) + ".png"
        file_path = UiPath.screenshot_path + "\\" + filename
        qiqiao.Application(self.driver).getScreenshot(file_path)
        qiqiao.Application(self.driver).commentInsertPic(file_path)
        time.sleep(1)
        html = self.driver.page_source
        self.assertIn(filename, html)

    def test_zzzzz(self):
        '''删除自动化测试数据'''
        qiqiao.SingleLineText(self.driver).search("单行文本", "自动化")
        qiqiao.Application(self.driver).clickSearchBtn()
        time.sleep(1)
        qiqiao.Application(self.driver).delete_all_data("删除")