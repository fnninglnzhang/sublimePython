#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest, time
# from HTMLTestRunner import HTMLTestRunner
from MyHTMLTestReportCN import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib,os
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
"""
def send_mail(file_new):
	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()
	msg = MIMEText(mail_body, 'html', 'utf-8')
	msg['Subject'] = Header("自动化测试报告", 'utf-8')
	msg['From'] = '17310520712@163.com'
	msg['To'] = '17310520712@163.com'
	smtp = smtplib.SMTP()
	smtp.connect("smtp.163.com")
	smtp.login("17310520712@163.com", "1989tq==C")
	smtp.sendmail("17310520712@163.com", "17310520712@163.com", msg.as_string())
	smtp.quit()
	print('email has send out!')
"""
# 发送测试报告，需要配置你的邮箱账号
def send_mail(file_new):
	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()
	msg = MIMEText(mail_body, 'html', 'utf-8')
	msg['Subject'] = Header("自动化测试报告", 'utf-8')
	msg['From'] = 'oyellow6@163.com'
	msg['To'] = '2513953126@qq.com'
	smtp = smtplib.SMTP()
	smtp.connect("smtp.163.com")
	smtp.login("oyellow6@163.com", "qwer1234")
	smtp.sendmail("oyellow6@163.com", "2513953126@qq.com", msg.as_string())
	smtp.quit()
	print('email has send out!')


# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
	file_new = os.path.join(testreport, lists[-1])
	print(file_new)
	return file_new


# 指定测试用例为当前文件夹下的test_case目录
test_dir = './mail/test_case'
# test_report = 'F:\\work\\python\\python\\sublimePython\\test_programe\\mail\\report'
test_report = 'e:\\python\\demo\\sublimePython\\test_programe\\mail\\report'
"""找到test_dir目录下所有的******——case的文件并执行
以通过文件的名称来判断是否为测试用例文件，如为用例文件则自动添加到测试套件中
"""
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_case.py')

if __name__ == "__main__":
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = test_report + '\\' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = unittest.TextTestRunner()
	runner = HTMLTestRunner(stream=fp,
	                        title='测试报告',
	                        description="运行环境：windows 10, Chrome")
	runner.run(discover)
	fp.close()

	new_report = new_report(test_report)
	send_mail(new_report)
