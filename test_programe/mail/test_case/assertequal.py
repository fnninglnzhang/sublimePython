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
        po = LoginPage(self.driver)
        po.open()
        sleep(5)
        self.assertEqual(u'登录', po.pppigabout_us())
        po.pppiglogin_close_Action('13011111101', '111111')
        sleep(3)




# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
