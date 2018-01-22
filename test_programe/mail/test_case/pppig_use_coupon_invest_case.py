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
        try:
            po = LoginPage(self.driver)
            sleep(2)
            po.open()
            username = '13011111101'
            po.pppiglogin_noclose_Action(username, "111111")
            sleep(2)
            po.open_R('/recommendloanDetail?loanId=35377')
            po1 = To_invest(self.driver)
            sleep(2)
            amount = '100'
            po1.pppiguse_ratecoupon_Invest_Action(amount)

            sleep(2)
            po1.pppiginvest_Action3("1111")
            sleep(2)
            po1.pppiginvest_Action4("111111")
            print('用户'+username+'投资'+amount+'元'+'  投资成功')
        except BaseException as e:
            print(e)



# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
