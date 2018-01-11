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
"""
f = open('D:\\1.txt')
lines=f.readlines()
for line in lines:
        username=line.split(',')[0]
        password=line.split(',')[1]
        在for循环内执行登录等等操作
#类似这样就行，账号密码一个一行，用逗号分开就行


f = open('D:\\1.txt')
lines=f.readlines()
for line in lines:
        username=line.split(',')[0]
        password=line.split(',')[1]
        在for循环内执行登录等等操作
#类似这样就行，账号密码一个一行，用逗号分开就行



"""