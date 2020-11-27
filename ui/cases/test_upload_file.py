'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:28
@File    : test_upload_file.py
'''

import time
import unittest
from tools.operation import Operation
from ui import qiqiao
from tools.read_config import WebConfig


class TestUploadFile(unittest.TestCase):
    '''测试文件上传'''
    def setUp(self) -> None:
        url = WebConfig().uploadfile()
        self.driver = qiqiao.Login().loginRuntime(url)

    def tearDown(self) -> None:
        self.driver.quit()


    def test_required(self):
        '''测试必填'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.Application(self.driver).clickSubmit()
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg','requiredmsg'))
        self.assertEqual("不能为空",msg)


    def test_limit_file_size(self):
        '''测试上传文件大小'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).normal("文件小于1兆","大于6M.jpg")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture', 'msg'))
        self.assertEqual("上传文件大小不能超过1MB!", msg)

    def test_limit_file_amount(self):
        '''测试上传文件数量'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).required("必填_提示","大写.PNG")
        qiqiao.UploadFile(self.driver).normal("文件数量2到4","大写.PNG")
        qiqiao.Application(self.driver).clickSubmit()
        time.sleep(1)
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('msg', 'requiredmsg'))
        self.assertEqual("上传数量必须在2到4之间", msg)

    def test_limit_pic(self):
        '''测试限制上传图片'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).normal("限制图片","doc格式文件.doc")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture', 'msg'))
        self.assertEqual("仅支持上传jpg/jpeg/gif/png/bmp格式文件！", msg)

    def test_limit_zip(self):
        '''测试限制上传zip文件'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).normal("限制压缩文件","doc格式文件.doc")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture', 'msg'))
        self.assertEqual("仅支持上传zip/rar/7z格式文件！", msg)


    def test_limit_word(self):
        '''测试限制上传word文件'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).normal("限制word文档","ppt格式文件.pptx")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture', 'msg'))
        self.assertEqual("仅支持上传doc/docx格式文件！", msg)

    def test_limit_excel(self):
        '''测试限制上传excel文件'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).normal("限制表格","ppt格式文件.pptx")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture', 'msg'))
        self.assertEqual("仅支持上传xls/xlsx/csv格式文件！", msg)

    def test_limit_ppt(self):
        '''测试限制上传ppt文件'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).normal("限制幻灯片","doc格式文件.doc")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture', 'msg'))
        self.assertEqual("仅支持上传ppt/pptx格式文件！", msg)

    def test_limit_pdf(self):
        '''测试限制上传pdf文件'''
        qiqiao.Application(self.driver).clickButtonInTitle("添加")
        qiqiao.UploadFile(self.driver).normal("限制pdf文档","doc格式文件.doc")
        msg = qiqiao.Application(self.driver).getText(Operation().readXml('uploadpicture', 'msg'))
        self.assertEqual("仅支持上传pdf格式文件！", msg)