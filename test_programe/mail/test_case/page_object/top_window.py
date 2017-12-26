# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from base import Base
class TopWindow(Base):
	url = "/"
	login_top_window = 'Top Window'
	login_top_window_text9 = (By.XPATH,'html/body/header/nav/a[9]')

	# 把每一个元素封装成一个方法
	def login_top(self):
		return self.find_element(*self.login_top_window_text9).text
