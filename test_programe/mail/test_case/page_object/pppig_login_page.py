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
class LoginPage(Page):
    # url = '/toLoginPage'
    url = '/accountInfo'
    # pppiglogin_btn_topassword = (By.ID,'zhanghaoDl')
    pppiglogin_btn_topassword = (By.XPATH, ".//*[@id='zhanghaoDl']")
    pppiglogin_username_text = (By.ID, 'userName')
    pppiglogin_password_text = (By.ID, 'password')
    pppiglogin_button_text = (By.ID, 'loginSubmit')
    pppiglogin_erro_hint_text = (By.ID, 'errorStr')
    pppiglogin_close_button_text = (By.XPATH, ".//*[@id='indexPPPig']/div[1]/div/ul/li[1]/a[2]")

    # 把每一个元素封装成一个方法
    def pppig_click_topassword(self):
        self.find_element(*self.pppiglogin_btn_topassword).click()

    def pppiglogin_username(self, text):
        self.find_element(*self.pppiglogin_username_text).send_keys(text)

    def pppiglogin_password(self, text):
        self.find_element(*self.pppiglogin_password_text).send_keys(text)

    def pppiglogin_button(self):
        self.find_element(*self.pppiglogin_button_text).click()

    def pppiglogin_close_button(self):
        self.find_element(*self.pppiglogin_close_button_text).click()

    def pppiglogin_erro_hint(self):
        return self.find_element(*self.pppiglogin_erro_hint_text).text

    def pppiglogin1_Action(self):                                            # 点击账号密码登录
        self.pppig_click_topassword()

    def pppiglogin2_Action(self, username, password):                        # 输入用户名密码
        self.pppiglogin_username(username)
        self.pppiglogin_password(password)

    def pppiglogin3_Action(self):                                              # 点击登录
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









    """
    def reader_txt(self, address):
        fp = codecs.open(address, 'r', "gb18030")
        # fp=open(address,'r')
        users = []
        pwds = []
        lines = fp.readlines()
        for data in lines:
            name, pwd = data.split(',')
            name = name.strip(' \t\r\n')
            pwd = pwd.strip(' \t\r\n')
            users.append(name)
            pwds.append(pwd)
            print("user:%s(len(%d))" % (name, len(name)))
            print("pwd:%s(len(%d))" % (pwd, len(pwd)))
        return users, pwds
        # fp.close()
    """
