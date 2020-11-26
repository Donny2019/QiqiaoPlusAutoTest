'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 18:00
@File    : globalset.py
'''
import os


class UiPath:
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chrome_driver_path = base_path + "/ui/drivers/chromedriver.exe"
    firefox_driver_path = base_path + "/ui/drivers/geckodriver.exe"
    exe_path = base_path + "/ui/data/exe/upload.exe"
    file_path = base_path + "/ui/data/file"
    xml_path = base_path + "/ui/elements"
    report_path = base_path + "/ui/reports"
    screenshot_path = base_path + "/ui/screenshots"
    cases_path = base_path + "/ui/cases"
    yaml_path = base_path + "/ui/config"


class AppPath:
    pass