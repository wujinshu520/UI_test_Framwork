# str1 = "bug标题：%s"
# title = "动态元素通过业务数据识别"
# print("bug标题：%s"%title)
# print(str1%title)
# str2 = str1%title
# print(str2)

from common.element_data_unitls import ElementDataUtils

elements = ElementDataUtils('login').get_element_info('bug_page')
print(elements['bug_link'])
# 通过业务数据识别元素
title = "动态元素通过业务数据识别"  # 业务数据
bug_link = elements['bug_link']
# 方式1：
element_name01 = bug_link['element_name'] % title
# 方式2：
element_name = elements['bug_link']['element_name'] % title
locator_value = elements['bug_link']['locator_value'] % title

print(element_name01)
print(element_name)
print(locator_value)
