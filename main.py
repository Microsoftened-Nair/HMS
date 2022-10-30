import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database='HMS',
)
def PMS():
  mycursor = mydb.cursor()
  mycursor.execute("describe pms")
  myresult = mycursor.fetchall()

  lst = []
  for x in myresult:
    lst.append(x[0])

  mycursor.execute("select * from pms")
  myresult = mycursor.fetchall()

  for x in myresult:
    pass