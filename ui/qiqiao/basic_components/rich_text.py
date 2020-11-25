'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 16:58
@File    : rich_text.py
'''

from tools.operation import Operation
from ui.base.ui_driver import UiDriver
import time,os
from setting.globalset import UiPath


class RichText(UiDriver):
    '''基础组件-富文本'''
    def required(self,filed_name,value):
        '''必填富文本输入值'''
        self.switchToFrame(Operation().readXml('richtext','required').format(name=filed_name))
        loc=Operation().readXml('richtext','input')
        self.sendKeys(loc,value)
        self.switchFrameOut()

    def comment(self,value):
        '''评论区富文本输入值'''
        self.switchToFrame("xpath=>//iframe[@class='tox-edit-area__iframe']")
        loc="xpath=>//body[@id='tinymce']/p"
        self.sendKeys(loc,value)
        self.switchFrameOut()

    def commentInsertPic(self,file_name):
        '''评论区富文本插入图片'''
        self.switchToFrame("xpath=>//iframe[@class='tox-edit-area__iframe']")
        self.clickElement("xpath=>//button[@aria-label='上传图片']")
        time.sleep(0.5)
        path = UiPath.file_path+'\\'+'{file_name}'.format(file_name=file_name)
        exe = UiPath.exe_path
        cmd = exe + ' '+path
        os.system(cmd)

    def normal(self,filed_name,value):
        '''非必填富文本输入值'''
        self.switchToFrame(Operation().readXml('richtext','normal').format(name=filed_name))
        loc=Operation().readXml('richtext','input')
        self.sendKeys(loc,value)
        self.switchFrameOut()

    def insertPic(self,filed_name,file_name):
        '''富文本插入图片'''
        self.switchToFrame(Operation().readXml('richtext','required').format(name=filed_name))
        self.clickElement(Operation().readXml('richtext','uploadpic'))
        time.sleep(0.5)
        path = UiPath.file_path+'\\'+'{file_name}'.format(file_name=file_name)
        exe = UiPath.exe_path
        cmd = exe + ' '+path
        # path = "D:\Projects\MagicAutoTestFranmework\\web\data\img\{file_name}".format(file_name=file_name)
        #         # os.system("D:\Projects\MagicAutoTestFranmework\\web\data\exe\\upload.exe %s" % path)
        os.system(cmd)