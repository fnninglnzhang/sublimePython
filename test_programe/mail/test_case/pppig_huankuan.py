#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_huankuan_page import Huankuan
from page_object.pppig_to_invest_page import To_invest
from model.log import log
from page_object.to_login_page import To_login
from page_object.mail_page import MailPage


class HuankuanTest(myunit.MyTest):

    def test_huankuan(self):
        '''还款'''
        try:
            for i in range(1, 100):
                po = LoginPage(self.driver)
                po.open()
                username = 'UATtest049'
                po.pppiglogin_noclose_Action(username, '111111')
                sleep(2)
                # po.open_R('/backingBorrow')
                po.open_R('/repayDetail?loanId={}'.format(loanId))
                pohuankuan = Huankuan(self.driver)
                pohuankuan.pppighuankuan_Action()
                po1 = To_invest(self.driver)
                po1.pppiginvest_Action4("111111")
                sleep(2)
                poclose = LoginPage(self.driver)
                poclose.pppiglogin_close_button()


        except BaseException as e:
            print(e)




# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
