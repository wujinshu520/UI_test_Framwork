# encoding: utf-8
# @author: wujinshu
# @file:
# @time:2021/10/16 14:14
# @desc: 读取元素识别Excel中的信息工具模块

import xlrd
import os
from common.config_untils import local_config

current_path = os.path.dirname(__file__)
# excel_path = os.path.join(current_path, "../element_info_datas/element_infos_old.xlsx")
excel_path = os.path.join(current_path, '..', local_config.element_info_path)


class ElementDataUtils():
    def __init__(self, module_name, page_name, element_path=excel_path):
        self.element_path = element_path

        self.element_path = os.path.join(
            self.element_path,
            module_name,
            page_name + '.xlsx'
        )

        self.workbook = xlrd.open_workbook(self.element_path)
        # self.sheet = self.workbook.sheet_by_name(module_name)
        self.sheet = self.workbook.sheet_by_index(0)  # 默认取第一个sheet
        self.row_count = self.sheet.nrows  # 求行数

    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.row_count):  # row_count= 4 取 1，2，3
            # if self.sheet.cell_value(i, 2) == page_name:
            element_info = {}
            element_info['element_name'] = self.sheet.cell_value(i, 1)
            element_info['locator_type'] = self.sheet.cell_value(i, 2)
            element_info['locator_value'] = self.sheet.cell_value(i, 3)

            timeout_value = self.sheet.cell_value(i, 4)
            element_info['timeout'] = timeout_value if isinstance(
                timeout_value, float) else local_config.time_out

            element_infos[self.sheet.cell_value(i, 0)] = element_info

        return element_infos


if __name__ == "__main__":
    # elements = ElementDataUtils('login').get_element_info('login_page')
    elements = ElementDataUtils('login', 'login_page').get_element_info()
    for e in elements.keys():
        print(e, elements[e])
