import unittest
from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.selenium_basc_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class QuitCase(SeleniumBaseCase):
    test_class_data = TestDataUtils(
        'main_suite',
        'quit_case',
        'QuitCase'
    ).convert_exceldata_testdata()

    @unittest.skipIf(test_class_data['test_quit']['isnot'], '条件为真跳过')
    def test_quit(self):
        # 读测试方法数据
        test_function_data = self.test_class_data['test_quit']
        self._testMethodDoc = test_function_data['test_name'] # self._testMethodDoc 测试方法备注

        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()  # 默认登录
        quit_action = QuitAction(main_page.driver)
        login_page = quit_action.quit()  # 退出回到登录页面
        actual = login_page.get_title()
        self.assertEqual(actual.__contains__(test_function_data['excepted_result']), True, "测试用例执行失败")


if __name__ == "__main__":
    unittest.main()
