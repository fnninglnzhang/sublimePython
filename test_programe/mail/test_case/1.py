# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = "2016/5/19 18:46"

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
driver = webdriver.Ie()
driver.get('http://www.baidu.com')
builder = ActionChains(driver)
builder.key_down(Keys.F12).perform()
sleep(5)
driver.quit()