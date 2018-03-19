#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from houtai_case.houtai_page_object.pppig_houtai_login_page import HoutaiLoginPage
from model.log import log
from page_object.to_login_page import To_login
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class HoutaiLoginTest(myunit.MyTest):

    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        try:
            po = HoutaiLoginPage(self.driver)
            po.open()
            po.pppig_houtai_login_Action('admin', '111111')
            sleep(2)
        except BaseException as e:
            mylog = log()
            mylog.error(e)
            print(e)




# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
