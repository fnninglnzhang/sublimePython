# !/usr/bin/python3
import pymysql as MySQLdb  # 这里是python3的写法 如果是python2.x的话，import MySQLdb

host = 'rm-2zerok14p432v4942o.mysql.rds.aliyuncs.com'
user = 'test'
passwd = '123456'
port = 3306
db = 'zsch_test1'
charset = 'utf8'


class SelectMySQL(object):
	def select_Data(self, sql):
		result = []
		try:
			# 和数据库建立连接
			conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db,  charset='utf8', )
			cur = conn.cursor()                            # 用来获得python执行Mysql命令的方法
			cur.execute(sql)                               # 真正执行MySQL语句，即查询表的数据
			alldata = cur.fetchall()                       # 接收全部的返回结果行
			# print(alldata)
			for rec in alldata:
				result.append(rec[0])                      # 注意，这里只是把查询出来的第一列数据保存到结果中了,如果是多列的话，稍微修改下就ok了
		except Exception as e:
			print('Error msg: ' + e)
		finally:
			cur.close()
			conn.close()

		return result

	"""
	def get_Result(self, sql, filename):
		print(sql)
		results = self.select_Data(sql)
		print('The amount of datas: %d' % (len(results)))
		with open(filename, 'w') as f:
			for result in results:
				f.write(str(result) + '\n')
		print('Data write is over!')
		return results
	"""


def get_Result(self, sql):
	print(sql)
	results = self.select_Data(sql)
	"""
	print('The amount of datas: %d' % (len(results)))
	with open(filename, 'w') as f:
		for result in results:
			f.write(str(result) + '\n')
	print('Data write is over!')
	"""
	return results



"""
# 用于验证该脚本
if __name__ == '__main__':
	sql = "SELECT * FROM user_main WHERE mobile = 13011111103"
	select = SelectMySQL()
	# 文件保存路径
	result1 = select.get_Result(sql, 'D:\\namemsg.txt')
	print(result1)
"""