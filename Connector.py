import mysql.connector as DB

mydb = DB.connect(host="localhost", user="root", passwd="toor", database="employees")

myCursor = mydb.cursor()

myCursor.execute("select * from employee")

result = myCursor.fetchall()

for i in result:
    print(i)
