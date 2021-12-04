# encoding: utf-8
# @author: wujinshu
# @file: test_data_utils.py
# @time:2021/10/17 12:52
# @desc: 读取测试数据
import os
from common.config_untils import local_config
from common.excel_utils import ExcelUtils

current_path = os.path.abspath(os.path.dirname(__file__))
testdata_path = os.path.join(
    current_path,
    '..',
    local_config.testdata_path)


class TestDataUtils(object):
    def __init__(self, test_suite_name, test_fail_name,
                 test_class_name, test_data_path=testdata_path):

        self.test_class_name = test_class_name

        test_data_path = os.path.join(
            test_data_path, test_suite_name,
            test_fail_name + '.xlsx'
        )

        self.excel_data = ExcelUtils(
            test_data_path,
            test_class_name
        ).get_sheet_data_by_list()

        self.excel_row = len(self.excel_data)  # 求excel 表中的行数，控制循环用的

    def convert_exceldata_testdata(self):
        test_data_infos = {}
        for i in range(1, self.excel_row):  # 共3行，读取第2，3行，下标分别为 1，2
            test_data_info = {}
            # if self.excel_data[i][2].__eq__(self.test_class_name):  # __eq__ 等于
            test_data_info['test_name'] = self.excel_data[i][1]
            # test_data_info['isnot'] = self.excel_data[i][3]
            test_data_info['isnot'] = False if self.excel_data[i][2].__eq__('是') else True
            test_data_info['excepted_result'] = self.excel_data[i][3]
            test_parameter = {}
            for j in range(4, len(self.excel_data[i])):
                if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j]) > 2:
                    parameter_info = self.excel_data[i][j].split('=')  # 通过 = 切割数据
                    test_parameter[parameter_info[0]] = parameter_info[1]
            test_data_info['test_parameter'] = test_parameter
            test_data_infos[self.excel_data[i][0]] = test_data_info
        return test_data_infos


if __name__ == "__main__":
    test_data_infos = TestDataUtils(
        'login_suite', 'login_case', 'LoginCase'
    ).convert_exceldata_testdata()

    for s in test_data_infos:
        print(s, test_data_infos[s])
