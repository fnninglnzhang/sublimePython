#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_important_notice_page import Important_noticePage
from page_object.mail_page import MailPage

class Important_noticeTest(myunit.MyTest):

	def test_important_notice_close(self):
		"""点击关闭重要通知"""
		po = Important_noticePage(self.driver)
		sleep(2)
		po.open()
		sleep(2)
		po.pppignotice_Action()
		function.insert_img(self.driver, "closenotice1.jpg")

