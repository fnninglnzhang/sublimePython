#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_to_invest_page import To_invest
from page_object.pppig_product_details_page import Product_details
loanId = 36068
   # 标的 URL
print('/recommendloanDetail?loanId={}'.format(loanId))





# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
