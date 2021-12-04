# 登录业务类

from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_untils import local_config


class LoginAction(object):
    def __init__(self, driver):
        self.login_page = LoginPage(driver)  # 传递驱动

    # 登录操作
    def login_action(self, username, password):
        # 传递用户名，密码
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        # 点击确认按钮
        self.login_page.click_login()

    # 登录成功操作
    def login_success(self, username, password):
        self.login_action(username, password)
        # 页面衔接问题
        # 登录成功之后，返回MainPage对象，只是把当前页面传给MainPage的构造方法，MainPage继承BasePage
        return MainPage(self.login_page.driver)

    # 登录失败的操作
    def login_fail(self, username, password):
        self.login_action(username, password)
        return self.login_page.get_login_fail_alert_content()

    # 默认登录
    def default_login(self):
        return self.login_success(local_config.user_name, local_config.pass_word)

    # 扩展：使用cookie绕过认证
    def login_by_cookie(self):
        pass
