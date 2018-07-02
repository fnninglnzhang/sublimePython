#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_withdraw_deposit_page import Withdraw_Deposit
from page_object.jx_transaction_password_page import Jx_Transaction_Password
from page_object.to_login_page import To_login
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

	def test_withdraw_deposit(self):
		'''登录后进行提现操作'''
		try:
			pologin = LoginPage(self.driver)
			pologin.open()
			username = '13011111101'
			pologin.pppiglogin_noclose_Action(username, "111111")
			sleep(1)
			powithdraw = Withdraw_Deposit(self.driver)
			sleep(2)
			amount = '1'
			powithdraw.rapid_Withdrawal_Action(amount)
			sleep(2)
			powithdraw.withdraw_Jx_Transaction_Password_Action('111111')
			sleep(10)

			# self.assertEqual(powithdraw.pppig_anready_withdrawal(), '取现操作已执行')
			function.insert_img(self.driver, "取现操作已执行.png")
			print('用户'+username+'提现'+amount+' 元'+'   提现操作已执行')
		except Exception as e:
			print(e)



# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
