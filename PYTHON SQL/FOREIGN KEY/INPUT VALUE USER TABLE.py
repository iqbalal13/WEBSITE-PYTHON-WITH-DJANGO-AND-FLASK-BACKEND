import mysql.connector

# Replace with your database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "iqbal",
    "database": "testdatabase"
}

# Connect to the MySQL server
conn = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define some sample data to insert
user_data = [
    ("Iqbal", "iqbal@example.com"),
    ("jilan", "jilan@example.com"),
    ("jasmine", "jasmine@example.com"),
]

# Insert data into the "users" table
insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
cursor.executemany(insert_query, user_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully.")