





import pymysql

dataBase = pymysql.connect(
	host = 'localhost',
	user = 'root',
	passwd = '*MYsql@17',
	db = 'project'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("SHOW DATABASES")

print("All Done")
