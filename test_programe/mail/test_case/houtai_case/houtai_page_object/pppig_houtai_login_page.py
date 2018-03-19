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
class HoutaiLoginPage(Page):
    # url = '/toLoginPage'
    url = '/login.action'
    pppig_houtai_login_username_text = (By.XPATH, ".//*[@id='guDenglvert']/div/form/div[1]/input")
    pppig_houtai_login_password_text = (By.XPATH, ".//*[@id='guDenglvert']/div/form/div[2]/input")
    pppig_houtai_login_button_text = (By.ID, 'denglu')




    # 把每一个元素封装成一个方法
    def pppig_click_topassword(self):
        self.find_element(*self.pppig_houtai_login_username_text).click()

    def pppig_houtai_login_username(self, text):
        self.find_element(*self.pppig_houtai_login_username_text).send_keys(text)

    def pppig_houtai_login_password(self, text):
        self.find_element(*self.pppig_houtai_login_username_text).send_keys(text)



    # 点击账号密码登录
    def pppig_houtai_login_Action(self,username, password):
        self.pppig_click_topassword()
        self.pppig_houtai_login_username(username)
        self.pppig_houtai_login_username(password)








