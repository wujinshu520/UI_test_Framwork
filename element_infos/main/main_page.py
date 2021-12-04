# 主页面类

from common.base_page import BasePage
from common.element_data_unitls import ElementDataUtils


class MainPage(BasePage):
    def __init__(self, dirver):
        super().__init__(dirver)  # 继承主页面
        elements = ElementDataUtils('main', 'main_page').get_element_info()
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value

    # 点击用户菜单
    def click_username(self):
        self.click(self.user_menu)

    # 点击退出
    def click_quit_button(self):
        self.click(self.quit_button)
