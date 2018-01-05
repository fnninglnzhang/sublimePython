__author__ = 'HLTQ'
from selenium import webdriver
import unittest
from Po.pages.Search_page import Serach_p
from selenium.webdriver.support import expected_conditions as EC

class Test_baidu(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Ie()

    def testSearch(self):
        # temp = Serach_p(self.driver, base_url="http://www.baidu.com")
        temp = Serach_p(self.driver)
        temp.gotoBaiduHome()
        temp.shuRuText("senlenium")
        temp.click_SouSuo()
        print('田奇真牛逼')

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()





