#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_set_transaction_password_page import SetTransactionPWD
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_success(self):
        '''参数化、用户名、密码正确,登录成功'''
        # try:
        po = LoginPage(self.driver)
        # sleep(1)
        po.open()
        po.pppiglogin_close_Action('18873692049', '111111')
        sleep(2)
        poset_transaction_password = SetTransactionPWD(self.driver)
        sleep(2)
        poset_transaction_password.pppigset_Transaction_password_Action('111111', '111111')
        sleep(5)
        # except BaseException as e:
        #     print(e)



# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
