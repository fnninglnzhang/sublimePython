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
    # 立即开通银行存管
    pppigopendepository_btn_text = (By.XPATH, "html/body/div[4]/div/a[1]")
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


    # 把每一个元素封装成一个方法
    # 立即开通银行存管
    def pppigopendepository_Btn(self):
        self.find_element(*self.pppigopendepository_btn_text).click()

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



    def opendepository1_Action(self):
        self.pppigopendepository_Btn()

    def opendepository2_Action(self, realname, idnumber, bankcard, checkcode):
        self.pppigopendepository_Jx_real_name(realname)
        self.pppigopendepository_Jx_ID_number(idnumber)
        self.pppigopendepository_Jx_credit_card_numbers(bankcard)
        self.pppigopendepository_Jx_getcode_button()
        self.pppigopendepository_Jx_message_checkcode(checkcode)
        self.pppigopendepository_Jx_agreement()
        self.pppigopendepository_Jx_agree
