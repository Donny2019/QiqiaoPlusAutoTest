'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/24 19:07
@File    : conftest.py
'''
import time

import pytest

from tools.read_config import WebConfig
from ui import qiqiao

@pytest.fixture(scope="class")
def beforclass():
    url = WebConfig().pc_business()
    global driver
    driver = qiqiao.Login().loginRuntime(url)
    yield driver
    driver.quit()
@pytest.fixture(scope="function")
def refreshPage():
    time.sleep(1)
    driver.refresh()


