#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_recharge_page import Recharge
from page_object.pppig_set_transaction_password_page import SetTransactionPWD
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class RechargeTest(myunit.MyTest):
	def test_login_success(self):
		'''参数化、用户名、密码正确,登录成功'''
		try:
			f = open('../date/recharge.txt')
			lines = f.readlines()
			for line in lines:
				username = line.split(',')[0]
				password = line.split(',')[1]
				pologin = LoginPage(self.driver)
				pologin.open()
				sleep(1)
				pologin.pppiglogin_noclose_Action(username, password)
				sleep(2)
				porecharge = Recharge(self.driver)
				# 充值 -- 充值金额 -- 获取短信验证码按钮
				amount = '2'
				porecharge.recharge1_Action(amount)
				# 手动输入验证码
				sleep(15)
				# 立即充值
				porecharge.recharge2_Action()
				sleep(5)
				print(username+'用户充值成功')
				function.insert_img(self.driver, "pppig_recharge_success.png")
				sleep(1)
				pologout = LoginPage(self.driver)
				pologout.pppiglogin_close_button()
				sleep(1)
				pologout.pppiglogin_close_button()
		except BaseException as e:
			print(e)






# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
