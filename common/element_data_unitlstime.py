# 读取元素识别Excel中的信息工具模块
import xlrd
import os

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, "../element_info_datas/element_infos_old.xlsx")


class ElementDataUtils(object):
    def __init__(self, module_name, page_name, element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(self.element_path)
        self.sheet = self.workbook.sheet_by_name(module_name)  # 模块
        self.page_name = page_name  # 页面
        self.row_count = self.sheet.nrows  # 求行数

    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.row_count):  # row_count= 4 取 1，2，3
            if self.sheet.cell_value(i, 2) == self.page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                element_info['timeout'] = self.sheet.cell_value(i, 5)
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos
    # element_info['timeout'] = self.sheet.cell_value(i, 5)
    # 如果Excel表中的超时时间未空的处理
    # 方案1：
    # time_out = self.sheet.cell_value(i, 5)
    # if time_out == "":
    #     timeout_value = 5.0
    # else:
    #     timeout_value = time_out
    # element_info['timeout'] = timeout_value


if __name__ == "__main__":
    elements = ElementDataUtils('login', page_name="login_page").get_element_info()
    for e in elements:
        print(e, elements[e])
