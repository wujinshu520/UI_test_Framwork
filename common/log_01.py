# 日志工具包
import logging
import os

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '../logs/test.log')


class LogUtils(object):
    def __init__(self, log_path=log_path):
        self.log_path = log_path
        self.logger = logging.getLogger(__name__)  # 创建日志对象
        self.logger.setLevel(level=logging.INFO)  # 设置日志级别

        # 创建一个文件类型的日志对象
        file_log = logging.FileHandler(self.log_path)
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self, message):  # 写入正常的日志信息
        self.logger.info(message)

    def error(self, message):  # 写入错误的日志信息
        self.logger.error(message)


# 优化日志，添加一个logger对象
logger = LogUtils()

if __name__ == '__main__':
    Log_Utils = LogUtils()
    Log_Utils.error('错误咯！！')
