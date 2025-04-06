import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Moghithm@22",
    database="testdb"
)
print(myDB)