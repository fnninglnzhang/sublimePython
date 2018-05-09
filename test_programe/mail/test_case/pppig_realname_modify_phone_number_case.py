#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_open_the_depository_page import Opendepository
from page_object.pppig_modify_phone_number_page import Modify_cellphone_Page
from page_object.pppig_set_transaction_password_page import SetTransactionPWD




class LoginTest(myunit.MyTest):

    def test_login_success(self):
        '''开通银行存管，设置交易密码，修改手机号'''
        try:

            f = open('../date/register.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]  # 取第一列用户名数据
                password = line.split(',')[1]  # 取第二列密码数据
                # getcode = line.split(',')[2]                                          # 取第三列验证码数据     sql语句
                realname = line.split(',')[2]
                idcode = line.split(',')[3]
                bankcard = line.split(',')[4]
                po = LoginPage(self.driver)
                po.open()
                po.pppiglogin_noclose_Action(username, password)
                sleep(2)

                # 立即开通银行存管
                poopendepository = Opendepository(self.driver)
                poopendepository.opendepository_repeat_Action()
                sleep(2)
                # poopendepository.opendepository2_Action(realname, idcode, bankcard)
                poopendepository.opendepository2_Action(realname, idcode, bankcard)
                # 江西银行-网贷资金存管账户开立-银行卡号
                sleep(1)
                poopendepository.opendepository3_Action(bankcard)
                # 跳转等待
                sleep(6)
                # 点击前往我的账户
                poopendepository.pppigto_Go_myaccount()
                # 有一个跳转的过程要加等待
                sleep(2)
                # 设置交易密码
                poset_transaction_password = SetTransactionPWD(self.driver)
                sleep(2)
                poset_transaction_password.pppigset_Transaction_password_Action('111111', '111111')
                sleep(10)
                # 修改手机号
                pomodifyphone = Modify_cellphone_Page(self.driver)
                pomodifyphone.pppigmodify_phone_Action('15120080522', username)
                pologout = LoginPage(self.driver)
                pologout.pppiglogin_close_button()
                print(username +'充值成功！！！')
        except BaseException as e:
            print(e)




# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
