#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.to_login_page import To_login
from model.txt import Reader_txt
from page_object.mail_page import MailPage
# import k1
# sys.path.append('./model')
# sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        f = open('../date/name.txt')
        # f = open('D:\\name.txt')
        lines = f.readlines()
        for line in lines:
            username = line.split(',')[0]
            password = line.split(',')[1]
            po = LoginPage(self.driver)
            sleep(2)
            po.open()
            po.pppiglogin1_Action()
            po.pppiglogin_username(username)
            po.pppiglogin_password(password)
            # po.pppiglogin2_Action(username, password)
            po.pppiglogin3_Action()
            sleep(2)
            po.pppiglogin_close_button()
            sleep(2)
            """
            po2 = To_login(self.driver)
            print(po2.login_success_user())
            self.assertEqual(po2.login_success_user(), username)
            """

# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
