# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium import webdriver
from page_object.pppig_login_page import LoginPage

class Recharge(Page):
	url = '/rechargeUI#recharge'
	# 我的账户
	pppigmy_account_button_text = (By.XPATH, ".//*[@id='indexPPPig']/div[2]/div/a")
	# 充值
	pppigacount_recharge_button_text = (By.XPATH, ".//*[@id='account-main']/div[1]/div[1]/div/div/a[1]")
	# 快捷充值
	pppigrapid_recharge_button_text = (By.XPATH, ".//*[@id='cz']/ul/li[1]")
	# 支付宝充值
	pppigalipay_recharge_button_text = (By.XPATH, ".//*[@id='cz']/ul/li[2]")
	# 转账充值
	pppigtransfer_recharge_button_text = (By.XPATH, ".//*[@id='cz']/ul/li[3]")
	# 充值金额
	pppigcash_recharge_amount_text = (By.ID, 'rechargeMoney')
	# 获取短信验证码按钮
	pppigrecharge_code_button_text = (By.ID, 'btn_countdown_recharge_fast')
	# 短信验证码
	pppigrecharge_code_number_text = (By.ID, 'yzmFast')
	# 立即充值
	pppigrecharge_at_once_button_text = (By.ID, "startRecharge")
	# 需要处理alert
	# 点击确定
	pppigalertenter_button_text = (By.XPATH, ".//*[@id='layui-layer3']/div[3]/a")



	# 把每一个元素封装成一个方法
	# 我的账户
	def pppigmy_account_button(self):
		self.find_element(*self.pppigmy_account_button_text).click()

	# 账户充值
	def pppigacount_recharge_button(self):
		self.find_element(*self.pppigacount_recharge_button_text).click()

	# 快速充值
	def pppigrapid_recharge_button(self):
		self.find_element(*self.pppigrapid_recharge_button_text).click()

	# 支付宝充值
	def pppigalipay_recharge_button(self):
		self.find_element(*self.pppigalipay_recharge_button_text).click()

	# 转账充值
	def pppigtransfer_recharge_button(self):
		self.find_element(*self.pppigtransfer_recharge_button_text).click()

	# 充值金额
	def pppigcash_recharge_amount(self, text):
		self.find_element(*self.pppigcash_recharge_amount_text).send_keys(text)

	# 获取短信验证码按钮
	def pppigrecharge_code_button(self):
		self.find_element(*self.pppigrecharge_code_button_text).click()


	"""
	这个没用，加等待就可以解决
	# 手动输入验证码
	def pppigsubmit_applications_button(self):
		self.find_element(*self.pppigrecharge_code_number_text).input()
	"""


	# 立即充值
	def pppigrecharge_at_once_button(self):
		self.find_element(*self.pppigrecharge_at_once_button_text).click()

	# 处理alert点击确定
	def pppigalertenter_button(self):
		self.find_element(*self.pppigalertenter_button_text)
		self.driver.switch_to_alart().accept()



	# 充值
	def recharge1_Action(self, amount):
		self.pppigmy_account_button()
		self.pppigacount_recharge_button()
		self.pppigcash_recharge_amount(amount)
		self.pppigrecharge_code_button()

	def recharge2_Action(self):
		self.pppigrecharge_at_once_button()
		self.pppigalertenter_button()