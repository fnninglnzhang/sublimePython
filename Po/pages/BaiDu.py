__author__ = 'HLTQ'
from selenium import webdriver


class pages(object):
    def __init__(self, driver, base_url="http://www.baidu.com"):
        self.driver = driver
        self.url = base_url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click_button(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title




