# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from selenium import webdriver
#页面对象（PO）登录页面
class RegisterPage(Page):
	url = '/goRegister'
	pppigregister_User1_role_text = (By.LINK_TEXT, '我要出借')
	pppigregister_User2_role_text = (By.LINK_TEXT, '我要借款')
	pppigregister_User_phone_text = (By.ID, 'mobilePhone')
	pppigregister_User_pwd_text = (By.ID, 'pass')
	pppigregister_TXVerification_code_text = (By.ID, 'tucode')
	pppigregister_GetCode_Button_text = (By.ID, 'getCodeButton')
	pppigregister_Verification_code_text = (By.ID, 'mbverifycode')
	pppigregister_Referral_invitation_code_text = (By.LINK_TEXT, '推荐人邀请码')
	pppigregister_Invitation_code_text = (By.ID, 'invitedCode1')
	pppigregister_Agreement_text = (By.ID, 'agreement')
	pppigregister_Button_text = (By.CLASS_NAME, 'loandBtn')
	pppigregiter_mobile_erro_hint_text = (By.ID,'mobilemessage')




	# 把每一个元素封装成一个方法
	# 角色
	def pppig_User1_role(self):
		self.find_element(self.pppigregister_User1_role_text).click()

	def pppig_User2_role(self):
		self.find_element(self.pppigregister_User2_role_text).click()
	# 手机号
	def pppigregister_Username(self, text):
		self.find_element(*self.pppigregister_User_phone_text).send_keys(text)

	def pppigregister_Password(self, text):
		self.find_element(*self.pppigregister_User_pwd_text).send_keys(text)

	def pppigregister_TXcode(self, text):
		self.find_element(*self.pppigregister_TXVerification_code_text).send_keys(text)

	def pppigregister_GetCode_Button(self):
		self.find_element(self.pppigregister_GetCode_Button_text).click()

	def pppigregister_Referral_invitation_code(self):
		self.find_element(self.pppigregister_Referral_invitation_code_text).click()

	def pppigregister_code(self, text):
		self.find_element(*self.pppigregister_Verification_code_text).send_keys(text)

	def pppigregister_Invitation_code(self):
		self.find_element(*self.pppigregister_Invitation_code_text).click()

	def pppigregister_Agreement(self):
		self.find_element(*self.pppigregister_Agreement_text).click()

	def pppigregister_button(self):
		self.find_element(*self.pppigregister_Button_text).click()

	def pppigregiter_mobile_erro_hint(self):
		return self.find_element(*self.pppigregiter_mobile_erro_hint_text).text


	def pppigregiter_Action(self, username, password, TXcode, code):
		self.pppig_User1_role()
		self.pppigregister_Username(username)
		self.pppigregister_Password(password)
		self.pppigregister_TXcode(TXcode)
		self.pppigregister_GetCode_Button()
		self.pppigregister_code(code)
		self.pppigregister_Agreement()
		self.pppigregister_button()

