import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='HMS'
)

c = db.cursor()
c.execute('select * from pms')

r = c.fetchall()

l = r[-1]
last_pid = l[0]
print(last_pid)