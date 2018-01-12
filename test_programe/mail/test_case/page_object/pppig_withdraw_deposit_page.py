# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page


#页面对象（PO）登录页面
class Withdraw_Deposit(Page):
    url = '/rechargeUI#withdraw'
    # 账户提现
    pppigccount_withdrawal_button_text = (By.XPATH, ".//*[@id='account-head-tabs']/a[2]")
    # 快速提现
    pppigrapid_withdrawal_button_text = (By.XPATH, ".//*[@id='cashForm']/div/a[1]")
    # 大额提现
    pppigwithdraw_deposits_button_text = (By.XPATH, ".//*[@id='cashForm']/div/a[1]")
    # 提现金额
    pppigcash_withdrawal_amount_text = (By.ID, 'withdrawMoney')
    # 输入银联卡号
    pppigeenter_the_unionpay_card_number_text = (By.ID, 'cardBankCnaps')
    # 提交申请
    pppigsubmit_applications_button_text = (By.ID, ".//*[@id='cashForm']/p[6]/button")


    # 把每一个元素封装成一个方法
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
        return self.find_element(*self.pppigsubmit_applications_button_text).click()

