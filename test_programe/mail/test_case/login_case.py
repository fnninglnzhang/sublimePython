#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        po = LoginPage(self.driver)
        sleep(5)
        po.open()
        user = "13011111101"
        po.pppiglogin_action(user,"111111")
        sleep(2)
        po2 = MailPage(self.driver)
        print(po2.login_success_user())
        self.assertEqual(po2.login_success_user(),user+"@163.com")
        function.insert_img(self.driver, "success.jpg")


# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
