import pymysql

REGION = 'us-east-2'

rds_host = "test.cgbkptzfvywp.us-east-2.rds.amazonaws.com"
username = "master"
password = "DB_master"
db_name = "dbtest"

conn = pymysql.connect(rds_host, user=username, port=3306, passwd=password, db=db_name)
cursor = conn.cursor()

cursor.execute("select * from Users U")
for row in cursor:
	print(row)
cursor.execute("select * from Users U where U.id = 2")
for row in cursor:
	print("The following records are found:")
	print(row)
conn.close()