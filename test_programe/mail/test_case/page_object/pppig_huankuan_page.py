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
class Huankuan(Page):
    # url = '/toLoginPage'
    url = '/backingBorrow'
    pppighuankuan_btn_text = (By.XPATH, '//*[@id="help-3"]/table/tbody/tr[1]/td[7]/a')
    pppighuankuan_yuandian_text = (By.XPATH, '//*[@id="7612-50312.50"]')
    pppighuankuan_btnb_text = (By.XPATH, '//*[@id="guHuankuan"]')


    # 把每一个元素封装成一个方法
    def pppighuankuan_btn(self):
        self.find_element(*self.pppighuankuan_btn_text).click()
    def pppighuankuan_yuandian(self):
        self.find_element(*self.pppighuankuan_yuandian_text).click()
    def pppighuankuan_btnb(self):
        self.find_element(*self.pppighuankuan_btnb_text).click()

    # 处理浏览器弹窗
    def switch_to_alert(self):
        self.driver.switch_to_alert().accept()


    def pppighuankuan_Action(self):
        self.pppighuankuan_btn()
        self.pppighuankuan_yuandian()
        self.pppighuankuan_btnb()
        self.switch_to_alert()


