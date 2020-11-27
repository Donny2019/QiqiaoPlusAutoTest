'''
-*- coding: utf-8 -*-
@Author  : PlayerGuan
@Time    : 2020/11/26 16:12
@File    : run.py
'''

import HTMLReport,unittest
from setting.globalset import UiPath
from tools.operation import Operation


screenshot_path = UiPath.screenshot_path
report_file = UiPath.report_path
Operation().deleteAllFile(screenshot_path)
path = Operation().makeFile(report_file)
# create_cooke('prod')
if __name__=="__main__":
    discover = unittest.defaultTestLoader.discover(UiPath.cases_path, pattern="test_*.py", top_level_dir=None)
    runner = HTMLReport.TestRunner(
                     report_file_name="七巧Web自动化测试报告",
                     log_file_name="日志文件",
                     output_path=path ,
                     title= "ui测试报告",
                     description= "七巧回归测试",
                     thread_count=2,
                     thread_start_wait= 5,
                     sequential_execution=True,
                     lang="cn"
    )
    runner.run(discover)
    # Funcations().sendEmail("wangdongyi@do1.com.cn","diaohuiyun@do1.com.cn","wujianlun@do1.com.cn","luolinyue@do1.com.cn")