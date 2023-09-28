import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="iqbal",
    database="testdatabase"
)

mycursor = db.cursor()

# Alter the table to add a new column 'personID' as an integer primary key
alter_query = "ALTER TABLE Person ADD COLUMN personID INT AUTO_INCREMENT PRIMARY KEY"
mycursor.execute(alter_query)

db.commit()  # Commit the changes to the database

# Close the cursor and the database connection
mycursor.close()
db.close()