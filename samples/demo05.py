# encoding: utf-8
# @author: wujinshu
# @file: demo05.py
# @time:2021/10/16 14:14
# @desc: mail_demo
import os
import smtplib
from email.mime.text import MIMEText

current_path = os.path.abspath(os.path.dirname(__file__))
dir_path = os.path.join(current_path, '..', 'reports/禅道自动化测试报告V1.0/禅道自动化测试报告V1.0.zip')
print(dir_path)

smtp_server = "smtp.qq.com"  # 邮件服务器地址
smtp_sender = "wujinshu1314@foxmail.com"  # 邮箱名
smtp_senderpassword = "wujinshu@zj1995"  # 授权码
smtp_receiver = "wujinshu1314@foxmail.com"  # 收件人
smtp_cc = "1964855301@qq.com"  # 抄送人
smtp_subject = "自动化测试报告（测试版）"  # 邮件主题
smtp_body = "来自python邮件测试"  # 邮件正文

# 邮件消息体
msg = MIMEText(smtp_body, "html", "utf-8")  # 邮件信息对象
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_senderpassword)
smtp.sendmail(smtp_senderm, smtp_receiver.split(',') + smtp_cc.split(','), msg.as_string())
