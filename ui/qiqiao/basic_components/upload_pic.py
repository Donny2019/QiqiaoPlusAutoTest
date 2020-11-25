'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:00
@File    : upload_pic.py
'''

import os
import time
from tools.operation import Operation
from ui.base.ui_driver import UiDriver
from setting.globalset import UiPath


class UploadPic(UiDriver):
    '''基础组件-图片上传'''
    def normal(self,filed_name,file_name):
        '''非必填'''
        loc = Operation().readXml("uploadpicture","normal").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(1)
        path =UiPath.file_path + "\\{file_name}".format(file_name=file_name)
        os.system(UiPath.exe_path+" "+path)


    def required(self,filed_name,file_name):
        '''必填上传图片'''
        loc = Operation().readXml("uploadpicture","required").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        path =UiPath.file_path + "\\{file_name}".format(file_name=file_name)
        os.system(UiPath.exe_path+" "+path)
