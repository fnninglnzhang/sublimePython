#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.login_page import LoginPage
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):
	def test_login_pwd_null(self):
		'''密码为空登录'''
		po = LoginPage(self.driver)
		po.open()
		po.login_action('abc', '')
		# sleep(2)
		po.wait_presence_of_element_located("请输入密码")
		# self.assertEqual(po.login_error_hint(),'请输入密码')
		function.insert_img(self.driver, 'pwd_null.jpg')
