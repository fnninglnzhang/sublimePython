#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base

class To_login(Base):
    url = '/toLoginPage'
    pppiglogin_success_user = (By.XPATH, ".//*[@id='indexPPPig']/div[1]/div/ul/li[1]/a[1]")

    def login_success_user(self):
        return self.find_element(*self.pppiglogin_success_user).text

