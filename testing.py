import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='HMS'
)

c = db.cursor()
c.execute('select password from accounts where username="admin"')

r = c.fetchall()


