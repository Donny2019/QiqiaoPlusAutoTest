'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:56
@File    : operation.py
'''

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml
from xml.dom.minidom import parse
import time,os
from setting.globalset import UiPath


class Operation():

    def makeFile(self,file_path):
        '''根据当前时间生成文件夹'''
        time_now = time.strftime("%Y-%m-%d", time.localtime())
        path = file_path + "\\" + time_now
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.exists(path):
            pass
        return path

    def deleteAllFile(self,file_path):
        '''删除文件夹下的所有文件'''

        del_list = os.listdir(file_path)
        for f in del_list:
            file = os.path.join(UiPath.screenshot_path, f)
            os.remove(file)

    def readXml(self,components, child_name):
        '''读取xml文件'''

        files = os.listdir(UiPath.xml_path)
        path = UiPath.xml_path
        for file in files:
            domtree = parse(os.path.join(path, file))
            rootnode = domtree.documentElement
            elements = rootnode.getElementsByTagName(components)
            try:
                loc = elements[0].getElementsByTagName(child_name)[0].getAttribute("loc")
            except:
                continue
            return loc

    def readYaml(self,file_name, key=None, key1=None):
        '''读取yaml配置文件'''
        yamlPath = UiPath.yaml_path + "/" + file_name
        f = open(yamlPath, 'r', encoding='utf-8')
        cfg = f.read()
        d = yaml.safe_load(cfg)
        if key1 is None and key is None:
            f.close()
            return d
        elif key != None and key1 == None:
            f.close()
            return d[key]
        else:
            f.close()
            return d[key][key1]

    def sendEmail(self,*args):
        '''发送邮件'''
        sender_mail = '981772991@qq.com'
        sender_pass = 'uchyilsslfvmbfhf'
        time_now = time.strftime("%Y-%m-%d", time.localtime())
        # 设置总的邮件体对象，对象类型为mixed
        msg_root = MIMEMultipart('mixed')
        # 邮件添加的头尾信息等
        msg_root['From'] = 'Donny<981772991@qq.com>'
        msg_root['To'] = "wangdongyi@do1.com.cn"
        # 邮件的主题，显示在接收邮件的预览页面
        subject = '自动化测试报告'
        msg_root['subject'] = Header(subject, 'utf-8')
        # 文本内容
        detil_file = open(UiPath.report_path + "\\" + time_now + "\\" + "结果概要.html", "rb")
        text_info = detil_file.read()
        text_sub = MIMEText(text_info, 'html', 'utf-8')
        msg_root.attach(text_sub)
        # 构造附件

        fiel_path = UiPath.report_path + "\\" + time_now + "\\" + "七巧Web自动化测试报告.html"
        txt_file = open(r'{}'.format(fiel_path), 'rb').read()
        txt = MIMEText(txt_file, 'base64', 'utf-8')
        txt["Content-Type"] = 'application/octet-stream'
        txt.add_header('Content-Disposition', 'attachment', filename="七巧Web自动化测试报告.html")
        msg_root.attach(txt)

        try:
            for to_person in args:
                sftp_obj = smtplib.SMTP('smtp.qq.com', 25)
                sftp_obj.login(sender_mail, sender_pass)
                sftp_obj.sendmail(sender_mail, to_person, msg_root.as_string())
                sftp_obj.quit()
                print('发送邮件成功！！！')

        except Exception as e:
            print('发送邮件失败，以下是失败原因！！')
            print(e)
