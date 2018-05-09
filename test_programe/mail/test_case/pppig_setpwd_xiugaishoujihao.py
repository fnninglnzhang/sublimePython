#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_recharge_page import Recharge
from page_object.pppig_set_transaction_password_page import SetTransactionPWD
from page_object.mail_page import MailPage
from pppig_modify_phone_number_page import Modify_cellphone_Page

class Setpwd_changmblTest(myunit.MyTest):
	def test_setpwd_changembl(self):
		u'''设置交易密码，修改手机号'''
		pologin = LoginPage(self.driver)
		pologin.open()
		username = 15110867276
		pologin.pppiglogin_noclose_Action(username, '111111')
		sleep(1)
		# 设置交易密码
		poset_transaction_password = SetTransactionPWD(self.driver)
		sleep(2)
		poset_transaction_password.pppigset_Transaction_password_Action('111111', '111111')
		sleep(10)
		pomodifyphone = Modify_cellphone_Page(self.driver)
		pomodifyphone.pppigmodify_phone_Action('15120080522', username)







# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
