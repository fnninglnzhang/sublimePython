#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import unittest, random, sys
from model import myunit, function
from page_object.pppig_login_page import LoginPage
from model.log import log
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_0login_success(self):
        '''用户名、密码正确,登录成功'''
        try:
            po = LoginPage(self.driver)
            po.open()
            username = '13011111117'
            po.pppiglogin_noclose_Action(username, '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_success_user(), 'pppig'+username)                             # 登录成功后断言右上角的用户信息
            print(po.pppiglogin_success_user()+'登陆成功')                                      # 打印用户登录成功
            function.insert_img(self.driver, "pppig_login_success.png")                       # 截图
            mylog = log()
            mylog.setMSG('info', '0.输入正确的用户名和密码，点击提交按钮，验证是否能正确登录。（正常输入）')
        except BaseException as e:
            print(e)
            mylog = log()
            mylog.setMSG('error', '执行失败，发生错误')

    """

    def test_1No_user_and_pwd_failure(self):
        '''什么都不输入，点击提交按钮，看提示信息。（非空检查）'''
        try:
            po = LoginPage(self.driver)                                                  # 实例化LoginPage这个类
            po.open()                                                                    # 调用打开网址的方法
            po.pppiglogin_noclose_Action('', '')                                         # 调用封装好的登陆
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '账号不能为空!')                # 断言错误信息
            print('\n'+'登录失败: ' + po.pppiglogin_erro_hint())                        # 打印报错信息
            function.insert_img(self.driver, "no_user_and_pwd_failure.png")           # 截图
            mylog = log()
            mylog.setMSG('info', '0.什么都不输入，点击提交按钮，看提示信息(账号不能为空)。（非空检查）')
            print('\n' + '什么都不输入，点击提交按钮，提示：   账号不能为空')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)


    def test_2_1user_name_wrong(self):
        '''用户名错误'''
        try:
            po = LoginPage(self.driver)
            po.open()
            po.pppiglogin_noclose_Action('13111111101', '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '手机号不存在!')                               # 断言错误信息
            print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())                                     # 打印报错信息
            function.insert_img(self.driver, "2_1user_name_wrong.png")
            mylog = log()
            mylog.setMSG('info', '2.输入错误的用户名, 验证登录会失败，并且提示相应的错误信息(手机号不存在)。（错误校验）')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)

    def test_2_2pass_word_wrong(self):
            '''用户名正确，密码错误'''
            try:
                po = LoginPage(self.driver)
                po.open()
                po.pppiglogin_noclose_Action('13011111101', '211111')
                sleep(2)
                self.assertEqual(po.pppiglogin_erro_hint(), '密码错误!')  # 断言错误信息
                print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())  # 打印报错信息
                function.insert_img(self.driver, "2_2pass_word_wrong.png")
                mylog = log()
                mylog.setMSG('info', '2.输入错误的密码, 验证登录会失败，并且提示相应的错误信息(密码错误)。（错误校验）')
            except BaseException as e:
                mylog = log()
                mylog.setMSG('error', e)




    def test_login_to_page(self):
        # 登录成功后能否能否跳转到正确的页面
        print('\n' + '登录成功后能否能否跳转到正确的页面')


    def test_4_1username_so_long(self):
        '''用户名太长，应该怎么处理（安全性）'''
        try:
            po = LoginPage(self.driver)
            po.open()
            po.pppiglogin_noclose_Action('13011111101111111', '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '账号不存在!')  # 断言错误信息
            print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())  # 打印报错信息
            function.insert_img(self.driver, "3_1username_so_long.png")
            mylog = log()
            mylog.setMSG('info', '用户名太长，应该怎么处理(账号不存在)（安全性）')
            print('\n' + '用户名过长未做限制')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)


    def test_4_2username_so_short(self):
        '''用户名太短，应该怎么处理'''
        try:
            po = LoginPage(self.driver)
            po.open()
            po.pppiglogin_noclose_Action('13011111', '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '手机号不存在!')           # 断言错误信息
            print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())                 # 打印报错信息
            function.insert_img(self.driver, "3_2username_so_short.png")
            mylog = log()
            mylog.setMSG('info', '用户名太短，应该怎么处理(账号不存在)（安全性）')
            print('\n' + '用户名过短未做任何提示')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)


    def test_5_1username_in_space(self):
        '''用户名和密码，中有特殊字符（比如空格），和其他非英文的情况（是否做了过滤）'''
        try:
            po = LoginPage(self.driver)
            po.open()
            po.pppiglogin_noclose_Action('1301  1111101', '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '账号不存在!')           # 断言错误信息
            print('\n' + '登录失败: ' + po.pppiglogin_erro_hint())                 # 打印报错信息
            function.insert_img(self.driver, "username_in_space.png")
            mylog = log()
            mylog.setMSG('info', '用户名中有空格（是否做了过滤）   (否)）')
            print('\n' + '中间空格未做过滤')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)

    def test_Remember_the_username_and_password(self):
        # 记住用户名的功能
        pass

    def test_7Remember_the_username(self):
          # 登陆失败后，不能记录密码，用户名可以保存
          pass
    

    def test_8_1_username_before_space(self):
        '''用户名前有空格的处理'''
        try:
            po = LoginPage(self.driver)
            po.open()
            username = '              13011111103'
            po.pppiglogin_noclose_Action(username, '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_success_user(), username)           # 断言用户登录到系统
            print('\n' + username + '登录成功')                               # 打印信息
            function.insert_img(self.driver, "8_1_username_before_space.png")
            mylog = log()
            mylog.setMSG('info', '前面出现空格做了过滤（是否做了过滤）   (是)）')
            print('\n' + '前面出现空格做了过滤')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)


    def test_8_2_username_after_space(self):
        # 用户名后有空格的处理
        try:
            po = LoginPage(self.driver)
            po.open()
            username = '13011111103              '
            po.pppiglogin_noclose_Action(username, '111111')
            sleep(2)
            self.assertEqual(po.pppiglogin_success_user(), username)           # 断言用户登录到系统
            print('\n' + username + '登录成功')                               # 打印信息
            function.insert_img(self.driver, "8_2_username_after_space.png")
            mylog = log()
            mylog.setMSG('info', '后面出现空格做了过滤（是否做了过滤）   (是)）')
            print('\n' + '后面出现空格做了过滤')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)

    def test_8_3_password_before_space(self):
        '''密码前有空格的处理'''
        try:
            po = LoginPage(self.driver)
            po.open()
            password = '       111111'
            po.pppiglogin_noclose_Action('13011111101', password)
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '密码错误!')           # 断言用户登录到系统
            print('\n' + po.pppiglogin_erro_hint())                               # 打印信息
            function.insert_img(self.driver, "8_3_password_before_space.png")
            mylog = log()
            mylog.setMSG('info', '密码前面出现空格是否做过滤（是否做了过滤）   (否)）')
            print('\n' + '密码前面出现空格未做过滤')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)


    def test_8_4_password_after_space(self):
        '''密码后有空格的处理'''
        try:
            po = LoginPage(self.driver)
            po.open()
            password = '111111       '
            po.pppiglogin_noclose_Action('13011111101', password)
            sleep(2)
            self.assertEqual(po.pppiglogin_erro_hint(), '密码错误!')           # 断言用户登录到系统
            print('\n' + po.pppiglogin_erro_hint())                               # 打印信息
            function.insert_img(self.driver, "8_4_password_after_space.png")
            mylog = log()
            mylog.setMSG('info', '密码后面出现空格是否做过滤（是否做了过滤）   (否)）')
            print('\n' + '密码后面出现空格未做过滤')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)

    def test_12Password_Encryption(self):
        # 密码是否加密显示（星号圆点等）
        mylog = log()
        mylog.info('密码是否加密显示（星号圆点等）'+ '\n' + '登录需要验证码的，输入完用户名和密码后，验证码为必填项'
                    + '\n' + '牵扯到验证码的，还要考虑文字是否扭曲过度导致辨认难度大，考虑颜色（色盲使用者），"刷新"或"换一个"按钮是否好用'
                   + '\n' + '输入密码的时候，大写键盘开启的时候要有提示信息' + '\n' + '登录失败的提示信息需要高亮处理' )
        print('密码是否加密显示（星号圆点等）')
        print('登录需要验证码的，输入完用户名和密码后，验证码为必填项')
        print('牵扯到验证码的，还要考虑文字是否扭曲过度导致辨认难度大，考虑颜色（色盲使用者），"刷新"或"换一个"按钮是否好用')
        print('输入密码的时候，大写键盘开启的时候要有提示信息')

    def test_more_wrong_pwd(self):
        '''输入错指定次数后，账号锁定，需要做解锁处理'''
        try:
            f = open('../date/pwdwrong.txt')
            lines = f.readlines()
            for line in lines:
                username = line.split(',')[0]
                password = line.split(',')[1]
                po = LoginPage(self.driver)
                # sleep(1)
                po.open()
                po.pppiglogin_noclose_Action(username, password)
                sleep(1)
                # self.assertEqual(po.pppiglogin_erro_hint(), '密码错误!'
                if po.pppiglogin_erro_hint() == '密码错误!':
                    # print('\n' + "登录失败，原因： " + "密码错误")
                    pass
                elif po.pppiglogin_erro_hint() == '账号已被锁定请稍后再试!':
                    print('\n' + "登录失败，原因： " + "账号已被锁定请稍后再试!")
                else:
                    print('不明原因')
                function.insert_img(self.driver, "more_wrong_pwd.png")
                mylog = log()
                mylog.setMSG('info', '输入错指定次数后，账号锁定，需要做解锁处理')
                print('\n' + '输入错指定次数后，账号锁定，需要做解锁处理')
        except BaseException as e:
            mylog = log()
            mylog.setMSG('error', e)
    """





# 用于验证该脚本是否有效
if __name__ == "__main__":
    unittest.main()
