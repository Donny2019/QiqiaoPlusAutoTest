'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:29
@File    : test_upload_pic.py
'''
from tools.read_config import WebConfig
import unittest
from ui import qiqiao
from tools.operation import Operation


class TestUploadPic(unittest.TestCase):
    '''测试图片上传'''
    def setUp(self) -> None:
        url = WebConfig().uploadpic()
        self.driver = qiqiao.Login().loginRuntimeByCookie(url)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_requierd(self):
        '''测试图片上传必填校验'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText("xpath=>//div[@class='el-form-item__error']")
        self.assertEqual(msg, "不能为空")

    def test_limit_size(self):
        '''测试上传限制大于1M图片'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadPic(self.driver).normal("图片大于1兆","大于6M.jpg")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture','msg'))
        self.assertEqual("上传文件大小不能超过1MB",msg)

    # def test_upload_pic(self):
    #     '''测试图片上传'''
    #     qiqiao.Application(self.driver).clickButtonInTitle("添加")
    #     qiqiao.UploadPic(self.driver).normal("裁剪2比1","大于6M.jpg")
    #     time.sleep(1)
    #     qiqiao.Application(self.driver).clickSubmit()
    #     time.sleep(1)
    #     html = self.driver.page_source
    #     self.assertIn("大于6M.jpg",html)
