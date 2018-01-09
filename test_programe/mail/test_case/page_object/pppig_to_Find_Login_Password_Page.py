# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from model.connect_mysql import *

class ForgetPWD(Page):

	url = '/toFindLoginPasswordPage'
	# 忘记密码点击事件
	pppigforget_pwd_text = (By.XPATH, "html/body/div[3]/div/div[2]/div[2]/div[3]/a")

	# 选择一种修改方式
	# 通过手机修改
	pppigselect_mobilephone_modification_pwd_text = (By.XPATH, ".//*[@id='guAlter']/div[2]/div/ul/li[1]/a")
	# 通过邮箱修改
	pppigselect_mailbox_modification_pwd_text = (By.XPATH,".//*[@id='guAlter']/div[2]/div/ul/li[2]/a")
	# 手机号码
	pppigselect_mobilephone_modification_pwd_telephonenumber_text = (By.ID, "phone_pwd")
	# 图形验证码
	pppigselect_mobilephone_modification_pwd_verificationcode_text = (By.ID, "tucode")
	# pppigselect_mobilephone_modification_pwd_verificationcode_text = (By.XPATH, ".//*[@id='tucode']")
	# 手机验证码
	pppigselect_mobilephone_modification_pwd_cellphone_verificationcode_text = (By.ID, "mbverifycode")
	# 获取验证码按钮
	pppigselect_mobilephone_modification_pwd_Click_on_the_get_text = (By.ID, "getCodeButton")
	# 下一步
	pppigselect_mobilephone_modification_pwd_next_step_text = (By.XPATH, ".//*[@id='registerUser']/div[6]/div/button")
	# 新密码
	pppigselect_mobilephone_modification_pwd_new_pwd_text = (By.ID, "newpassword")
	# 确认密码
	pppigselect_mobilephone_modification_pwd_enter_new_pwd_text = (By.ID, "rnewpassword")
	# 下一步
	pppigselect_mobilephone_modification_pwd_enter_new_pwd_next_step_text = (By.XPATH, ".//*[@id='guAlter']/form/div[3]/button")

	# 忘记密码点击事件
	def pppigforget_Pwd(self):
		self.find_element(*self.pppigforget_pwd_text).click()

	# 通过手机修改
	def pppigselect_Mobilephone_modification_pwd(self):
		self.find_element(*self.pppigselect_mobilephone_modification_pwd_text).click()

	# 通过邮箱修改
	def pppigselect_Mailbox_modification_pwd(self):
		self.find_element(*self.pppigselect_mailbox_modification_pwd_text).click()
	# 手机号码
	def pppigselect_Mobilephone_modification_pwd_telephonenumber(self,text):
			self.find_element(*self.pppigselect_mobilephone_modification_pwd_telephonenumber_text).send_keys(text)
	# 图形验证码
	def pppigselect_Mobilephone_modification_pwd_verificationcode(self,text):
			self.find_element(*self.pppigselect_mobilephone_modification_pwd_verificationcode_text).send_keys(text)
	# 点击获取手机验证
	def pppigselect_Mobilephone_modification_pwd_Click_on_the_get(self):
		self.find_element(*self.pppigselect_mobilephone_modification_pwd_Click_on_the_get_text).click()
	# 输入手机验证码
	def pppigselect_Mobilephone_modification_pwd_cellphone_verificationcode(self,text):
			self.find_element(*self.pppigselect_mobilephone_modification_pwd_cellphone_verificationcode_text).send_keys(text)

	# 点击下一步
	def pppigselect_Mobilephone_modification_pwd_next_step(self):
		self.find_element(*self.pppigselect_mobilephone_modification_pwd_next_step_text).click()

	# 新密码
	def pppigselect_Mobilephone_modification_pwd_new_pwd(self,text):
		self.find_element(*self.pppigselect_mobilephone_modification_pwd_new_pwd_text).send_keys(text)

	# 确认新密码
	def pppigselect_Mobilephone_modification_pwd_enter_new_pwd(self,text):
		self.find_element(*self.pppigselect_mobilephone_modification_pwd_enter_new_pwd_text).send_keys(text)

		# 点击下一步
	def pppigselect_Mobilephone_modification_pwd_enter_new_pwd_next_step(self):
			self.find_element(*self.pppigselect_mobilephone_modification_pwd_enter_new_pwd_next_step_text).click()

	def toFindLoginPasswordPage_Action(self):
		self.pppigselect_Mobilephone_modification_pwd()

	def toFindLoginPasswordForPhonePage1_Action(self, cellphone, code):
		# self.pppigselect_Mobilephone_modification_pwd()
		self.pppigselect_Mobilephone_modification_pwd_telephonenumber(cellphone)
		self.pppigselect_Mobilephone_modification_pwd_verificationcode(code)
		self.pppigselect_Mobilephone_modification_pwd_Click_on_the_get()
		# self.pppigselect_Mobilephone_modification_pwd_cellphone_verificationcode(cellcode)
		# self.pppigselect_Mobilephone_modification_pwd_next_step()

	def toFindLoginPasswordForPhonePage2_Action(self,cellcode):
		self.pppigselect_Mobilephone_modification_pwd_cellphone_verificationcode(cellcode)
		self.pppigselect_Mobilephone_modification_pwd_next_step()

	def findByValidCodeP(self, newpassword1, rnewpassword1):
		self.pppigselect_Mobilephone_modification_pwd_new_pwd(newpassword1)
		self.pppigselect_Mobilephone_modification_pwd_enter_new_pwd(rnewpassword1)
		self.pppigselect_Mobilephone_modification_pwd_enter_new_pwd_next_step()