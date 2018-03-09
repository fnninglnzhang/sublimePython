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
        '''修改手机号'''
        try:
            po = LoginPage(self.driver)
            po.open()
            username = '18079409047'
            po.pppiglogin_noclose_Action(username, '111111')
            sleep(2)

            # 立即开通银行存管
            poopendepository = Opendepository(self.driver)
            poopendepository.opendepository_repeat_Action()
            sleep(2)
            # poopendepository.opendepository2_Action(realname, idcode, bankcard)
            bankcard = '3005229650080765337'
            poopendepository.opendepository2_Action('李测试账户一', '310101198807252788', bankcard)
            # 江西银行-网贷资金存管账户开立-银行卡号
            poopendepository.opendepository3_Action(bankcard)
            # 跳转等待
            sleep(7)
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
        except BaseException as e:
            print(e)




# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
