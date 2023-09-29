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

# Replace "your_table_name" with the name of the table you want to view
table_name = "person"
query = "SELECT * FROM person"

# Execute the query
cursor.execute(query)

# Fetch and print the data
for row in cursor.fetchall():
    print(row)

# Close the cursor and the connection
cursor.close()
connection.close()