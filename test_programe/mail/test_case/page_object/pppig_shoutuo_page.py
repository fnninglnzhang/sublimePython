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
class Shoutuo(Page):
    # url = '/toLoginPage'
    url = '/getNotTrusteePay'
    # pppiglogin_btn_topassword = (By.ID,'zhanghaoDl')
    pppigenter_btn_text = (By.XPATH, ".//*[@id='help-3']/table/tbody/tr[1]/td[7]/a[1]")

    # 把每一个元素封装成一个方法
    def pppigenter_btn(self):
        self.find_element(*self.pppigenter_btn_text).click()


    # 点击账号密码登录
    def pppigshoutuo_Action(self):
        self.pppigenter_btn()

