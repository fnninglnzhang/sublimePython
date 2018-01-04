# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from selenium.webdriver.support.ui import WebDriverWait as Wa
from selenium.webdriver.support import expected_conditions as Ec



class Page(object):
	def __init__(self, driver, base_url='https://t.pangpangpig.com'):
	# def __init__(self, driver, base_url='https://www.pangpangpig.com'):
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


# *参数个数不是固定的（By.ID, 'kw'）
	def find_element(self, *loc):
		# 元祖接收多余的参数，预防程序报错，把多余的存起来
		return self.driver.find_element(*loc)



"""
	if __name__ == "__main__":
		unittest.main()
"""





