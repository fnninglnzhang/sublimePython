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
        # try:
        po = LoginPage(self.driver)
        po.open()
        username = '18079409047'
        po.pppiglogin_noclose_Action(username, '111111')
        sleep(2)



        # 修改手机号
        pomodifyphone = Modify_cellphone_Page(self.driver)
        pomodifyphone.pppigmodify_phone_Action('15120080522', username)
        # except BaseException as e:
        #     print(e)




# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
