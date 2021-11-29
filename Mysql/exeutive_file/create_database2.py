"""
创建demo数据库

"""

import pymysql

db=pymysql.connect("localhost","root","123456")

cursor=db.cursor()

cursor.execute("CREATE DATABASE test")

db.close()