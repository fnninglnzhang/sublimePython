# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium.webdriver.support.ui import WebDriverWait as Wa
from selenium.webdriver.support import expected_conditions as Ec


#页面对象（PO）登录页面
class Jx_Transaction_Password (Page):
	# 电子账户交易密码
	jx_electronic_account_trading_password = (By.ID, 'encPin')
	# 江西交易密码
	pppigjx_transaction_password_text = (By.ID, 'pass')
	# 确认投标
	pppigmake_sure_jx_transaction_password_button_text = (By.ID, 'sub')

	# 江西交易密码
	def pppigjx_Transaction_password(self, text):
		self.find_element(*self.pppigjx_transaction_password_text).send_keys(text)

	# 确认投标
	def pppigmake_Sure_jx_transaction_password_button(self):
		self.find_element(*self.pppigmake_sure_jx_transaction_password_button_text).click()

	# 等待
	def wait_presence_of_electronic_account_trading_password(self, jx_electronic_account_trading_password):
		try:
			return Wa(self.driver, 10, 0.5).until(Ec.presence_of_element_located(jx_electronic_account_trading_password))
		except Exception as e:
			print(e)
			print('未找到对应元素')

	# 江西确定投资
	def jx_Transaction_Password_Action(self, jx_transaction_password):
		# self.wait_presence_of_electronic_account_trading_password(element)
		self.pppigjx_Transaction_password(jx_transaction_password)
		self.pppigmake_Sure_jx_transaction_password_button()