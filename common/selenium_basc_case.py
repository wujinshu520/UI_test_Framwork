# 基础用例类
import unittest
from common.config_untils import local_config
from common.browser import Browser
from common.base_page import BasePage
from common.log_untils import logger


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 测试类的前置
        logger.info("")
        logger.info("========= 测试类初始化 ===========")
        cls.url = local_config.get_url  # 获取地址

    def setUp(self):  # 测试方法的前置
        logger.info("----------- 测试类执行完毕 ----------")
        self.driver = Browser().get_driver()
        self.base_page = BasePage(self.driver)
        self.base_page.open_url(self.url)
        self.base_page.set_browser_max()
        self.base_page.implicitly_Wait()

    @classmethod
    def tearDownClass(cls):  # 测试类的后置
        logger.info("==== 测试类执行完毕 ====")

    def tearDown(self):  # 测试方法的后置
        # 测试用例执行断言失败的截图
        # errors = self._Outcome.errors  # 判断断言错误
        # for test, exc_info in errors:
        #     if exc_info:
        #         self.base_page.wait()
        #         self.base_page.screentshot_as_file()
        #         logger.error("断言执行失败，已截图")
        self.base_page.close_table()
        logger.info("--------- 测试类执行完毕 ---------")
