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
		'''充值'''
		# try:
		pologin = LoginPage(self.driver)
		pologin.open()
		pologin.pppiglogin_noclose_Action('13011111106', '111111')
		sleep(1)
		porecharge = Recharge(self.driver)
		# 充值 -- 充值金额 -- 获取短信验证码按钮
		porecharge.recharge1_Action('3')
		# 手动输入验证码
		sleep(15)
		# 立即充值
		# porecharge.recharge2_Action()
		# porecharge.pppigalertenter_button()
		# sleep(5)
		porecharge.pppigrecharge_at_once_button()
		sleep(1)
		print(porecharge.pppigrecharge_success())
		self.assertEquals(porecharge.pppigrecharge_success(), '充值成功' )
		print(porecharge.pppigrecharge_success())
		# function.insert_img(self.driver, "pppig_recharge_success.png")
		# except AssertionError as e:
		# 	print(e)






# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
