__author__ = 'HLTQ'
from selenium import webdriver
from Po.pages.BaiDu import pages
from selenium.webdriver.common.by import By


class Serach_p(pages):
    # 百度输入框
    search_input = (By.ID, "kw")
    search_button = (By.ID, "su")

    def __init__(self, driver, base_url="http://www.baidu.com"):
        self.driver = driver
        self.url = base_url

    def gotoBaiduHome(self):
        print(self.url)
        self.driver.get(self.url)

    def shuRuText(self, text):
        self.input_text(self.search_input, text)

    def click_SouSuo(self):
        self.click_button(self.search_button)








