# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from page import Page
from selenium import webdriver
#页面对象（PO）登录页面
class LoginPage(Page):
    url = '/toLoginPage'
    pppiglogin_btn_topassword = (By.ID,'zhanghaoDl')
    pppiglogin_username_text = (By.NAME, 'userName')
    pppiglogin_password_text = (By.NAME, 'password')
    pppiglogin_button_text = (By.ID, 'loginSubmit')
    pppiglogin_erro_hint_text = (By.ID, 'errorStr')

    #把每一个元素封装成一个方法
    def btn_topassword(self):
        self.driver.find_element(self.pppiglogin_btn_topassword).click()

    def pppiglogin_username(self, text):
        self.driver.find_element(*self.pppiglogin_username_text).send_keys(text)

    def pppiglogin_password(self, text):
        self.driver.find_element(*self.pppiglogin_password_text).send_keys(text)

    def pppiglogin_button(self):
        self.driver.find_element(*self.pppiglogin_button_text).click()

    def pppiglogin_erro_hint(self):
        return self.driver.find_element(*self.pppiglogin_erro_hint_text).text


    def pppiglogin_action(self, username, password):
        self.btn_topassword()
        self.pppiglogin_username(username)
        self.pppiglogin_password(password)
        self.pppiglogin_button()