import pymysql

database=input("请输入想连接的数据库:")

if database==None:
    db=pymysql.connect("localhost","root","123456","demo")
else:
    db = pymysql.connect("localhost", "root", "123456", database)

cursor=db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()

print("Database version is %s"%data)

db.close()