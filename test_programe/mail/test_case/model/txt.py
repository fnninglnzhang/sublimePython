# !/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import os, time
import codecs
class Reader_txt():
	"""
		# def str_reader_txt(address):
			# fp = codecs.open(address, 'r', "gb18030")
		"""
	def reader_Txt_Date(self, address):
		fp = codecs.open(address, 'r', "gb18030")
		# fp=open(address,'r')
		users = []
		pwds = []
		lines = fp.readlines()
		for data in lines:
			name, pwd = data.split(',')
			name = name.strip(' \t\r\n')
			pwd = pwd.strip(' \t\r\n')
			users.append(name)
			pwds.append(pwd)
			print("user:%s(len(%d))" % (name, len(name)))
			print("pwd:%s(len(%d))" % (pwd, len(pwd)))
		return users, pwds
		# fp.close()

if __name__ == "__main__":
	a = Reader_txt()
	a.reader_Txt_Date('D:\\name.txt')
