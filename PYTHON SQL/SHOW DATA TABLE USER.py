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

# Select all data from the "users" table
select_query = "SELECT * FROM users"
cursor.execute(select_query)

# Fetch all rows
user_data = cursor.fetchall()

# Display the retrieved data
if user_data:
    print("ID  | Username | Email")
    print("-----------------------")
    for row in user_data:
        user_id, username, email = row
        print(f"{user_id} | {username} | {email}")
else:
    print("No data found in the 'users' table")

# Close the connection
conn.close()