'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:57
@File    : read_config.py
'''
from .operation import Operation


class WebConfig:
    def bowser(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml','beta','switch')
        if qa_info is True:
            bowser = Operation().readYaml('web.yaml','qa','browser')
        elif prod_info is True:
            bowser = Operation().readYaml('web.yaml','prod','browser')
        elif beta_info is True:
            bowser = Operation().readYaml('web.yaml','beta','browser')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return bowser

    def url(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml','beta','switch')
        if qa_info is True:
            url = Operation().readYaml('web.yaml','qa','url')
        elif prod_info is True:
            url = Operation().readYaml('web.yaml','prod','url')
        elif beta_info is True:
            url = Operation().readYaml('web.yaml','beta','url')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return url

    def username(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            username = Operation().readYaml('web.yaml','qa','username')
        elif prod_info is True:
            username = Operation().readYaml('web.yaml','prod','username')
        elif beta_info is True:
            username =Operation().readYaml('web.yaml','beta','username')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return username

    def password(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            password = Operation().readYaml('web.yaml','qa','password')
        elif prod_info is True:
            password = Operation().readYaml('web.yaml','prod','password')
        elif beta_info is True:
            password = Operation().readYaml('web.yaml','beta','password')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return password

    def cookies(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            cookies = dict(Operation().readYaml('web.yaml','qa','cookies'))
        elif prod_info is True:
            cookies = Operation().readYaml('web.yaml','prod','cookies')
        elif beta_info is True:
            cookies = Operation().readYaml('web.yaml','beta','cookies')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return cookies

    def multilinetext(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            multilinetext = Operation().readYaml('web.yaml','qa','multilinetext')
        elif prod_info is True:
            multilinetext = Operation().readYaml('web.yaml','prod','multilinetext')
        elif beta_info is True:
            multilinetext = Operation().readYaml('web.yaml','beta','multilinetext')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return multilinetext

    def number(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            number = Operation().readYaml('web.yaml','qa','number')
        elif prod_info is True:
            number = Operation().readYaml('web.yaml','prod','number')
        elif beta_info is True:
            number = Operation().readYaml('web.yaml','beta','number')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return number

    def pc_business(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            pc_business = Operation().readYaml('web.yaml', 'qa', 'pc_business')
        elif prod_info is True:
            pc_business = Operation().readYaml('web.yaml','prod','pc_business')
        elif beta_info is True:
            pc_business = Operation().readYaml('web.yaml','beta','pc_business')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return pc_business

    def singlechoice(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            singlechoice = Operation().readYaml('web.yaml','qa','singlechoice')
        elif prod_info is True:
            singlechoice = Operation().readYaml('web.yaml','prod','singlechoice')
        elif beta_info is True:
            singlechoice = Operation().readYaml('web.yaml','beta','singlechoice')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return singlechoice

    def singlelinetext(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            singlelinetext = Operation().readYaml('web.yaml','qa','singlelinetext')
        elif prod_info is True:
            singlelinetext = Operation().readYaml('web.yaml','prod','singlelinetext')
        elif beta_info is True:
            singlelinetext = Operation().readYaml('web.yaml','beta','singlelinetext')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return singlelinetext

    def multiplechoice(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            multiplechoice = Operation().readYaml('web.yaml','qa','multiplechoice')
        elif prod_info is True:
            multiplechoice = Operation().readYaml('web.yaml','prod','multiplechoice')
        elif beta_info is True:
            multiplechoice = Operation().readYaml('web.yaml','beta','multiplechoice')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return multiplechoice

    def date(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            date = Operation().readYaml('web.yaml','qa','date')
        elif prod_info is True:
            date = Operation().readYaml('web.yaml','prod','date')
        elif beta_info is True:
            date = Operation().readYaml('web.yaml','beta','date')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return date


    def formcomment(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            formcomment = Operation().readYaml('web.yaml','qa','formcomment')
        elif prod_info is True:
            formcomment = Operation().readYaml('web.yaml','prod','formcomment')
        elif beta_info is True:
            formcomment = Operation().readYaml('web.yaml','beta','formcomment')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return formcomment

    def foreignkey(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            foreignkey = Operation().readYaml('web.yaml','qa','foreignkey')
        elif prod_info is True:
            foreignkey = Operation().readYaml('web.yaml','prod','foreignkey')
        elif beta_info is True:
            foreignkey = Operation().readYaml('web.yaml','beta','foreignkey')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return foreignkey

    def uploadpic(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            uploadpic = Operation().readYaml('web.yaml','qa','uploadpic')
        elif prod_info is True:
            uploadpic = Operation().readYaml('web.yaml','prod','uploadpic')
        elif beta_info is True:
            uploadpic = Operation().readYaml('web.yaml','beta','uploadpic')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return uploadpic

    def uploadfile(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            uploadfile = Operation().readYaml('web.yaml','qa','uploadfile')
        elif prod_info is True:
            uploadfile = Operation().readYaml('web.yaml','prod','uploadfile')
        elif beta_info is True:
            uploadfile = Operation().readYaml('web.yaml','beta','uploadfile')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return uploadfile

    def personnelselection(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            personnelselection = Operation().readYaml('web.yaml','qa','personnelselection')
        elif prod_info is True:
            personnelselection = Operation().readYaml('web.yaml','prod','personnelselection')
        elif beta_info is True:
            personnelselection = Operation().readYaml('web.yaml','beta','personnelselection')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return personnelselection

    def departmentradio(self):
        qa_info = Operation().readYaml('web.yaml','qa','switch')
        prod_info = Operation().readYaml('web.yaml','prod','switch')
        beta_info = Operation().readYaml('web.yaml', 'beta', 'switch')
        if qa_info is True:
            departmentradio = Operation().readYaml('web.yaml','qa','departmentradio')
        elif prod_info is True:
            departmentradio = Operation().readYaml('web.yaml','prod','departmentradio')
        elif beta_info is True:
            departmentradio = Operation().readYaml('web.yaml','beta','departmentradio')
        else:
            raise TypeError("yaml文件配配置有误，请检查测试参数switch是否设置为True")
        return departmentradio