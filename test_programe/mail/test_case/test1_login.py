#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from model.log import log
from page_object.to_login_page import To_login
from page_object.mail_page import MailPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):
    """
    def test_login_success(self):
        '''用户名、密码正确,登录成功'''
        try:
            po = LoginPage(self.driver)
            po.open()
            username = '13011111101'
            po.pppiglogin_noclose_Action(username, '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_success_user(), username)                             # 登录成功后断言右上角的用户信息
            print(po.pppiglogin_success_user()+'登陆成功')                                      # 打印用户登录成功
            function.insert_img(self.driver, "pppig_login_success.png")                       # 截图
        except BaseException as e:
            mylog = log()
            mylog.error(e)
            print(e)
    """

    """
    def test_No_user_and_pwd_failure(self):
        '''什么都不输入，点击提交按钮'''
        po = LoginPage(self.driver)
        po.open()
        po.pppiglogin_noclose_Action('', '')
        sleep(2)
        self.assertEqual(po.pppiglogin_erro_hint(), '账号不能为空!')   # 断言错误信息
        print('\n'+'登录失败: ' + po.pppiglogin_erro_hint())                       # 打印报错信息
        # function.insert_img(self.driver, "no_user_and_pwd_failure.png")
    """

    """
    def test_user_name_wrong(self):
        '''用户名错误'''
        po = LoginPage(self.driver)
        po.open()
        po.pppiglogin_noclose_Action('13111111101', '111111')
        sleep(2)
        self.assertEqual(po.pppiglogin_erro_hint(), '手机号不存在!')  # 断言错误信息
        print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())  # 打印报错信息
        # function.insert_img(self.driver, "user_name_wrong.png")
    """

    """
    def test_pass_word_wrong(self):
            '''用户名正确，密码错误'''
            po = LoginPage(self.driver)
            po.open()
            po.pppiglogin_noclose_Action('13011111101', '211111')
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '密码错误!')  # 断言错误信息
            print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())  # 打印报错信息
            # function.insert_img(self.driver, "pass_word_wrong.png")
    """

    """
    def test_login_to_page(self):
        # 登录成功后能否能否跳转到正确的页面
        pass
    """
    """
    def test_username_so_long(self):
        '''用户名太长，应该怎么处理（安全性）'''
        po = LoginPage(self.driver)
        po.open()
        po.pppiglogin_noclose_Action('13011111101111111', '111111')
        sleep(2)
        self.assertEqual(po.pppiglogin_erro_hint(), '账号不存在!')  # 断言错误信息
        print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())  # 打印报错信息
        # function.insert_img(self.driver, "username_so_long.png")
    """
    """
    def test_username_so_short(self):
        '''用户名太短，应该怎么处理'''
        po = LoginPage(self.driver)
        po.open()
        po.pppiglogin_noclose_Action('13011111', '111111')
        sleep(2)
        self.assertEqual(po.pppiglogin_erro_hint(), '手机号不存在!')           # 断言错误信息
        print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())                 # 打印报错信息
        # function.insert_img(self.driver, "username_so_short.png")
    """
    """
    def test_username_in_space(self):
        '''用户名和密码，中有特殊字符（比如空格），和其他非英文的情况（是否做了过滤）'''
        po = LoginPage(self.driver)
        po.open()
        po.pppiglogin_noclose_Action('1301  1111101', '111111')
        sleep(2)
        self.assertEqual(po.pppiglogin_erro_hint(), '账号不存在!')           # 断言错误信息
        print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())                 # 打印报错信息
        # function.insert_img(self.driver, "username_in_space.png")
    """
    """
    def test_Remember_the_username_and_password(self):
        # 记住用户名的功能
        pass
    """





# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
