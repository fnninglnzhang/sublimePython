# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium import webdriver

class SetTransactionPWD(Page):
	# url = '/recommendloanDetail?loanId=35416'
	# 请设置账户交易密码文本
	pppigset_transaction_password_text = (By.XPATH, ".//*[@id='accountP_cont1']")
	# 请设置账户交易密码
	pppigset_transaction_password_button_text = (By.XPATH, "html/body/div[4]/div[3]/a")
	# 江西设置电子账户交易密码
	pppigjxset_transaction_password_text = (By.ID, 'encPin1')
	# 江西确定电子账户交易密码
	pppigenterjx_transaction_password_text = (By.ID, 'encPin2')
	# 确认设置
	pppigenter_button_text = (By.ID, 'sub')

	# 获取页面元素
	def pppigset_Transaction_password(self):
		return self.find_element(*self.pppigset_transaction_password_text)

	# 点击设置交易密码
	def pppigset_Transaction_password_button(self):
		self.find_element(*self.pppigset_transaction_password_button_text).click()

	# 设置电子账户交易密码
	def pppigjxset_transaction_password(self, text):
		self.find_element(*self.pppigjxset_transaction_password_text).send_keys(text)

	# 确定电子账户交易密码
	def pppigenterjx_Transaction_password(self, text):
		self.find_element(*self.pppigenterjx_transaction_password_text).send_keys(text)

	# 点击确认
	def pppigenter_button(self):
		self.find_element(*self.pppigenter_button_text).click()



	def pppigset_Transaction_password_Action(self, code1, code2):
		self.pppigset_Transaction_password_button()
		self.pppigjxset_transaction_password(code1)
		self.pppigenterjx_Transaction_password(code2)
		self.pppigenter_button()
