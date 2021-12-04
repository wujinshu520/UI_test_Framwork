# encoding: utf-8
# @author: wujinshu
# @file: run_all_cases.py
# @time:2021/10/17 17:13
# @desc: 执行层、执行所有测试用例

import os
import unittest
from common import HTMLTestReportCN
from common.config_untils import local_config
from common.emailUtils import EmailUtils

# 当前的路径
current_path = os.path.abspath(
    os.path.dirname(__file__)
)
# 测试用例路径
case_path = os.path.join(
    current_path,
    '..',
    local_config.case_path
)
# 测试报告目录路径
report_path = os.path.join(
    current_path,
    '..',
    local_config.report_path
)


class RunAllCases(object):
    def __init__(self):
        self.test_case_path = case_path  # 顶层目录
        self.report_path = report_path  # 报告路径
        self.title = "禅道自动化测试报告"  # 报告的标题
        self.description = "wujinshu"  # 描述

    def run(self):
        # 搜索出满足规则的用例
        discover = unittest.defaultTestLoader.discover(
            start_dir=self.test_case_path,  # 路径
            pattern='*case.py',  # 参数规则
            top_level_dir=self.test_case_path
        )
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        # 自动生成文件夹
        report_dir = HTMLTestReportCN.ReportDirectory(
            self.report_path
        )
        report_dir.create_dir(self.title)

        # 获取文件夹的目录
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path, 'wb')

        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=fp,
            title=self.title,
            tester="wujinshu"
        )
        runner.run(all_suite)
        fp.close()
        return dir_path


if __name__ == "__main__":
    # RunAllCases().run()
    dir_path = RunAllCases().run()  # 执行用例，返回当前报告文件夹路径
    print(dir_path)
    EmailUtils("吴进书自动化测试报告", dir_path).zip_send_mail()
