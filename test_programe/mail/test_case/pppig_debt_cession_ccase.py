#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_debt_cession_page import To_investdebtcession
from page_object.pppig_product_details_page import Product_details
sys.path.append('./model')
sys.path.append('./page_obj')

class To_investdebtcessionTest(myunit.MyTest):

    def test_to_invest_success(self):
        '''投资'''
        po = LoginPage(self.driver)
        sleep(2)
        po.open()
        po.pppiglogin_Action("13011111101", "111111")
        sleep(3)
        po_debtcession = To_investdebtcession(self.driver)
        po_debtcession.pppiginvestdebtcession_Action1()
        sleep(3)
        po_debtcession.pppiginvestdebtcession_Action2()
        sleep(3)
        po_debtcession.pppiginvestdebtcession_Action3('111111')



# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
