#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys

from model.log import log
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
		f = open('../date/recharge/recharge2.txt')
		lines = f.readlines()
		for line in lines:
			username = line.split(',')[0]
			# password = line.split(',')[1]
			pologin = LoginPage(self.driver)
			pologin.open()
			sleep(1)
			pologin.pppiglogin_noclose_Action(username, '111111')
			sleep(2)
			porecharge = Recharge(self.driver)
			# 充值 -- 充值金额 -- 立即充值
			# amount = '9000000'
			amount = '1'
			porecharge.recharge1_Action(amount)
			# 江西充值页面_已加入手动输入验证码
			sleep(1)
			porecharge.jx_recharge_Action('111111')
			sleep(2)
			logger_info = log()
			logger_info.setMSG('info', "username = {}充值成功".format(username))
			print("username = {}充值成功".format(username))
			pologout = LoginPage(self.driver)
			pologout.pppiglogin_close_button()
			sleep(1)



# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
