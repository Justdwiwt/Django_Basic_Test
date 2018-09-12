import pymysql

pymysql.install_as_MySQLdb()

db = pymysql.connect("localhost", "root", "1234", "db_django")

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()
