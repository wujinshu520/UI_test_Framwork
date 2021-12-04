# 登录页面类
from common.base_page import BasePage
from common.element_data_unitls import ElementDataUtils
from common.browser import Browser


class LoginPage(BasePage):  # LoginPage类，继承BasePage类
    def __init__(self, driver):
        super().__init__(driver)  # 继承父类的driver
        # elements = ElementDataUtils(page_name="login_page").get_element_info()
        # elements = ElementDataUtils('login').get_element_info('login_page')
        elements = ElementDataUtils('login', 'login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

        # 打开浏览器
        # self.driver = webdriver.Chrome(executable_path=driver_path)
        # self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        # 属性--->页面上的控件
        # super().__init__(driver)  # 继承父类的driver
        # self.username_inputbox = self.driver.find_element(By.XPATH, '//input[@name="account"]')
        # self.password_inputbox = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        # self.login_button = self.driver.find_element(By.XPATH, '//button[@id="submit"]')
        # self.keepLoginon_checkbox = self.driver.find_element(By.XPATH, '//input[@name="keepLogin[]"]')
        # 字典形式封装返回元素
        # self.username_inputbox = {'element_name': '用户输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="account"]',
        #                           'timeout': 5}
        #
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'timeout': 5}
        #
        # self.login_button = {'element_name': '登录按钮',
        #                      'locator_type': 'xpath',
        #                      'locator_value': '//button[@id="submit"]',
        #                      'timeout': 5}
        #
        # self.keepLoginon_checkbox = {'element_name': '记住密码复选框',
        #                              'locator_type': 'xpath',
        #                              'locator_value': '//input[@name="keepLogin[]"]',
        #                              'timeout': 5}

    # 方法---> 控件的操作
    def input_username(self, username):
        # self.username_inputbox.send_keys(username)
        self.input(self.username_inputbox, username)
        # logger.info("用户名输入框输入：" + str(username))

    def input_password(self, password):
        # self.password_inputbox.send_keys(password)
        self.input(self.password_inputbox, password)
        # logger.info("密码输入框输入：" + str(password))

    def click_login(self):
        # self.login_button.click()
        self.click(self.login_button)
        # logger.info("点击登录按钮")

    # 登录失败，返回提示框
    def get_login_fail_alert_content(self):
        return self.switch_to_alert()


if __name__ == "__main__":
    # current = os.path.dirname(__file__)
    # driver_path = os.path.join(current, '../webdriver/chromedriver')
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver = Browser().get_driver()
    login_page = LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
#    login_page.screentshot_as_file()
    login_page.exit_quit()
