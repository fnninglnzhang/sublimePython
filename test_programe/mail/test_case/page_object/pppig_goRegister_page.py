# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from model import *
from selenium import webdriver

#页面对象（PO）登录页面
class GoRegister(Page):
	url = '/goRegister'
	# 我要出借
	pppiggoregister_user_role1_text = (By.XPATH, ".//*[@id='user-role']/div[1]/i")
	# 我要借款
	pppiggoregister_user_role2_text = (By.XPATH, ".//*[@id='user-role']/div[2]/i")
	# 手机号
	pppiggoregister_mobilePhone_text = (By.ID, 'mobilePhone')
	# 登录密码
	pppiggoregister_password_text = (By.ID, 'pass')
	# 图形验证码
	pppiggoregister_checkTuCode_text = (By.ID, 'tucode')
	# 获取短信验证码点击
	pppiggoregister_getCodeButton_text = (By.ID, 'getCodeButton')
	# 验证码
	pppiggoregister_message_checkCode_text = (By.ID, 'mbverifycode')
	# 推荐人邀请码
	pppiggoregister_referral_invitation_code_button_text = (By.XPATH, ".//*[@id='registerUser']/div/div[7]/span")
	# 邀请号
	pppiggoregister_invite_number_text = (By.ID, 'invitedCode1')
	# 同意协议
	pppiggoregister_agreement_text = (By.ID, 'agreement')
	# 注册按钮
	pppiggoregister_button_text = (By.XPATH, ".//*[@id='registerUser']/div/a")

	# 把每一个元素封装成一个方法
	# 我要出借
	def pppiggoregister_User_Role1(self):
		self.find_element(*self.pppiggoregister_user_role1_text).click()

	# 我要借款
	def pppiggoregister_User_Role2(self):
		self.find_element(*self.pppiggoregister_user_role2_text).click()

	# 手机号
	def pppiggoregister_MobilePhone(self, text):
		self.find_element(*self.pppiggoregister_mobilePhone_text).send_keys(text)

	# 登录密码
	def pppiggoregister_Password(self, text):
		self.find_element(*self.pppiggoregister_password_text).send_keys(text)

	# 图形验证码
	def pppiggoregister_CheckTuCode(self, text):
		self.find_element(*self.pppiggoregister_checkTuCode_text).send_keys(text)

	# 获取短信验证码点击
	def pppiggoregister_GetCodeButton (self):
		self.find_element(*self.pppiggoregister_getCodeButton_text).click()

	# 短信验证码
	def pppiggoregister_Message_CheckCode (self, text):
		self.find_element(*self.pppiggoregister_message_checkCode_text).send_keys(text)

	# 推荐人邀请码点击
	def pppiggoregister_referral_invitation_code_button (self):
		self.find_element(*self.pppiggoregister_referral_invitation_code_button_text).click()

	# 邀请号
	def pppiggoregister_invite_number (self, text):
		self.find_element(*self.pppiggoregister_invite_number_text ).send_keys(text)

	# 同意协议
	def pppiggoregister_agreement(self):
		self.find_element(*self.pppiggoregister_agreement_text).click()

	# 注册按钮
	def pppiggoregister_button(self):
		self.find_element(*self.pppiggoregister_button_text).click()

	# 无邀请码
	def goregisternoinvite_Action(self, mobilePhone, password, checkTuCode, checkCode,):
		self.pppiggoregister_User_Role1()
		self.pppiggoregister_MobilePhone(mobilePhone)
		self.pppiggoregister_Password(password)
		self.pppiggoregister_CheckTuCode(checkTuCode)
		self.pppiggoregister_GetCodeButton()
		self.pppiggoregister_Message_CheckCode(checkCode)
		self.pppiggoregister_agreement()
		self.pppiggoregister_button()

	# 有邀请码
	def goregisterinvite_Action(self, mobilePhone, password, checkTuCode, checkCode, invitenumber):
		self.pppiggoregister_User_Role1()
		self.pppiggoregister_MobilePhone(mobilePhone)
		self.pppiggoregister_Password(password)
		self.pppiggoregister_CheckTuCode(checkTuCode)
		self.pppiggoregister_GetCodeButton()
		self.pppiggoregister_Message_CheckCode(checkCode)
		self.pppiggoregister_referral_invitation_code_button()
		self.pppiggoregister_invite_number(invitenumber)
		self.pppiggoregister_agreement()
		self.pppiggoregister_button()