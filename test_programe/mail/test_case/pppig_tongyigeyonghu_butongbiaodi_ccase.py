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
        '''同一个用户不同标的'''
        try:
            # for i in range(1, 10):
                po = LoginPage(self.driver)
                sleep(2)
                po.open()
                username = '13011111101'
                po.pppiglogin_noclose_Action(username, "111111")
                sleep(2)
                po.open_R('/recommendloanDetail?loanId=36210')
                po1 = To_invest(self.driver)
                sleep(2)
                amount = '1000'
                # 使用加息券
                # po1.pppiguse_ratecoupon_Invest_Action(amount)
                # 使用红包
                # po1.pppiguse_Redpacket_Invest_Action(amount)
                # po1.pppiguse_no_Coupon_Invest_Action(amount)
                # 不使用卡券余额全投
                po1.pppiguse_NoRedpacket_Invest_All_Action()
                # 余额全投——使用红包——即刻投资
                # po1.pppiguse_Redpacket_Invest_All_Action()
                # 使用加息券余额全投
                # po1.pppiguse_Rate_Coupon_Invest_All_Action()
                sleep(2)
                po1.pppiginvest_Action3("1111")
                sleep(2)
                po1.pppiginvest_Action4("111111")
                sleep(2)
                poclose = LoginPage(self.driver)
                poclose.pppiglogin_close_button()
                print('用户'+username+'投资'+amount+'元'+'投资成功')
        except BaseException as e:
            print(e)



# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
