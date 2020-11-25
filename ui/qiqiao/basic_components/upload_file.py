'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:00
@File    : upload_file.py
'''
import os,time
from tools.operation import Operation
from ui.base.ui_driver import UiDriver
from setting.globalset import UiPath


class UploadFile(UiDriver):
    '''基础组件-文件上传'''
    def normal(self,filed_name,file):
        '''非必填'''
        loc=Operation().readXml("uploadfile","normal").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        path =UiPath.file_path + "\\{file_name}".format(file_name=file)
        os.system(UiPath.exe_path+" "+path)


    def required(self,filed_name,file):
        '''必填'''
        loc=Operation().readXml("uploadfile","required").format(name=filed_name)
        self.clickElement(loc)
        time.sleep(0.5)
        path =UiPath.file_path + "\\{file_name}".format(file_name=file)
        os.system(UiPath.exe_path+" "+path)