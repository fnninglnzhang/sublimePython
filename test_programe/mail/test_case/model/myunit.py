#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
from .function import insert_img
import unittest
from .driver import browser


class MyTest(unittest.TestCase):


    def setUp(self):
        self.driver = browser()
        # self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


"""
#用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
"""