# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from selenium.webdriver.support.ui import WebDriverWait as Wa
from selenium.webdriver.support import expected_conditions as Ec



class HoutaiPage(object):
	def __init__(self, driver, base_url='https://mgtt.pangpangpig.com'):
		self.driver = driver
		self.base_url = base_url
		self.timeout = 30

	def _open(self, url):
		url_a = self.base_url + url
		self.driver.maximize_window()
		self.driver.get(url_a)
		# sleep(2)
		assert self.driver.current_url == url_a, 'Did ont land on %s' % url_a

	def open_R(self, url_invest):
		url_I = self.base_url + url_invest
		self.driver.get(url_I)


	def open(self):
		self._open(self.url)

	# *参数个数不是固定的（By.ID, 'kw'）
	# 重写元素定位方法
	def find_element(self, *loc):
		# 元祖接收多余的参数，预防程序报错，把多余的存起来
		return self.driver.find_element(*loc)

	# 重写switch_frame方法
	def switch_frame(self, loc):
		return self.driver.switch_to_frame(loc)

	# 使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
	def on_page(self, pagetitle):
		return pagetitle in self.driver.title

	# 定义script方法，用于执行js脚本，范围执行结果
	def script(self, src):
		self.driver.execute_script(src)

	# 重写定义send_keys方法
	def send_keys(self, loc, vaule, clear_first=True, click_first=True):
		try:
			loc = getattr(self, "_%s" % loc)                                # loc  定位到的元素    value发送的内容   click_first 是否要单击设置焦点  clear_first是否需要先清除内容
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				self.find_element(*loc).clear()
			self.find_element(*loc).send_keys(vaule)
		except AttributeError:
			print(u"%s 页面中未能找到 %s 元素" % (self, loc))

"""
	if __name__ == "__main__":
		unittest.main()
"""





