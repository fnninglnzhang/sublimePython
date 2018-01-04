# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page

class Important_noticePage(Page):

	url = '/index.action'
	pppigtongzhi_popup_text = (By.CLASS_NAME, 'closeBtn')

	def pppigtongzhi_Popup(self):
		self.find_element(self.pppigtongzhi_popup_text).click()

	def pppignotice_Action(self):
		self.pppigtongzhi_Popup()