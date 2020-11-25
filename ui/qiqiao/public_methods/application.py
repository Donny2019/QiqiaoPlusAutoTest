'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:01
@File    : application.py
'''
import os
import time
from tools.operation import Operation
from ui.base.ui_driver import UiDriver
from setting.globalset import UiPath

class Application(UiDriver):
    '''应用中的公共方法'''

    def openAppPage(self):
        '''打开应用页面'''
        element = self.getElement(Operation().readXml("application", "apppage"))
        self.js("arguments[0].click()", element)

    def clickApp(self, appname):
        '''根据应用名称，打开应用'''
        loc = Operation().readXml("application", "app").format(app=appname)
        self.clickElement(loc)

    def clickLeftMenu(self, menu_name):
        '''根据菜单名称，点击左侧菜单'''
        loc = Operation().readXml("application", "leftmenu").format(menu=menu_name)
        self.clickElement(loc)

    def clickButtonInTitle(self, button_name):
        '''根据按钮名称，点击表头按钮'''
        loc = Operation().readXml("application", "title_btn").format(button=button_name)
        try:
            self.clickElement(loc)
        except Exception:
            time.sleep(1)
            self.F5()
            self.clickElement(loc)

    def clickButtonInForm(self, button_name, row_num):
        '''点击表单数据行，操作区按钮'''
        loc = Operation().readXml("application", "form_btn").format(button=button_name, row=row_num - 1)
        elements = self.getElements(loc)
        time.sleep(1)
        if len(elements) == 0:
            time.sleep(1)
            self.F5()
            self.getElements(loc)[2].click()
        else:
            elements[2].click()

    def clickSearchBtn(self):
        '''点击搜索按钮'''
        loc = Operation().readXml("application", "search_btn")
        self.clickElement(loc)

    def clickResetBtn(self):
        '''点击重置按钮'''
        loc = Operation().readXml("application", "reset_btn")
        self.clickElement(loc)

    def clickExpand(self):
        '''点击展开按钮'''
        loc = Operation().readXml("application", "expand")
        self.clickElement(loc)

    def openProcessPage(self):
        '''点击流程页面'''
        loc = Operation().readXml("application", "precesspage")
        self.clickElement(loc)

    def openProcess(self, name):
        '''打开流程'''
        loc = Operation().readXml("application", "openprecess").format(name)
        # loc = "xpath=>//p[@title='{}']/..".format(name)
        self.clickElement(loc)

    def clickSubmit(self):
        '''点击提交按钮'''
        loc = Operation().readXml("application", "submit_btn")
        self.clickElement(loc)

    def clickDeleteInForm(self, button_name, row_num):
        '''点击表单数据行，操作区删除按钮'''
        loc = Operation().readXml("application", "form_delete_btn").format(button_name, row_num)
        time.sleep(2)
        self.getElements(loc)[2].click()
        delete_loc = Operation().readXml("application", "delete_confirm_top")
        self.clickElement(delete_loc)

    def submitComment(self):
        '''点击表单评论提交按钮'''
        loc = Operation().readXml("formcomment", "submit")
        self.clickElement(loc)

    def commentAddAnnex(self, file_name):
        '''添加评论附件'''
        loc = Operation().readXml("formcomment", "add_annex")
        self.clickElement(loc)
        time.sleep(1)
        cmd = UiPath.exe_path+ " " +file_name
        os.system(cmd)

    def delete_comment(self, loc_time):
        '''根据评论时间，删除评论'''

        loc = Operation().readXml("formcomment", "up_time").format(uptime=loc_time)
        self.moveToElement(loc)
        self.clickElement(Operation().readXml("formcomment", "delete_btn").format(uptime=loc_time))
        self.clickElement(Operation().readXml("formcomment", "confrim"))

    def edit_comment(self, loc_time):
        '''编辑评论'''
        loc = Operation().readXml("formcomment", "up_time").format(uptime=loc_time)
        self.moveToElement(loc)
        self.clickElement(Operation().readXml("formcomment", "edit_btn").format(uptime=loc_time))

    def editCommentPageAddAnnex(self, file_name):
        '''点击编辑页面添加附件按钮'''
        self.clickElement(Operation().readXml("formcomment", "edit_add_annex"))
        time.sleep(1)
        cmd = UiPath.exe_path + " " +file_name
        os.system(cmd)
        time.sleep(1)
        self.clickElement(Operation().readXml("formcomment", "edit_confrim"))

    def editCommentPageDeleteAnnex(self):
        '''编辑页面删除附件'''

        self.clickElement(Operation().readXml("formcomment", "edit_delte_annex"))
        self.clickElement(Operation().readXml("formcomment", "edit_confrim"))

    def commentUploadFile(self, file_name):
        '''评论上传文件'''
        self.clickElement(Operation().readXml("formcomment", "table_file"))
        self.clickElement(Operation().readXml("formcomment", "upload_file"))
        time.sleep(1)
        cmd = UiPath.exe_path + " " + file_name
        os.system(cmd)
        time.sleep(1)
        self.clickElement(Operation().readXml("formcomment", "upload_file_confirm"))

    def commentInsertPic(self, file_name):
        '''评论内容插入图片'''

        self.clickElement("xpath=>//button[@aria-label='上传图片']")
        time.sleep(0.5)
        cmd = UiPath.exe_path + " " + file_name
        os.system(cmd)
        time.sleep(1)
        self.submitComment()

    def delete_all_data(self, btn_name):
        '''删除列表整页数据'''
        self.clickElement(Operation().readXml("application", "cheked_all_data"))
        self.clickElement(Operation().readXml("application", "delete_btn").format(button_name=btn_name))
        self.clickElement(Operation().readXml("application", "delete_confirm_top"))

    def deleteAllData(self, btn_name):
        '''删除列表所有数据'''
        self.clickElement(Operation().readXml("application", "cheked_all_data"))
        self.clickElement(Operation().readXml("application", "delete_btn").format(button_name=btn_name))
        self.clickElement(Operation().readXml("application", "delete_confirm_bottom"))