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
				# 充值 -- 充值金额 -- 立即充值
				amount = '9000000'
				porecharge.recharge1_Action(amount)
				# 江西充值页面_已加入手动输入验证码
				sleep(1)
				porecharge.jx_recharge_Action('111111')
				sleep(1)
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
