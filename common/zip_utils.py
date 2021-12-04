# encoding: utf-8
# @author: wujinshu
# @file: zip_utils.py
# @time:2021/10/23 14:45
# @desc:

import os
import zipfile


def zip_dir(dir_path, zip_path):
    """
    :param dir_path: 目标文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    """
    zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        file_path = root.replace(dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
        # 循环出一个个文件名
        for filename in filenames:
            zip.write(
                os.path.join(root, filename),
                os.path.join(file_path, filename)
            )
            zip.close()


current_path = os.path.abspath(os.path.dirname(__file__))
dir_path = os.path.join(current_path, '..', 'reports/禅道自动化测试报告V1.1')
smtp_file_path = os.path.join(current_path, '..', 'reports/禅道自动化测试报告zip')
zip_dir(dir_path, smtp_file_path)
