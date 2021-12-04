# 退出操作
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage


class QuitAction(object):
    def __init__(self, driver):
        self.main_page = MainPage(driver)  # 在主页面才能退出

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        # 页面衔接问题，成功退出后，返回一个login_page页面
        return LoginPage(self.main_page.driver)
