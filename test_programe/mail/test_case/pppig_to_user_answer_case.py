# -*- coding: UTF-8 -*-
import unittest, random, sys
from time import sleep

from model import myunit, function
from page_object.pppig_login_page import LoginPage
from page_object.pppig_to_user_answer_page import To_User_Snswer_page

class pppigToUserAnswer(myunit.MyTest):

    def test_pppig_user_answer(self):
        tusp = To_User_Snswer_page(self.driver)
        lp = LoginPage(self.driver)
        sleep(2)
        #登录
        lp.open()
        sleep(2)
        lp.pppiglogin_noclose_Action("13011111101", "111111")
        sleep(4)
        #风险测评
        tusp.open()
        sleep(2)
        tusp.pppigToUserAnswer_Action1(4,4,1,2,3,4,4)
        function.insert_img(self.driver, "success3.png")

#验证
if __name__ == "__main__":
    unittest.main()



