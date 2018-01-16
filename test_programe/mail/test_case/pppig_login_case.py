#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.to_login_page import To_login
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_success(self):
        '''参数化、用户名、密码正确,登录成功'''
        try:
            f = open('../date/name.txt')
            # f = open('D:\\name.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]
                password = line.split(',')[1]
                po = LoginPage(self.driver)
                # sleep(1)
                po.open()
                po.pppiglogin_close_Action(username, password)
                sleep(2)
        except BaseException as e:
            print(e)


    """
    def test_no_close_login_success(self):
        '''没有退出用户名、密码正确,登录'''
        try:
            po = LoginPage(self.driver)
            po.open()
            po.pppiglogin_noclose_Action("13011111101", "111111")
            sleep(2)
        except BaseException as e:
            print(e)
    """

# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
