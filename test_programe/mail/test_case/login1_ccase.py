#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.to_login_page import To_login
from model.txt import Reader_txt
from page_object.mail_page import MailPage
# sys.path.append('./model')
# sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        f = open('D:\\name.txt')
        lines = f.readlines()
        for line in lines:
            username = line.split(',')[0]
            password = line.split(',')[1]
            po = LoginPage(self.driver)
            sleep(5)
            po.open()

            po.pppiglogin_Action(username, password)
            sleep(2)
            po2 = To_login(self.driver)
            print(po2.login_success_user())
            # self.assertEqual(po2.login_success_user(),username)
            function.insert_img(self.driver, "success.png")


# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
