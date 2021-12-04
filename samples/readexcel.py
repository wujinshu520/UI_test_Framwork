# 测试读取Excel表
import xlrd
import os

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, "../element_info_datas/element_infos.xlsx")

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name("login_page")

row_count = sheet.nrows  # 求行数
element_infos = {}
'''
一行的数据
self.login_button = {'element_name': '登录按钮',
                             'locator_type': 'xpath',
                             'locator_value': '//button[@id="submit"]',
                             'timeout': 5}
'''
for i in range(1, row_count):  # row_count= 4 取 1，2，3
    element_info = {}
    element_info['element_name'] = sheet.cell_value(i, 1)
    element_info['locator_type'] = sheet.cell_value(i, 2)
    element_info['locator_value'] = sheet.cell_value(i, 3)
    element_info['timeout'] = sheet.cell_value(i, 4)
    element_infos[sheet.cell_value(i, 0)] = element_info
for element_info in element_infos:
    print(element_info, element_infos[element_info])
