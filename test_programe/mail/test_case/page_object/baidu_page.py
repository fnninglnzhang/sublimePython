# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
from time import sleep
from base import Base

class BaiduPage(Base):

	url = '/duty/'
	baidu_aboutbaidu_text = (By.XPATH, 'html/body/center/div/div[1]/div[1]/a[2]')

	def baidu_Aboutbaidu(self):
		self.find_element(self.baidu_aboutbaidu_text).click()

	def baidu_Aboutbaidu_Action(self):
		self.baidu_Aboutbaidu()