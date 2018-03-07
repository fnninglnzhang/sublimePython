#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_goRegister_page import GoRegister
from page_object.pppig_open_the_depository_page import Opendepository
from model.oldconnect_mysql import *



class RegisterTest(myunit.MyTest):

	def test_register_success(self):
		'''注册'''
		f = open('../date/onlyregister.txt')
		lines = f.readlines()
		for line in lines:
			username = line.split(',')[0]  # 取第一列用户名数据
			poRegister = GoRegister(self.driver)
			sleep(2)
			poRegistercode = SelectMySQL()
			poRegister.open()
			poRegister.goregisternoinvite1_Action(username, "111111", "1111")
			sleep(3)
			checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile={} and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1".format(username))
			poRegister.goregisternoinvite2_Action(checkCode)
			# 登出
			pologout = LoginPage(self.driver)
			pologout.pppiglogin_close_button()

			# function.insert_img(self.driver, "success.png")