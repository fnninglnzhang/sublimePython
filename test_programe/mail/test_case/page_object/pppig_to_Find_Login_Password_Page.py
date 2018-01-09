# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
class ForgetPWD(Page):

	url = 'toFindLoginPasswordPage'
	# 忘记密码点击事件
	pppigforget_pwd = (By.XPATH, "html/body/div[3]/div/div[2]/div[2]/div[3]/a")
	# 选择一种修改方式
	# 通过手机修改
	pppigselect_mobilephone_modification_pwd = (By.XPATH, ".//*[@id='guAlter']/div[2]/div/ul/li[1]/a")
	# 通过邮箱修改
	pppigselect_mailbox_modification_pwd = (By.XPATH,".//*[@id='guAlter']/div[2]/div/ul/li[2]/a")
	# 手机号码
	pppigselect_mobilephone_modification_pwd_telephonenumber = (By.ID,"phone_pwd")
	# 图形验证码
	pppigselect_mobilephone_modification_pwd_verificationcode = (By.ID,"tucode")
	# 手机验证码
	pppigselect_mobilephone_modification_pwd_cellphone_verificationcode = (By.ID,"mbverifycode")
	# 获取验证码按钮
	pppigselect_mobilephone_modification_pwd_Click_on_the_get = (By.ID, "getCodeButton")
	# 下一步
	pppigselect_mobilephone_modification_pwd_next_step = (By.XPATH, ".//*[@id='registerUser']/div[6]/div/button")
	# 新密码
	pppigselect_mobilephone_modification_pwd_new_pwd = (By.ID, "newpassword")
	# 确认密码
	pppigselect_mobilephone_modification_pwd_enter_new_pwd = (By.ID, "rnewpassword")
	# 下一步
	pppigselect_mobilephone_modification_pwd_enter_new_pwd_next_step = (By.XPATH, ".//*[@id='guAlter']/form/div[3]/button")