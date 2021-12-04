# ini 配置文件读取二次封装
import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '../config/config.ini')


class ConfigUtils(object):
    def __init__(self, path=config_path):
        self.cig = configparser.ConfigParser()
        self.cig.read(path, encoding='utf-8')

    @property
    def get_url(self):
        value = self.cig.get('default', 'URL')
        return value

    @property
    def get_driver_path(self):
        value = self.cig.get('default', 'driver_path')
        return value

    @property
    def driver_name(self):
        value = self.cig.get('default', 'driver_name')
        return value

    @property
    def element_info_path(self):
        value = self.cig.get('default', 'element_info_path')
        return value

    @property
    def time_out(self):
        value = float(self.cig.get('default', 'time_out'))
        return value

    @property
    def screent_shot_path(self):
        value = self.cig.get('default', 'screent_shot_path')
        return value

    @property
    def user_name(self):
        value = self.cig.get('default', 'user_name')
        return value

    @property
    def pass_word(self):
        value = self.cig.get('default', 'pass_word')
        return value

    @property
    def log_path(self):
        value = self.cig.get('default', 'log_path')
        return value

    @property
    def log_level(self):
        value = int(self.cig.get('default', 'log_level'))
        return value

    @property
    def testdata_path(self):
        value = self.cig.get('default', 'testdata_path')
        return value

    @property
    def case_path(self):
        value = self.cig.get('default', 'case_path')
        return value

    @property
    def report_path(self):
        value = self.cig.get('default', 'report_path')
        return value

    @property
    def smtp_server(self):
        value = self.cig.get('email', 'smtp_server')
        return value

    @property
    def smtp_sender(self):
        value = self.cig.get('email', 'smtp_sender')
        return value

    @property
    def smtp_senderpassword(self):
        value = self.cig.get('email', 'smtp_senderpassword')
        return value

    @property
    def smtp_receiver(self):
        value = self.cig.get('email', 'smtp_receiver')
        return value

    @property
    def smtp_cc(self):
        value = self.cig.get('email', 'smtp_cc')
        return value

    @property
    def smtp_subject(self):
        value = self.cig.get('email', 'smtp_subject')
        return value



local_config = ConfigUtils()  # 创建一个配置工具类的对象

if __name__ == "__main__":
    print(local_config.get_url)
    print(local_config.get_driver_path)
    print(local_config.driver_name)
    print(local_config.element_info_path)
    print(local_config.time_out)
    print(local_config.screent_shot_path)
    print(local_config.user_name)
    print(local_config.pass_word)
    print(local_config.log_path)
    print(local_config.log_level)
    print(local_config.testdata_path)
    print(local_config.case_path)
    print(local_config.report_path)
    print(local_config.smtp_server)
    print(local_config.smtp_subject)
    print(local_config.smtp_sender)
    print(local_config.smtp_receiver)
    print(local_config.smtp_cc)
    print(local_config.smtp_senderpassword)
