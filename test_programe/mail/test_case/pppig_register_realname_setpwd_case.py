#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_goRegister_page import GoRegister
from page_object.pppig_open_the_depository_page import Opendepository
from page_object.pppig_set_transaction_password_page import SetTransactionPWD
from model.oldconnect_mysql import *

class RegisterTest(myunit.MyTest):

    def test_register_success(self):
        '''注册'''
        try:
            f = open('../date/register.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]                                         # 取第一列用户名数据
                password = line.split(',')[1]                                         # 取第二列密码数据
                # getcode = line.split(',')[2]                                          # 取第三列验证码数据     sql语句
                realname = line.split(',')[2]
                idcode = line.split(',')[3]
                bankcard = line.split(',')[4]
                # 注册
                poRegister = GoRegister(self.driver)
                sleep(2)
                # 查询验证码
                poRegistercode = SelectMySQL()
                poRegister.open()
                # 下方用例包含点击获取验证码
                poRegister.goregisternoinvite1_Action(username, password, "1111")
                checkCode = poRegistercode.select_Data("select validCode from mobile_authen where mobile= {} and mobileAuthenid>3399000 ORDER BY sendTime desc limit 0,1".format(username))
                # 下方用例包含输入验证码 - 同意协议 - 点击注册
                poRegister.goregisternoinvite2_Action(checkCode)
                # 实名认证
                poopendepository = Opendepository(self.driver)
                poopendepository.opendepository1_Action()
                sleep(2)
                poopendepository.opendepository2_Action(realname, idcode, bankcard, "111111")
                # self.assertEqual(u'开户成功', poopendepository.pppigsuccessful_Opening_an_account())
                # 点击前往我的账户
                poopendepository.pppigto_Go_myaccount()
                # 有一个跳转的过程要加等待
                sleep(2)
                # 设置交易密码
                poset_transaction_password = SetTransactionPWD(self.driver)
                sleep(2)
                poset_transaction_password.pppigset_Transaction_password_Action('111111', '111111')
                sleep(10)
                pologout = LoginPage(self.driver)
                pologout.pppiglogin_close_Action(username, password)
                pologout.pppiglogin_close_button()
        except BaseException as e:
            print(e)

# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()







