# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class Page(object):
	def __init__(self, driver, base_url='https://t.pangpangpig.com'):
		self.driver = driver
		self.base_url = base_url
		self.timeout = 30

	def _open(self, url):
		url_a = self.base_url + url
		self.driver.maximize_window()
		self.driver.get(url_a)
		sleep(2)
		assert self.driver.current_url == url_a, 'Did ont land on %s' % url_a

	def open(self):
		self._open(self.url)




"""
	if __name__ == "__main__":
		unittest.main()
"""





