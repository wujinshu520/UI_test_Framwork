# 主页面类
from selenium.webdriver.common.by import By
from element_infos.login.login_page import LoginPage
from common.log_01 import logger
from common.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):  # 构造函数
        super().__init__(driver)  # 继承父类方法
        login_page = LoginPage()
        # login_page.input_username("test02")
        # login_page.input_password("newdream123")
        # login_page.click_login()
        # 页面的衔接
        self.driver = login_page.driver  # 把login_page的对象转移到main_page
        # 页面的元素
        self.companyname_showbox = self.driver.find_element(By.XPATH, '//h1[@id="companyname"]')
        self.myzone_menu = self.driver.find_element(By.XPATH, '//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH, '//li[@data-id="product"]')
        self.username_showspan = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')

    # 操作
    def get_companyname(self):  # 获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        logger.info("获取公司名称:" + value)
        return value

    def goto_myzone(self):  # 进入我的地盘
        self.myzone_menu.click()

    def goto_product(self):  # 进入产品模块
        self.product_menu.click()

    def get_username(self):  # 获取用户名称
        name = self.username_showspan.text
        logger.info("获取用户名成功，用户名为：" + str(name))
        return name


if __name__ == "__main__":
    main_page = MainPage()
    username = main_page.get_username()
    # main_page.goto_product()  报错
    # main_page.goto_myzone()  报错
    print("登录账户的用户名：", username)
