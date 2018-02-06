#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from model.log import log
from page_object.to_login_page import To_login
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        try:
            po = LoginPage(self.driver)
            po.open()
            username = '15511509024'
            po.pppiglogin_noclose_Action(username, '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_success_user(), username)                             # 登录成功后断言右上角的用户信息
            print(po.pppiglogin_success_user()+'登陆成功')                                      # 打印用户登录成功
            function.insert_img(self.driver, "pppig_login_success.png")                       # 截图
        except BaseException as e:
            mylog = log()
            mylog.error(e)
            print(e)




# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
