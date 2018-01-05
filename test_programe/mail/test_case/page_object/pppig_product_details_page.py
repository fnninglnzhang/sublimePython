# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium import webdriver

class Product_details(Page):
	pppiginvestment_Amount_text = (By.ID, 'sideInput')
	pppigbuy_it_now_button_text = (By.ID, 'daojishi')

	def pppiginvestment_Amount(self, text):
		self.find_element(*self.pppiginvestment_Amount_text).send_keys(text)

	def pppiginvestment_Amount_button(self):
		self.find_element(*self.pppigbuy_it_now_button_text).click()

	def product_Details_Action(self, investment_smount):
		self.pppiginvestment_Amount(investment_smount)
		self.pppiginvestment_Amount_button()

