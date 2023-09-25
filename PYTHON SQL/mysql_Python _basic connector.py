import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdatabase"
)

mycursor = db.cursor()