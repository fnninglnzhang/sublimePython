# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium import webdriver

class To_invest(Page):
	pppigI_want_to_invest_text = (By.XPATH, ".//*[@id='munue_2']/a")
	# 出借债权
	pppigon_sale_investment_text = (By.XPATH, ".//*[@id='listform']/div[1]/div[1]/div[1]/ul/li[3]/a")
	pppigbuy_it_now_text = (By.XPATH, ".//*[@id='listform']/div[1]/div[2]/div[3]/div[1]/div[2]/span[2]")

	pppiginvestment_Amount_text = (By.ID, 'sideInput')
	pppigbuy_it_now_button_text = (By.ID, 'daojishi')

	pppiginvest_verifycode_text = (By.ID, 'verifycode')
	pppigagree_three_protocol_text = (By.NAME,'agreementxieyi')
	pppigmake_sure_invest_text = (By.ID, 'invest_btn')
	pppigjx_transaction_password_text = (By.ID, 'pass')
	pppigmake_sure_jx_transaction_password_button_text = (By.ID, 'sub')

	def pppig_To_invest(self):
		self.find_element(*self.pppigI_want_to_invest_text).click()

	def pppigon_Sale_investment(self):
		self.find_element(*self.pppigon_sale_investment_text).click()

	def pppigbuy_It_now(self):
		self.find_element(*self.pppigbuy_it_now_text).click()

	def pppiginvestment_Amount(self, text):
		self.find_element(*self.pppiginvestment_Amount_text).send_keys(text)

	def pppiginvestment_Amount_button(self):
		self.find_element(*self.pppigbuy_it_now_button_text).click()

	def pppiginvest_Verifycode(self, text):
		self.find_element(*self.pppiginvest_verifycode_text).send_keys(text)

	def pppigagree_Three_protocol(self):
		self.find_element(*self.pppigagree_three_protocol_text).click()

	def pppigmake_Sure_invest(self):
		self.find_element(*self.pppigmake_sure_invest_text).click()

	def pppigjx_Transaction_password(self, text):
		self.find_element(*self.pppigjx_transaction_password_text).send_keys(text)

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

	# def pppiginvest_Action1(self, investment_smount):
	def pppiginvest_Action1(self):
		self.pppig_To_invest()
		self.pppigon_Sale_investment()
		self.pppigbuy_It_now()
	def pppiginvest_Action2(self, investment_smount):
		self.pppiginvestment_Amount(investment_smount)
		self. pppiginvestment_Amount_button()

	def pppiginvest_Action3(self, invest_verifycode):
		self.pppiginvest_Verifycode(invest_verifycode)
		self.pppigagree_Three_protocol()
		self.pppigmake_Sure_invest()

	def pppiginvest_Action4(self, jx_transaction_password):
		self.pppigjx_Transaction_password(jx_transaction_password)
		self.pppigmake_Sure_jx_transaction_password_button()

