#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_goRegister_page import GoRegister
from page_object.pppig_open_the_depository_page import Opendepository
from model.oldconnect_mysql import *



class LoginshimingTest(myunit.MyTest):

    def test_login_shiming_success(self):
        '''登录、实名'''
