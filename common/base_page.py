# 基本页面类
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from common.log_01 import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common.config_untils import local_config
from selenium.webdriver.common.action_chains import ActionChains
from common.log_untils import logger
from common import HTMLTestReportCN


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        # self.chains = ActionChains(self.driver)

    # 浏览器操作
    def open_url(self, url):
        try:
            self.driver.get(url)
            logger.info("打开URL地址%s" % url)
        except Exception as e:
            logger.error("不能打开指定的测试网址，原因是：%s" % e.__str__())

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info("浏览器最大化")

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info("浏览器最小化")

    # implicitlyWait() 可以在一个时间范围内等待，称为隐式等待
    def implicitly_Wait(self, seconds=local_config.time_out):
        self.driver.implicitly_wait(seconds)

    def refresh(self):
        self.driver.refresh()
        logger.info("浏览器刷新")

    def get_title(self):
        title = self.driver.title
        logger.info("获取网页标题，标题为%s" % title)
        return title

    def get_url(self):
        url = self.driver.current_url
        logger.info("获取网页网址，网址为%s" % url)
        return url

    def exit_quit(self):
        # time.sleep(3)
        self.wait(6)
        self.driver.quit()
        logger.info("关闭浏览器")

    def close_table(self):
        self.wait(6)
        self.driver.close()
        logger.info("关闭当前的tab页")

    # 元素识别封装  目的：传入一个元素的识别数据，返回一个元素
    # 控件的元素名称：element_name（ username_inputbox ）
    # 元素识别方法：locator_type（ By.XPATH ）
    # 定位信息：locator_value （ '//input[@name="account"]' ）
    # 识别元素超时时间：timeout
    def find_element(self, element_info):
        """
        根据参数中提供的element_info 信息进行元素查找
        :param element_info: 元素信息，字典类型{}
        :return: element 对象
        """
        try:
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['timeout']
            if locator_type_name == 'id':
                locator_type = By.ID
            elif locator_type_name == 'class':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'xpath':
                locator_type = By.XPATH
            elif locator_type_name == 'css':
                locator_type = By.CSS_SELECTOR
            element = WebDriverWait(self.driver, locator_timeout).until(lambda x:
                                                                        x.find_element(locator_type,
                                                                                       locator_value_info))
            logger.info("[%s]元素识别成功" % element_info["element_name"])
        except Exception as e:
            logger.error("[%s]不能识别成功" % element_info["element_name"])
            # 元素识别错误截图
            self.screentshot_as_file()
        return element

    # 封装元素操作方法
    def click(self, element_info):
        element = self.find_element(element_info)
        try:
            element.click()
            logger.info('[%s]元素进行了点击操作' % element_info["element_name"])
        except Exception as e:
            logger.info('[%s] 元素点击操作失败，原因是%s' % (element_info["element_name"],
                                                 e.__str__()))

    def input(self, element_info, content):  # content：输入内容
        element = self.find_element(element_info)
        try:
            element.send_keys(content)
            logger.info('[%s]元素输入数据:%s' % (element_info["element_name"], content))
        except Exception as e:
            logger.info('[%s] 元素输入数据，原因是%s' % (element_info["element_name"],
                                               e.__str__()))

    # 获取文本信息
    def get_text(self, element_info):
        element = self.find_element(element_info)
        text = element.text
        logger.info("获取[%s]元素的文本信息：%s" % (element_info['element_name'], text))
        return element.text

    # 鼠标操作封装
    #  move_to_element() : 鼠标移动到一个元素上
    # time.sleep(2)
    # el = driver.find_element_by_name('tj_settingicon')
    # ActionChains(driver).move_to_element(el).preform()

    # 鼠标悬停
    def move_to_element_by_mouse(self, element_info):
        self.wait(3)
        element = self.driver.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    # 鼠标双击
    def double_click_by_mouse(self, element_info):
        element = self.driver.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()

    # 鼠标右击
    def right_click_element(self, element_info):
        element = self.driver.find_element(element_info)
        ActionChains(self.driver).context_click(element).perform()

    # 键盘的封装
    def control_v(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    # 鼠标封装方法2：不推荐使用
    # def move_to_element_by_mouse2(self, element_info):
    #     self.wait(2)
    #     element = self.driver.find_element(element_info)
    #     self.chains.move_to_element(element).perform()

    # 封装切框架
    # 思路1：通过元素来切
    def swith_to_frame(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 思路2：通过id 或者name来切
    def switch_to_frame_id_or_name(self, id_or_name):
        self.driver.switch_to.frame(id_or_name)

    def swirch_to_frame_by_element(self, element_info):
        element = self.driver.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 思路3：灵活处理，把识别的方式做成收集参数
    # id = frameid name = framename element = element_info
    def switch_to_frame(self, **element_dict):
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.driver.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)

    # 提示框的处理
    # 封装方法1：
    # def switch_to_alert(self, action='accept', time_out=local_config.time_out):
    #     self.wait(2)
    #     alert = self.driver.switch_to.alert  # 提示框对象
    #     alert_text = alert.txt
    #     if action == 'accept':
    #         alert.accept()
    #     else:
    #         alert.dismiss()
    #     return alert_text
    # 思考： 如果页面上没有提示框，是不是就不能操作，必须有一个提示框才能操作
    # 加一个提示框断言，确定提示框存在再进行操作

    # 封装方法2：
    # 登录失败，返回提示框的内容
    def switch_to_alert(self, action='accept', time_out=local_config.time_out):
        # 判断页面上是否存在alert,如果有就切换到alert并返回alert的内容
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert  # 提示框对象
        alert_text = alert.text  # 提示框内容
        if action == 'accept':
            alert.accept()
        else:
            alert.dismiss()
        return alert_text

    # 多页面切换封装
    # 获取当前页面窗口句柄
    def get_windows_handle(self):
        return self.driver.current_window_handle

    # 切句柄
    def switch_to_window_by_handle(self, windows_handle):
        self.driver.switch_to.window(windows_handle)

    def switch_to_window_by_title(self, title):
        window_handles = self.driver.window_handles  # 先获取所有句柄
        for window_handle in window_handles:
            # if self.get_title() == title:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    def switch_to_window_by_url(self, url):
        window_handles = self.driver.window_handles  # 先获取所有句柄
        for window_handle in window_handles:
            # if self.get_url() == url:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    # js 操作封装
    # 步骤1：封装移除元素的value属性   封装设置元素的value属性
    # Js = 'arguments[0].removeAttribute("value");' # 移除元素的value 属性
    # Js = 'arguments[0].setAttribute("value","newdream");'  # 设置元素的value属性

    def delete_element_attribute(self, element_info, attribute_name):
        # element = self.driver.find_element(element_info)
        js = 'arguments[0].removeAttribute("%s");' % attribute_name
        # self.driver.execute_script(js, element)
        self.__execute_script(js, element_info)

    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        # element = self.driver.find_element(element_info)
        js = 'arguments[0].setAttribute("%s","%s");' % (attribute_name, attribute_value)
        # self.driver.execute_script(js, element)
        self.__execute_script(js, element_info)

    # 滚动条操作
    def school(self, heigh):
        js = "window.scrollBy(0," + str(heigh) + ")"
        # self.driver.execute_script(js)
        self.__execute_script(js)
        self.wait(3)
        # time.sleep(3)

    # 步骤2： 继续封装selenium 执行js的脚本
    def __execute_script(self, js_str, element_info=None):
        if element_info:
            element = self.driver.find_element(element_info)
            self.driver.execute_script(js_str, element)
        else:
            self.driver.execute_script(js_str)

    # 固定等待封装
    def wait(self, seconds=local_config.time_out):
        time.sleep(seconds)

    # 把截图放报告中
    def screentshot_as_file(self):
        report_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            '..',
            local_config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)

    # 错误截图封装
    def screentshot_as_file_old(self, *screentshot_path):
        if len(screentshot_path) == 0:  # 为0 ，没有给截图的地址
            screentshot_filepath = local_config.screent_shot_path
        else:
            screentshot_filepath = screentshot_path[0]
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        current_dir = os.path.dirname(__file__)
        screentshot_filepath = os.path.join(current_dir, '..',
                                            screentshot_filepath,
                                            'UItest_%s.png' % now)
        self.driver.save_screenshot(screentshot_filepath)
