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
            po.pppiglogin_noclose_Action("13446576460", "111111")              # 用户登陆
            sleep(2)
            po.open_R('/recommendloanDetail?loanId=35378')                    # 标的 URL
            po1 = To_invest(self.driver)
            sleep(2)
            # po1.pppiguse_no_Coupon_Invest_Action('100000')                          # 不使用卡券投资
            po1.pppiguse_ratecoupon_Invest_Action('20000')                        # 投资金额   使用加息券
            # po1.pppiguse_Redpacket_Invest_Action(100)                            # 投资金额   使用红包
            # po1.pppiguse_Redpacket_Invest_All_Action()                           # 余额全投   使用红包
            # po1.pppiguse_Rate_Coupon_Invest_All_Action()                         # 余额全投   使用加息券

            sleep(2)
            po1.pppiginvest_Action3("1111")                                       # 图形验证码
            sleep(2)
            po1.pppiginvest_Action4("111111")                                     # 交易密码
            function.insert_img(self.driver, "invest_success.png")               # 截图
            print('投资成功')
        except BaseException as e:
            print(e)



# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
