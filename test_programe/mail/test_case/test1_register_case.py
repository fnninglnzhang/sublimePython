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
        f = open('../date/register.txt')
        lines = f.readlines()
        for line in lines:
            username = line.split(',')[0]                                         # 取第一列用户名数据
            password = line.split(',')[1]                                         # 取第二列密码数据
            # getcode = line.split(',')[2]                                          # 取第三列验证码数据     sql语句
            realname = line.split(',')[2]
            idcode = line.split(',')[3]
            bankcard = line.split(',')[4]

            poRegister = GoRegister(self.driver)
            sleep(2)
            poRegistercode = SelectMySQL()
            poRegister.open()
            poRegister.goregisternoinvite1_Action(username, password, "1111")     # 包含点击获取验证码


            # checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile=13011111122 and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1")
            # 把sql完整的写到txt文档中
            # checkCode = poRegistercode.select_Data(getcode)
            # 使用占位符
            # checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile= {%s} and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1".format(username))
            checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile= {} and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1".format(username))
            print(checkCode)



            poRegister.goregisternoinvite2_Action(checkCode)
            poopendepository = Opendepository(self.driver)
            poopendepository.opendepository1_Action()
            sleep(2)
            poopendepository.opendepository2_Action(realname, idcode, bankcard, "111111")


        sleep(2)


        function.insert_img(self.driver, "success.png")