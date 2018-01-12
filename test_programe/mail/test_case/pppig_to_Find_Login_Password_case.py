#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_to_Find_Login_Password_Page import ForgetPWD
from model.oldconnect_mysql import *

class FindPWD(myunit.MyTest):
# class FindPWD(ForgetPWD, SelectMySQL):
	def test_find_password(self):
		"""找回密码"""
		po = ForgetPWD(self.driver)
		po.open()
		po.toFindLoginPasswordPage_Action()
		po2 = SelectMySQL()
		po.toFindLoginPasswordForPhonePage1_Action("13011111101", "1111")
		a = po2.select_Data("select validCode from mobile_authen where mobile=13011111101 and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1")
		po.toFindLoginPasswordForPhonePage2_Action(a)
		po.findByValidCodeP("111111", "111111")

# 用于验证该脚本是否有效
if __name__ == "__main__":
	unittest.main()
