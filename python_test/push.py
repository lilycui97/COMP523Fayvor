import pymysql

REGION = 'us-east-2'

rds_host = "test.cgbkptzfvywp.us-east-2.rds.amazonaws.com"
username = "master"
password = "DB_master"
db_name = "dbtest"

conn = pymysql.connect(rds_host, user=username, port=3306, passwd=password, db=db_name)

try:
    cursor = conn.cursor()

    # create a table 
    sql_query = """CREATE TABLE Users
        (id int(11) NOT NULL AUTO_INCREMENT,
         firstname varchar(255) COLLATE utf8_bin NOT NULL,
         lastname varchar(255) COLLATE utf8_bin NOT NULL,
         PRIMARY KEY (id) )
    """
   
    cursor.execute(sql_query)
    conn.commit()

except Exception as e:
	print("Exception occured:{}".format(e))

# insert 1 record
sql_query = "INSERT INTO Users (firstname, lastname) VALUES (%s, %s)"
cursor.execute(sql_query, ("first1", "last1"))

# insert all users in the list
users = [('firstname1', 'lastname1'),
         ('foo1', 'bar1'),
         ('foo2', 'bar2'),
         ('us1', 'er1'),
         ('firstname1', 'lastname2')]
for user in users:
    cursor.execute(sql_query, (user[0], user[1]))

conn.commit()
conn.close()
