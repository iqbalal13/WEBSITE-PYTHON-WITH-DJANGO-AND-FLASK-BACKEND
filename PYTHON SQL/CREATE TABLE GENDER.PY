import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iqbal",
    database="testdatabase"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE genders(name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM ('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL  AUTO_INCREMENT)")

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()