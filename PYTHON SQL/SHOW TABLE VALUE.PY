import mysql.connector

# Replace these with your database credentials
host = "localhost"
user = "root"
password = "iqbal"
database = "new_database"

# Create a MySQL database connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the table name you want to query
table_name = "new_table"

# Construct the SQL query to select all records from the table
query = f"SELECT * FROM new_table"

# Execute the query
cursor.execute(query)

# Fetch all the records
records = cursor.fetchall()

# Iterate through the records and print them
for record in records:
    print(record)

# Close the cursor and database connection
cursor.close()
connection.close()