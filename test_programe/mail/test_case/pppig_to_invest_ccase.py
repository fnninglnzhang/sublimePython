#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_to_invest_page import To_invest
from page_object.pppig_product_details_page import Product_details
sys.path.append('./model')
sys.path.append('./page_obj')

class To_investTest(myunit.MyTest):

    def test_to_invest_success(self):
        '''投资'''
        po = LoginPage(self.driver)
        sleep(2)
        po.open()
        po.pppiglogin_Action("13011111101", "111111")
        sleep(3)
        po1 = To_invest(self.driver)
        # po1.pppiginvest_Action("200", "1111", "111111")
        po1.pppiginvest_Action1()
        sleep(2)
        """
        po2 = Product_details(self.driver)
        sleep(2)
        po2.product_Details_Action("200")
        sleep(2)
        """
        po1.pppiginvest_Action2("300")
        sleep(2)
        po1.pppiginvest_Action3("1111")
        sleep(2)
        po1.pppiginvest_Action4("111111")
        sleep(2)
        function.insert_img(self.driver, "success2.png")


# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
