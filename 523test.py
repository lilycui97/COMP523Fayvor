import pymysql

rds_host = "test.cgbkptzfvywp.us-east-2.rds.amazonaws.com" #connects to zach's test database b/c real database not populated + idk how to get in
username = "fakeuser"
password = "fakepass"
db_name = "dbtest"

conn = pymysql.connect(rds_host, user=username, port=3306, passwd=password, db=db_name)


try:
    cursor = conn.cursor()
	
	cr_query = """ SELECT firstname FROM Users """ #will be care providers    trying to do a really simple first name match + return all those who have same fn
	cp_query = """ SELECT firstname FROM Users """ #will be care receivers
	
	cursor.execute(cr_query)
	  
	rownumber = int(cursor.rowcount)	#putting sql query results into two seperate lists to compare

		for r in rownumber:
			row = cursor.fetchone()
			
			
	cursor.execute(cp_query)
	  
	 rownumber = int(cursor.rowcount)
	 
		for r in rownumber:
			row = cursor.fetchone()
			
			
    conn.commit()
	
	cursor.close()
    conn.close()
	
	for name in cr_query: 	#honestly this could just be it, simple compare if name exists in other list (tell me if you think too simple)
		if name in cp_query:
			print(name)
	
	

	except Error as error:
    print(error)
	