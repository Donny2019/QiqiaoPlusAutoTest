'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 17:01
@File    : login.py
'''

import time

from tools.operation import Operation
from ui.base.ui_driver import UiDriver
from setting.globalset import UiPath
from tools.read_config import WebConfig
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Login():
    def loginRuntime(self, url):
        '''登录PC端运行平台'''
        username = WebConfig().username()
        password = WebConfig().password()
        driver = webdriver.Chrome(executable_path=UiPath.chrome_driver_path)
        UiDriver(driver).openUrl(url)
        UiDriver(driver).clickElement(Operation().readXml("login", "account"))
        UiDriver(driver).sendKeys(Operation().readXml("login", "username"), username)
        UiDriver(driver).sendKeys(Operation().readXml("login", "password"), password)
        UiDriver(driver).clickElement(Operation().readXml("login", "submit"))
        return driver



    def longConsole(self):
        '''登录开发平台'''
        pass


    def loginRuntimeByCookie(self,direct_url):
        cooke = WebConfig().cookies()
        bowser = WebConfig().bowser()
        if bowser=="firefox":

            driver = webdriver.Firefox(executable_path=Path.firefox_driver_path)
            driver.maximize_window()
            driver.get(WebConfig().url())
            driver.add_cookie(cooke)
            time.sleep(1)
            driver.get(direct_url)
        elif bowser == "chrome":

            driver = webdriver.Chrome(executable_path=Path.chrome_driver_path)
            driver.maximize_window()
            driver.get(WebConfig().url())
            driver.get(direct_url)
            driver.add_cookie(cooke)


        else:
            raise TypeError("未设置任何浏览器，请在web.yaml文件中设置浏览器")

        return driver