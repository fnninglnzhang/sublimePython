# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium import webdriver


class To_investdebtcession(Page):
	pppigI_want_to_invest_text = (By.XPATH, ".//*[@id='munue_2']/a")
	# 出借债权
	pppigon_sale_investment_text = (By.XPATH, ".//*[@id='listform']/div[1]/div[1]/div[1]/ul/li[3]/a")
	# 债权转让
	pppigon_debt_cession_text = (By.XPATH, ".//*[@id='listform']/div[1]/div[1]/div[1]/ul/li[5]/a")
	pppigbuy_it_now_text = (By.XPATH, ".//*[@id='listform']/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/span[3]")
	# 同意协议
	# pppigagreement_button_text = (By.ID, 'buy')
	pppigagreement_button_text = (By.XPATH, ".//*[@id='buy']")
	# 江西页面交易密码
	pppigjx_transaction_password_text = (By.ID, 'pass')
	pppigmake_sure_jx_transaction_password_button_text = (By.ID, 'sub')

	# 我要出借
	def pppig_To_invest(self):
		self.find_element(*self.pppigI_want_to_invest_text).click()

	# 转让专区
	def pppigon_Debt_cession(self):
		self.find_element(*self.pppigon_debt_cession_text).click()

	# 认购
	def pppigbuy_It_now(self):
		self.find_element(*self.pppigbuy_it_now_text).click()

	# 同意协议
	def pppigagreement_button(self):
		self.find_element(*self.pppigagreement_button_text).click()

	# 江西交易密码
	def pppigjx_Transaction_password(self, text):
		self.find_element(*self.pppigjx_transaction_password_text).send_keys(text)

	def pppigmake_Sure_jx_transaction_password_button(self):
		self.find_element(*self.pppigmake_sure_jx_transaction_password_button_text).click()

	# def pppiginvest_Action1(self, investment_smount):
	def pppiginvestdebtcession_Action1(self):
		self.pppig_To_invest()
		self.pppigon_Debt_cession()
		self.pppigbuy_It_now()

	def pppiginvestdebtcession_Action2(self):
		self.pppigagreement_button()

	def pppiginvestdebtcession_Action3(self, jx_transaction_password):
		self.pppigjx_Transaction_password(jx_transaction_password)
		self.pppigmake_Sure_jx_transaction_password_button()
