import pymysql

database=input("请输入想连接的数据库")

if database==None:
    db=pymysql.connect("localhost","root","123456","demo")
else:
    db = pymysql.connect("localhost", "root", "123456", database)