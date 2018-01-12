#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_goRegister_page import GoRegister
from page_object.pppig_open_the_depository_page import Opendepository
from model.oldconnect_mysql import *



class RegisterTest(myunit.MyTest):

    def test_register_success(self):
        '''注册'''
        poRegister = GoRegister(self.driver)
        sleep(2)
        poRegistercode = SelectMySQL()
        poRegister.open()
        poRegister.goregisternoinvite1_Action("13011111122", "111111", "1111")
        checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile=13011111122 and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1")
        poRegister.goregisternoinvite2_Action(checkCode)
        poopendepository = Opendepository(self.driver)
        poopendepository.opendepository1_Action()
        sleep(2)
        poopendepository.opendepository2_Action("李测试账户五", "310101199207230627", "3005294647733520", "111111")


        sleep(2)


        function.insert_img(self.driver, "success.png")