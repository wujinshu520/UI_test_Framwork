# 第一条：登录用例
import unittest
from actions.login_action import LoginAction
from common.selenium_basc_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoginCase(SeleniumBaseCase):
    # 整个测试类的数据
    test_class_data = TestDataUtils(
        'login_suite',
        'login_case',
        'LoginCase'
    ).convert_exceldata_testdata()

    def setUp(self):  # 个性化设置
        super().setUp()  # 1、先继承父类的setUp

    @unittest.skipIf(test_class_data['test_login_success']['isnot'], "条件为真跳过")
    def test_login_success(self):
        # 根据用例的名称，读取相关数据
        test_function_data = self.test_class_data['test_login_success']
        self._testMethodDoc = test_function_data['test_name'] + str(
            test_function_data['isnot'])  # 测试方法说明

        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(
            test_function_data['test_parameter'].get('username'),
            test_function_data['test_parameter'].get('password')
        )

        self.assertEqual(
            main_page.get_username(),
            test_function_data['excepted_result'],
            'test02登录失败！')

    @unittest.skipIf(test_class_data['test_login_fail']['isnot'], "条件为真跳过")
    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']  # 测试方法说明

        login_action = LoginAction(self.base_page.driver)

        actual_result = login_action.login_fail(
            test_function_data['test_parameter'].get('username'),
            test_function_data['test_parameter'].get('password')
        )  # 错误的登录信息

        print("actual%s" % actual_result)
        self.assertEqual(
            actual_result, test_function_data['excepted_result']
        )


if __name__ == "__main__":
    unittest.main()
