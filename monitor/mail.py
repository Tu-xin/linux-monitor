#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib  # 发送邮件
from email.mime.text import MIMEText  # 构造纯文本邮件
from email.utils import formataddr # 格式化邮件地址


def structural_mail(text, recipient):
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = formataddr(["涂鑫", '974038517@qq.com'])  # 发件人
    msg['To'] = formataddr([recipient, recipient])  # recipient收件人
    msg['Subject'] = "监控报警"  # 主题
    return msg


def send_mail(text, recipient):
    from_addr = '974038517@qq.com'
    password = 'iijpofxaxznwbffb'
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    to_addr = []  # 可以一次发给多个人,因此传入一个列表
    to_addr.append(recipient)
    msg = structural_mail(text, recipient)
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)   #服务器和端口
    server.login(from_addr, password)     
    server.sendmail(from_addr, to_addr, msg.as_string())   
'''
def check():
    if cpuUsed <= 80 or diskUsed >= 7:
       send_mail('CPU使用率：{}%，磁盘使用率：{}%'.format(cpuUsed, diskUsed),'wstxach123@email.swu.edu.cn')
    else:
        pass

'''