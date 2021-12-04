# driver 的二次封装
import os
import time

from selenium import webdriver
from common.config_untils import local_config
from selenium.webdriver.chrome.options import Options
from common.log_untils import logger

current_path = os.path.dirname(__file__)
dri_path = os.path.join(current_path, '..', local_config.get_driver_path)
dri_name = local_config.driver_name


class Browser(object):
    def __init__(self, driver_path=dri_path, driver_name=dri_name):
        self.__driver_path = driver_path
        self.__driver_name = driver_name  # 读取选择的测试浏览器类型

    # 获取驱动的driver的再次封装：根据测试需要，修改配置文件，选择不同的浏览器
    def get_driver(self):
        if self.__driver_name.lower() == "chrome":
            return Browser().__get_chrome_driver()
        elif self.__driver_name.lower() == "firefox":
            return Browser().__get_firefox_driver()
        elif self.__driver_name.lower() == "edge":
            return Browser().__get_edge_driver()

    # 谷歌浏览器的驱动
    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=ZH_CH.UTF-8')  # 设置默认编码为UTF-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消Chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome 受自动控制提示
        chrome_driver_path = os.path.join(self.__driver_path, 'chromedriver')
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        logger.info("初始化Google浏览器并启动")
        return driver

    # 火狐浏览器的驱动
    def __get_firefox_driver(self):
        firefox_driver_path = os.path.join(self.__driver_path, 'geckodriver')
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        logger.info("初始化Firefox浏览器并启动")
        return driver

    # edge的驱动
    def __get_edge_driver(self):
        edge_driver_path = os.path.join(self.__driver_path, 'MicrosfWebDriver')
        driver = webdriver.Edge(executable_path=edge_driver_path)
        logger.info("初始化Edge浏览器并启动")
        return driver

    # 分布式，远程的浏览器驱动
    def __get_remote_driver(self):  # selenium 支持分布式执行grid
        pass


if __name__ == "__main__":
    driver = Browser().get_driver()
    driver.get("https://www.baidu.com")
    time.sleep(5)
    driver.quit()
