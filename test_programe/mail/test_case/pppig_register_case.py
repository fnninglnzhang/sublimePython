#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_goRegister_page import GoRegister
from page_object.to_login_page import To_login
from model.connect_mysql import *



class RegisterTest(myunit.MyTest):

    def test_register_success(self):
        '''注册'''
        poRegister = GoRegister(self.driver)
        sleep(2)
        poRegistercode = SelectMySQL()
        poRegister.open()
        poRegister.goregisternoinvite1_Action("13011111118", "111111", "1111")
        checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile=13011111118 and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1")
        poRegister.goregisternoinvite2_Action(checkCode)
        sleep(2)


        function.insert_img(self.driver, "success.png")