#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_to_invest_page import To_invest
from page_object.pppig_product_details_page import Product_details


loanId = 38860

class To_investTest(myunit.MyTest):

    def test_aredpack_invest_success(self):
        '''使用红包投资'''
        try:
            f = open('../date/invest/invest3.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]
                investmentamount = line.split(',')[1]
                po = LoginPage(self.driver)
                sleep(2)
                po.open()
                po.pppiglogin_noclose_Action(username, "111111")              # 用户登陆
                sleep(2)
                # po.open_R('/recommendloanDetail?loanId=35925')                    # 标的 URL
                po.open_R('/recommendloanDetail?loanId={}'.format(loanId))
                po1 = To_invest(self.driver)
                sleep(2)
                # 使用加息券
                # po1.pppiguse_ratecoupon_Invest_Action(investmentamount)
                # 使用红包
                po1.pppiguse_Redpacket_Invest_Action(investmentamount)
                # 不使用卡券
                # po1.pppiguse_no_Coupon_Invest_Action(investmentamount)
                # 不使用卡券余额全投
                # po1.pppiguse_NoRedpacket_Invest_All_Action()                       # 余额全投   使用加息券
                sleep(2)
                po1.pppiginvest_Action3("1111")                                       # 图形验证码
                sleep(2)
                po1.pppiginvest_Action4("111111")                                     # 交易密码
                sleep(2)
                poclose = LoginPage(self.driver)
                poclose.pppiglogin_close_button()
                function.insert_img(self.driver, "invest_success.png")               # 截图
                print('投资成功')

        except BaseException as e:
            print(e)

    def test_bcoupon_invest_success(self):
        '''使用加息券投资'''
        try:
            f = open('../date/invest/invest2.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]
                investmentamount = line.split(',')[1]
                po = LoginPage(self.driver)
                sleep(2)
                po.open()
                po.pppiglogin_noclose_Action(username, "111111")  # 用户登陆
                sleep(2)
                # po.open_R('/recommendloanDetail?loanId=35925')  # 标的 URL
                po.open_R('/recommendloanDetail?loanId={}'.format(loanId))
                po1 = To_invest(self.driver)
                sleep(2)
                # 使用加息券
                po1.pppiguse_ratecoupon_Invest_Action(investmentamount)
                # 使用红包
                # po1.pppiguse_Redpacket_Invest_Action(investmentamount)
                # 不使用卡券
                # po1.pppiguse_no_Coupon_Invest_Action(investmentamount)
                # 不使用卡券余额全投
                # po1.pppiguse_NoRedpacket_Invest_All_Action()  # 余额全投   使用加息券
                sleep(2)
                po1.pppiginvest_Action3("1111")  # 图形验证码
                sleep(2)
                po1.pppiginvest_Action4("111111")  # 交易密码
                sleep(2)
                poclose = LoginPage(self.driver)
                poclose.pppiglogin_close_button()
                function.insert_img(self.driver, "invest_success.png")  # 截图
                print('投资成功')

        except BaseException as e:
            print(e)

    def test_cnopack_invest_success(self):
        '''无卡券余额全投'''
        try:
            f = open('../date/invest/invest4.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]
                investmentamount = line.split(',')[1]
                po = LoginPage(self.driver)
                sleep(2)
                po.open()
                po.pppiglogin_noclose_Action(username, "111111")  # 用户登陆
                sleep(2)
                # po.open_R('/recommendloanDetail?loanId=35925')  # 标的 URL
                po.open_R('/recommendloanDetail?loanId={}'.format(loanId))
                po1 = To_invest(self.driver)
                sleep(2)
                # 使用加息券
                # po1.pppiguse_ratecoupon_Invest_Action(investmentamount)
                # 使用红包
                # po1.pppiguse_Redpacket_Invest_Action(investmentamount)
                # 不使用卡券
                # po1.pppiguse_no_Coupon_Invest_Action(investmentamount)
                # 不使用卡券余额全投
                po1.pppiguse_NoRedpacket_Invest_All_Action()  # 余额全投   使用加息券
                sleep(2)
                po1.pppiginvest_Action3("1111")  # 图形验证码
                sleep(2)
                po1.pppiginvest_Action4("111111")  # 交易密码
                sleep(2)
                poclose = LoginPage(self.driver)
                poclose.pppiglogin_close_button()
                function.insert_img(self.driver, "invest_success.png")  # 截图
                print('投资成功')

        except BaseException as e:
            print(e)
    """
    def test_all_invest_success(self):
        '''全投'''
        try:
            f = open('../date/invest/invest3.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]
                investmentamount = line.split(',')[1]
                po = LoginPage(self.driver)
                sleep(2)
                po.open()
                po.pppiglogin_noclose_Action(username, "111111")  # 用户登陆
                sleep(2)
                po.open_R('/recommendloanDetail?loanId=35786')  # 标的 URL
                po1 = To_invest(self.driver)
                sleep(2)
                # 使用加息券
                # po1.pppiguse_ratecoupon_Invest_Action(investmentamount)
                # 使用红包
                # po1.pppiguse_Redpacket_Invest_Action(investmentamount)
                # 不使用卡券
                # po1.pppiguse_no_Coupon_Invest_Action(investmentamount)
                # 不使用卡券余额全投
                po1.pppiguse_NoRedpacket_Invest_All_Action()  # 余额全投
                sleep(2)
                po1.pppiginvest_Action3("1111")  # 图形验证码
                sleep(2)
                po1.pppiginvest_Action4("111111")  # 交易密码
                sleep(2)
                poclose = LoginPage(self.driver)
                poclose.pppiglogin_close_button()
                function.insert_img(self.driver, "invest_success.png")  # 截图
                print('投资成功')

        except BaseException as e:
            print(e)
    """


# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
