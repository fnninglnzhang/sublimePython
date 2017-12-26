#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.top_window import TopWindow
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')
class Top_9(myunit.MyTest):


	def test_top_9_txt(self):
		"""断言该字有没有"""
		po = TopWindow(self.driver)
		po.open()
		try:
			self.assertEqual(po.find_element(),'私人助理')
			print('私人助理')
		except AssertionError as e:
			print('错误')