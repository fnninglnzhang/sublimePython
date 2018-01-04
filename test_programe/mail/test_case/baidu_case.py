#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.baidu_page import BaiduPage
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

	def test_login_user_pwd_null(self):
		'''用户名、密码为空登录'''
		po = BaiduPage(self.driver)
		po.open()
		sleep(2)
		po.baidu_Aboutbaidu_Action()
		sleep(2)
		function.insert_img(self.driver, 'baidu_Aboutbaidu.jpg')

