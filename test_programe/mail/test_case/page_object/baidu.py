# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
class Page(object):
	def __init__(self, driver, base_url='https://www.baidu.com'):
		self.driver = driver
		self.base_url = base_url
		self.timeout = 30

	def _open(self, url):
		url_ = self.base_url + url
		self.driver.maximine_window()
		self.driver.get(url_)
		sleep(2)
		assert self.driver.current_url == url_, 'Did ont land on %s' % url_


# if __name__ == "__main__":

