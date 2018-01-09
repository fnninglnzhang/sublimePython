# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium.webdriver.support.ui import WebDriverWait as Wa
from selenium.webdriver.support import expected_conditions as Ec
def wait_elements_contains(self, element):
	try:
		return Wa(self.driver, 10, 0.5).until(Ec.title_contains(element))
	except Exception as e:
		print(e)
		print('未找到对应元素')