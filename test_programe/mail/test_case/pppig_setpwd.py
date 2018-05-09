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
		pologin.pppiglogin_noclose_Action('15647510953', '111111')
		sleep(1)
		# 设置交易密码
		poset_transaction_password = SetTransactionPWD(self.driver)
		sleep(2)
		poset_transaction_password.pppigset_Transaction_password_Action('111111', '111111')
		sleep(10)







# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
