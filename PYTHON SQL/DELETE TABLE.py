import mysql.connector

# Replace these values with your own database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "iqbal",
    "database": "testdatabase"
}

# Establish a connection to the database
connection = mysql.connector.connect(**db_config)

# Create a cursor
cursor = connection.cursor()

# Replace "your_table_name" with the name of the table you want to delete
table_name = "person"
drop_table_query = "DROP TABLE person"

# Execute the DROP TABLE query
cursor.execute(drop_table_query)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()