# 测试用例类的前置后置

import unittest


class testDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 测试类的前置
        cls.num = 1
        print('setUpClass')

    def setUp(self):  # 测试方法的前置
        print('setUp %d' % self.num)

    @classmethod
    def tearDownClass(cls):  # 测试类的后置
        print('tearDownClass')

    def tearDown(self):  # 测试方法的后置
        print('tearDown')

    def test01(self):
        print("test01_%d" % self.num)
        self.assertTrue(True)

    def test02(self):
        print("test02")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
