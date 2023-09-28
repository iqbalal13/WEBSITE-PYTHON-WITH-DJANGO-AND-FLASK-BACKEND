import mysql.connector

db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="iqbal"

)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase" )