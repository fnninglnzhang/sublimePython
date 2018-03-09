# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from model import *
from selenium import webdriver
import codecs

#页面对象（PO）登录页面
class Modify_cellphone_Page(Page):
	url = '/accountInstall'
	# 账户设置
	account_set_text = (By.XPATH, ".//*[@id='accountSideNav']/li[5]/a/span")
	# 更换第三方手机号
	pppigchange_three_cellphone_text = (By.XPATH, ".//*[@id='mobileModify1']/span/a")
	# 原手机号
	pppigold_cellphone_text = (By.XPATH, ".//*[@id='oldMobile']")
	# 新手机号
	pppignew_cellphone_text = (By.XPATH, ".//*[@id='newMobile']")
	# 修改
	pppigmodify_button_text = (By.XPATH, ".//*[@id='submitBtn']")
	# 立即修改
	pppigmodify_atonce_button_text = (By.XPATH, "html/body/div[1]/div[2]/div[2]/input")
	# 获取手机验证码
	pppigget_code_button_text = (By.XPATH, ".//*[@id='getOldCode']")
	# 验证码
	pppig_code_text = (By.XPATH, ".//*[@id='oldCodeValid']")
	# 确定
	pppig_enter_text = (By.XPATH, ".//*[@id='oldSMSValid']")

	# 获取新手机验证码
	pppigget_new_code_button_text = (By.XPATH, ".//*[@id='getNewCode']")
	# 新验证码
	pppig_new_code_text = (By.XPATH, ".//*[@id='newCodeValid']")
	# 新确定
	pppig_new_enter_text = (By.XPATH, ".//*[@id='queding']")

	# 账户设置
	def account_set(self):
		self.find_element(*self.account_set_text).click()

	# 更换第三方手机号
	def pppigchange_three_cellphone(self):
		self.find_element(*self.pppigchange_three_cellphone_text).click()

	# 原手机号
	def pppigold_cellphone(self, text):
		self.find_element(*self.pppigold_cellphone_text).click()
		self.find_element(*self.pppigold_cellphone_text).clear()
		self.find_element(*self.pppigold_cellphone_text).send_keys(text)

	# 新手机号
	def pppignew_cellphone(self, text):
		self.find_element(*self.pppignew_cellphone_text).send_keys(text)
	# 修改按钮
	def pppigmodify_button(self):
		self.find_element(*self.pppigmodify_button_text).click()

	# 通过手机号立即修改
	def pppigmodify_atonce_button(self):
		self.find_element(*self.pppigmodify_atonce_button_text).click()

	# 获取手机验证码
	def pppigget_code_button(self):
		self.find_element(*self.pppigget_code_button_text).click()

	# 验证码
	def pppig_code(self, text):
		self.find_element(*self.pppig_code_text).send_keys(text)

	# 确定
	def pppig_enter(self):
		self.find_element(*self.pppig_enter_text).click()

	# 获取手机验证码
	def pppigget_new_code_button(self):
		self.find_element(*self.pppigget_new_code_button_text).click()

	# 验证码
	def pppig_new_code(self, text):
		self.find_element(*self.pppig_new_code_text).send_keys(text)

	# 确定
	def pppig_new_enter(self):
		self.find_element(*self.pppig_new_enter_text).click()




	# 修改手机号
	def pppigmodify_phone_Action(self, oldcellphone, newcellphone, code='111111'):
		self.account_set()
		sleep(1)
		self.pppigchange_three_cellphone()
		sleep(1)
		self.pppigold_cellphone(oldcellphone)
		self.pppignew_cellphone(newcellphone)
		self.pppigmodify_button()
		sleep(1)
		self.pppigmodify_atonce_button()
		self.pppigget_code_button()
		self.pppig_code(code)
		self.pppig_enter()
		sleep(1)
		self.pppigget_new_code_button()
		self.pppig_new_code(code)
		self.pppig_new_enter()

	# 点击登录
	def pppiglogin3_Action(self):
		self.pppiglogin_button()

	# 登入不退出
	def pppiglogin_noclose_Action(self, username, password):
		self.pppig_click_topassword()
		self.pppiglogin_username(username)
		self.pppiglogin_password(password)
		self.pppiglogin_button()

	# 有退出操作的登陆
	def pppiglogin_close_Action(self, username, password):
		self.pppig_click_topassword()
		self.pppiglogin_username(username)
		self.pppiglogin_password(password)
		self.pppiglogin_button()
		self.pppiglogin_close_button()







