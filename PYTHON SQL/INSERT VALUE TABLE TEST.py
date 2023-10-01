import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iqbal",
    database="testdatabase"

)

mycursor = db.cursor()

#mycursor.execute("CREATE TABLE test(name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM ('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL  AUTO_INCREMENT)")
mycursor.execute("INSERT INTO test (name, created, gender) VALUES(%s,%s,%s)",("iqbal", datetime.now(),"M"))

db.commit()


