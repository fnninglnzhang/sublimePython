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
        username = 18565400667
        poRegister.goregisternoinvite1_Action(username, "111111", "1111")
        sleep(2)
        checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile={} and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1".format(username))
        poRegister.goregisterokinvite_Action(checkCode, '04257802')
        poopendepository = Opendepository(self.driver)
        poopendepository.opendepository1_Action()
        sleep(2)
        poopendepository.opendepository2_Action("李测试账户三", "310101198909029499", "3005108627957482010", "111111")

        function.insert_img(self.driver, "success.png")