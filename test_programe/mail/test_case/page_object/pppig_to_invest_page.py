# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium import webdriver

class To_invest(Page):
	# url = '/recommendloanDetail?loanId=35416'
	# 我要出借
	pppigI_want_to_invest_text = (By.XPATH, ".//*[@id='munue_2']/a")
	# 出借债权
	pppigon_sale_investment_text = (By.XPATH, ".//*[@id='listform']/div[1]/div[1]/div[1]/ul/li[3]/a")
	# 立即投标
	pppigbuy_it_now_text = (By.XPATH, ".//*[@id='listform']/div[1]/div[2]/div[3]/div[1]/div[2]/span[2]")
	# 投资金额
	pppiginvestment_Amount_text = (By.ID, 'sideInput')
	# 去选择红包和加息券
	pppiguse_car_text = (By.ID, 'hongbaojiaxi')


	# 使用红包
	pppiguse_red_packet_text = (By.XPATH, "html/body/div[8]/div/div[3]/div[1]/div/ul/li[1]/span[5]/input")

	# 使用加息券
	pppiguse_rate_coupon_text = (By.XPATH, ".//*[@id='active_ul']/li[1]/span[5]/input")

	# 确定使用
	pppigenteruse_coupon_text = (By.XPATH, ".//*[@id='wxy_submit']/input")


	# 即刻投标
	pppigbuy_it_now_button_text = (By.ID, 'daojishi')
	# 验证码
	pppiginvest_verifycode_text = (By.ID, 'verifycode')
	# 同意协议
	pppigagree_three_protocol_text = (By.NAME,'agreementxieyi')
	# 确认标的信息
	pppigmake_sure_invest_text = (By.ID, 'invest_btn')
	# 江西交易密码
	pppigjx_transaction_password_text = (By.ID, 'pass')
	# 确认投标
	pppigmake_sure_jx_transaction_password_button_text = (By.ID, 'sub')

	def pppig_To_invest(self):
		self.find_element(*self.pppigI_want_to_invest_text).click()

	# 出借债权
	def pppigon_Sale_investment(self):
		self.find_element(*self.pppigon_sale_investment_text).click()

	# 立即投标
	def pppigbuy_It_now(self):
		self.find_element(*self.pppigbuy_it_now_text).click()

	# 投资金额
	def pppiginvestment_Amount(self, text):
		self.find_element(*self.pppiginvestment_Amount_text).send_keys(text)

	# 去选择红包和加息券
	def pppiguse_card(self):
		self.find_element(*self.pppiguse_car_text).click()

	# 选择红包
	"""
	def pppiguse_red_packet(self):
		redpacket = self.find_element(*self.pppiguse_red_packet_text).click()
		self.driver.execute_script("arguments[0].scrollIntoView();", redpacket)
	"""

	def pppiguse_red_packet(self):
		self.find_element(*self.pppiguse_red_packet_text).click()
	# 选择加息券
	"""
	def pppiguse_rate_coupon(self):
		ratecoupon = self.find_element(*self.pppiguse_rate_coupon_text)
		self.driver.execute_script("arguments[0].scrollIntoView();", ratecoupon).click()
	"""

	def pppiguse_rate_coupon(self):
		self.find_element(*self.pppiguse_rate_coupon_text).click()
	# 确定使用卡券
	def pppigenteruse_coupon(self):
		self.find_element(*self.pppigenteruse_coupon_text).click()



	# 即刻投标
	def pppiginvestment_Amount_button(self):
		self.find_element(*self.pppigbuy_it_now_button_text).click()

	# 验证码
	def pppiginvest_Verifycode(self, text):
		self.find_element(*self.pppiginvest_verifycode_text).send_keys(text)

	# 同意协议
	def pppigagree_Three_protocol(self):
		self.find_element(*self.pppigagree_three_protocol_text).click()

	# 确认标的信息
	def pppigmake_Sure_invest(self):
		self.find_element(*self.pppigmake_sure_invest_text).click()

	# 江西交易密码
	def pppigjx_Transaction_password(self, text):
		self.find_element(*self.pppigjx_transaction_password_text).send_keys(text)

	# 确认投标
	def pppigmake_Sure_jx_transaction_password_button(self):
		self.find_element(*self.pppigmake_sure_jx_transaction_password_button_text).click()

	def pppiginvest_Action(self, investment_smount, invest_verifycode, jx_transaction_password,):
		self.pppig_To_invest()
		self.pppigon_Sale_investment()
		self.pppigbuy_It_now()
		self.pppiginvestment_Amount(investment_smount)
		self.pppiginvestment_Amount_button()
		self.pppiginvest_Verifycode(invest_verifycode)
		self.pppigagree_Three_protocol()
		self.pppigmake_Sure_invest()
		self.pppigjx_Transaction_password(jx_transaction_password)
		self.pppigmake_Sure_jx_transaction_password_button()

	# 我要出借-出借债券_立即投标
	def pppiginvest_Action1(self):
		self.pppig_To_invest()
		self.pppigon_Sale_investment()
		self.pppigbuy_It_now()

	# 投资金额
	def pppiginvest_Action2(self, investment_smount):
		self.pppiginvestment_Amount(investment_smount)
		self. pppiginvestment_Amount_button()

	# 验证码
	def pppiginvest_Action3(self, invest_verifycode):
		self.pppiginvest_Verifycode(invest_verifycode)
		self.pppigagree_Three_protocol()
		self.pppigmake_Sure_invest()

	# 江西确定投资
	def pppiginvest_Action4(self, jx_transaction_password):
		self.pppigjx_Transaction_password(jx_transaction_password)
		self.pppigmake_Sure_jx_transaction_password_button()

	# 投资金额——使用红包——即刻投资
	def pppiguse_Redpacket_Invest_Action(self, text):
		self.pppiginvestment_Amount(text)
		self.pppiguse_card()
		self.pppiguse_red_packet()
		self.pppigenteruse_coupon()
		self.pppiginvestment_Amount_button()


	# 使用加息券
	def pppiguse_ratecoupon_Invest_Action(self, text):
		self.pppiginvestment_Amount(text)
		self.pppiguse_card()
		self.pppiguse_rate_coupon()
		self.pppigenteruse_coupon()
		self.pppiginvestment_Amount_button()
