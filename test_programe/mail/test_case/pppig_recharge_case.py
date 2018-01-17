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
		pologin = LoginPage(self.driver)
		pologin.open()
		sleep(1)
		pologin.pppiglogin_noclose_Action('13011111101', '111111')
		porecharge = Recharge(self.driver)
		"""
		# 充值
		porecharge.pppigacount_recharge_button()
		# 充值金额
		porecharge.pppigcash_recharge_amount('1')
		# 获取短信验证码按钮
		porecharge.pppigrecharge_code_button()
		sleep(10)
		# 手动输入验证码
		# porecharge.pppigsubmit_applications_button()
		# sleep(5)
		# 立即充值
		porecharge.pppigrecharge_at_once_button()
		"""
		porecharge.recharge1_Action('1')
		sleep(10)
		porecharge.recharge2_Action()





# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
