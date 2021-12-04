# encoding: utf-8
# @author: wujinshu
# @file: log_untils.py
# @time:2021/10/16 16:18
# @desc:写入日志文件
import logging
import os
import time
from common.config_untils import local_config

current_path = os.path.dirname(__file__)  # 当前路径
log_path = os.path.join(current_path, '..', local_config.log_path)


class LogUtil(object):
    def __init__(self, logger=None):
        self.log_name = os.path.join(log_path, 'UITest_%s.log' % time.strftime(
            '%Y_%m_%d'))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(local_config.log_level)  # 设置日志级别

        self.fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 追加模式  输出到文件
        self.fh.setLevel(local_config.log_level)
        self.ch = logging.StreamHandler()  # 输出到控制台
        self.ch.setLevel(local_config.log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d  [%(levelname)s] : %(message)s'
        )
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def get_log(self):
        return self.logger


logger = LogUtil().get_log()

if __name__ == "__main__":
    logger.debug("debug日志")
    logger.info("info日志")
    logger.warning("warning日志")
    logger.error("error日志")
    logger.critical("致命错误日志 ，critical日志")
