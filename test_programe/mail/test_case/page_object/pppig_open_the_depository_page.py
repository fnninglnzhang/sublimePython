# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pppig_page import Page
from model import *
from selenium import webdriver

#页面对象（PO）登录页面
class Opendepository(Page):
    # 立即开通银行存管（注册）
    pppigopendepository_btn_text = (By.XPATH, "html/body/div[4]/div/a[1]")
    # 立即开通银行存管（重新登录）
    pppigopendepository_repeat_btn_text = (By.XPATH, "html/body/div[4]/div[3]/a")
    # 暂不开通银行存管
    pppignotopendepository_btn_text = (By.XPATH, "html/body/div[4]/div/a[2]")
    # 开通银行账户真实姓名
    pppigopendepository_jx_real_name_text = (By.ID, 'KH_userRealName')
    # 开通银行账户身份证号码
    pppigopendepository_jx_ID_number_text = (By.ID, "KH_userIdNumber")
    # 开通银行账户银行卡号
    pppigopendepository_jx_credit_card_numbers_text = (By.ID, "KH_account")
    # 开通银行账户修改手机号点击修改事件
    pppigopendepository_jx_modify_phone_numbers_button_text = (By.ID, "xiugaiPhone")
    # 开通银行账户修改手机号修改
    pppigopendepository_jx_modify_phone_numbers_text = (By.ID, "KH_userPhone")
    # 开通银行账户获取验证码点击事件
    pppigopendepository_jx_getcode_button_text = (By.ID, "getPhoneYzm")
    # 开通银行账户验证码
    pppigopendepository_jx_message_checkcode_text = (By.ID, "KH_PhoneYzm")
    # 开通银行账户同意协议
    pppigopendepository_jx_agreement_text = (By.ID, "agreement")
    # 开通银行账户立即开通
    pppigopendepository_jx_agree_text = (By.ID, "KH_button")
    # 开户成功    用于断言开户成功
    pppigsuccessful_opening_an_account_text = (By.XPATH, "html/body/div[4]/div/div/h2")
    # 前往我的账户
    pppigto_Go_myaccount_text = (By.XPATH, "html/body/div[4]/div/div/a[2]")
    # 绑定卡号
    pppigopendepository_jx_binding_card_text = (By.ID, "BIND_CARD_NO")
    # 获取验证码
    pppigopendepository_jx_getimaggecode_button_text = (By.ID, "smsBtn")
    # 同意协议
    pppigsuccessful_jx_agree_product_text = (By.ID, "mainAcceptIpt")
    # 确认
    pppigsuccessful_jx_agree_button_text = (By.ID, "sub")








    # 把每一个元素封装成一个方法
    # 立即开通银行存管（注册）
    def pppigopendepository_Btn(self):
        self.find_element(*self.pppigopendepository_btn_text).click()

    # 立即开通银行存管（重新登录）
    def pppigopendepository_repeat_btn(self):
        self.find_element(*self.pppigopendepository_repeat_btn_text).click()

    # 暂不开通银行存管
    def pppignotopendepository_Btn(self):
        self.find_element(*self.pppignotopendepository_btn_text).click()

    # 开通银行账户真实姓名
    def pppigopendepository_Jx_real_name(self, text):
        self.find_element(*self.pppigopendepository_jx_real_name_text ).send_keys(text)

    # 开通银行账户身份证号码
    def pppigopendepository_Jx_ID_number(self, text):
        self.find_element(*self.pppigopendepository_jx_ID_number_text).send_keys(text)

    # 开通银行账户银行卡号
    def pppigopendepository_Jx_credit_card_numbers(self, text):
        self.find_element(*self.pppigopendepository_jx_credit_card_numbers_text).send_keys(text)

    # 开通银行账户修改手机号点击修改事件
    def pppigopendepository_Jx_modify_phone_numbers_button(self):
        self.find_element(*self.pppigopendepository_jx_modify_phone_numbers_button_text).click()

    # 开通银行账户修改手机号修改
    def pppigopendepository_Jx_modify_phone_numbers(self, text):
        self.find_element(*self.pppigopendepository_jx_modify_phone_numbers_text).click()
        self.find_element(*self.pppigopendepository_jx_modify_phone_numbers_text).clear()
        self.find_element(*self.pppigopendepository_jx_modify_phone_numbers_text ).send_keys(text)

    # 开通银行账户获取验证码点击事件
    def pppigopendepository_Jx_getcode_button(self):
        self.find_element(*self.pppigopendepository_jx_getcode_button_text).click()

    # 开通银行账户验证码
    def pppigopendepository_Jx_message_checkcode(self, text):
        self.find_element(*self.pppigopendepository_jx_message_checkcode_text).send_keys(text)

    # 开通银行账户同意协议
    def pppigopendepository_Jx_agreement(self):
        self.find_element(*self.pppigopendepository_jx_agreement_text ).click()

    # 开通银行账户修改手机号修改
    def pppigopendepository_Jx_agree(self):
        self.find_element(*self.pppigopendepository_jx_agree_text).click()

    # 开户成功    用于断言开户成功
    def pppigsuccessful_Opening_an_account(self):
        return self.find_element(*self.pppigsuccessful_opening_an_account_text).text


    # 前往我的账户
    def pppigto_Go_myaccount(self):
        self.find_element(*self.pppigto_Go_myaccount_text).click()

    # 绑定卡号
    def pppigopendepository_jx_binding_card(self, text):
        self.find_element(*self.pppigopendepository_jx_binding_card_text ).send_keys(text)

    # 获取验证码
    def pppigopendepository_jx_getimaggecode_button(self):
        self.find_element(*self.pppigopendepository_jx_getimaggecode_button_text ).click()

    # 同意协议
    def pppigsuccessful_jx_agree_product(self):
        return self.find_element(*self.pppigsuccessful_jx_agree_product_text ).click()

    # 确认
    def pppigsuccessful_jx_agree_button(self):
        self.find_element(*self.pppigsuccessful_jx_agree_button_text ).click()







    # 注册
    def opendepository1_Action(self):
        self.pppigopendepository_Btn()
    # 重新登录
    def opendepository_repeat_Action(self):
        self.pppigopendepository_repeat_btn()


    """
    # 合规前
    def opendepository2_Action(self, realname, idnumber, bankcard, checkcode):
        self.pppigopendepository_Jx_real_name(realname)
        self.pppigopendepository_Jx_ID_number(idnumber)
        self.pppigopendepository_Jx_credit_card_numbers(bankcard)
        self.pppigopendepository_Jx_getcode_button()
        self.pppigopendepository_Jx_message_checkcode(checkcode)
        self.pppigopendepository_Jx_agreement()
        self.pppigopendepository_Jx_agree()
    """

    # 合规后_身份录入
    def opendepository2_Action(self, realname, idnumber, bankcard, cellphone='15120080522'):
        self.pppigopendepository_Jx_real_name(realname)
        self.pppigopendepository_Jx_ID_number(idnumber)
        self.pppigopendepository_Jx_credit_card_numbers(bankcard)
        self.pppigopendepository_Jx_modify_phone_numbers(cellphone)
        self.pppigopendepository_Jx_agreement()
        self.pppigopendepository_Jx_agree()



    # 合规后_存管账户开立
    def opendepository3_Action(self, cardnumber):
        self.pppigopendepository_jx_binding_card(cardnumber)
        self.pppigopendepository_jx_getimaggecode_button()
        # 手动输入验证码
        sleep(15)
        self.pppigsuccessful_jx_agree_product()
        self.pppigsuccessful_jx_agree_button()

