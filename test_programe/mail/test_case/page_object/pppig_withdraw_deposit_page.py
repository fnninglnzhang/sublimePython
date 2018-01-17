# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from page_object.jx_transaction_password_page import Jx_Transaction_Password


# 提现的类
class Withdraw_Deposit(Page):
	url = '/rechargeUI#withdraw'
	# 我的账户
	pppigmy_account_button_text = (By.XPATH, ".//*[@id='indexPPPig']/div[2]/div/a")
	# 提现
	pppigccount_withdrawal_button_text = (By.XPATH, ".//*[@id='account-main']/div[1]/div[1]/div/div/a[2]")
	# 快速提现
	pppigrapid_withdrawal_button_text = (By.XPATH, ".//*[@id='cashForm']/div/a[1]")
	# 大额提现
	pppigwithdraw_deposits_button_text = (By.XPATH, ".//*[@id='cashForm']/div/a[1]")
	# 提现金额
	pppigcash_withdrawal_amount_text = (By.ID, 'withdrawMoney')
	# 输入银联卡号
	pppigeenter_the_unionpay_card_number_text = (By.ID, 'cardBankCnaps')
	# 提交申请
	pppigsubmit_applications_button_text = (By.XPATH, ".//*[@id='cashForm']/p[6]/button")
	# 江西交易密码
	pppigjx_transaction_password_text = (By.ID, 'encPin')
	# 确认投标
	pppigmake_sure_jx_transaction_password_button_text = (By.ID, 'sub')
	# 交易成功
	pppig_trade_successfully_text = (By.ID, 'succMsg')
	# 取现操作已执行
	pppig_anready_withdrawal_text = (By.CSS_SELECTOR, '.chianerpay-main>h2')


	# 把每一个元素封装成一个方法
	#我的账户
	def pppigmy_account_button(self):
		self.find_element(*self.pppigmy_account_button_text).click()
	# 账户提现
	def pppigccount_withdrawal_button(self):
		self.find_element(*self.pppigccount_withdrawal_button_text).click()
	# 快速提现
	def pppigrapid_withdrawal_button(self):
		self.find_element(*self.pppigrapid_withdrawal_button_text).click()
	# 大额提现
	def pppigwithdraw_deposits_button(self):
		self.find_element(*self.pppigwithdraw_deposits_button_text).click()
	# 提现金额
	def pppigcash_withdrawal_amount(self, text):
		self.find_element(*self.pppigcash_withdrawal_amount_text).send_keys(text)
	# 输入银联卡号
	def pppigeenter_the_unionpay_card_number(self, text):
		self.find_element(*self.pppigeenter_the_unionpay_card_number_text).send_keys(text)
	# 提交申请
	def pppigsubmit_applications_button(self):
		self.find_element(*self.pppigsubmit_applications_button_text).click()

	# 江西交易密码
	def pppigjx_Transaction_password(self, text):
		self.find_element(*self.pppigjx_transaction_password_text).send_keys(text)

	# 确认投标
	def pppigmake_Sure_jx_transaction_password_button(self):
		self.find_element(*self.pppigmake_sure_jx_transaction_password_button_text).click()

	# 交易成功
	def pppig_trade_successfully(self):
		return self.find_element(*self.pppig_trade_successfully_text)

	# 取现操作已执行
	def pppig_anready_withdrawal(self):
		return self.find_element(*self.pppig_anready_withdrawal_text)

	# 快速提现
	def rapid_Withdrawal_Action(self, amount):
		# self.pppigmy_account_button()
		self.pppigccount_withdrawal_button()
		# self.pppigrapid_withdrawal_button()
		self.pppigcash_withdrawal_amount(amount)
		self.pppigsubmit_applications_button()

	# 大额提现
	def withdraw_Deposits_In_large_amounts_Action(self, amount, card_number):
		self.pppigmy_account_button()
		self.pppigccount_withdrawal_button()
		self.pppigwithdraw_deposits_button()
		self.pppigcash_withdrawal_amount(amount)
		self.pppigeenter_the_unionpay_card_number(card_number)
		self.pppigsubmit_applications_button()

	# 江西确定投资
	def withdraw_Jx_Transaction_Password_Action(self, jx_transaction_password):
		self.pppigjx_Transaction_password(jx_transaction_password)
		self.pppigmake_Sure_jx_transaction_password_button()
