import mysql.connector
from datetime import datetime

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iqbal",
    database="testdatabase"
)

# Create a cursor
mycursor = db.cursor()

# Define the data you want to insert
data_to_insert = ("Alice", datetime.now(), "F")

# SQL query to insert data into the table
insert_query = "INSERT INTO test (name, created, gender) VALUES (%s, %s, %s)"

# Execute the insert query with the data
mycursor.execute(insert_query, data_to_insert)

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()