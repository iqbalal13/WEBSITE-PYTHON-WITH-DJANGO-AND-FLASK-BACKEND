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

# Define sample data to insert
order_data = [
    (1, '2023-10-02', 100.50),
    (2, '2023-10-03', 75.25),
    (3, '2023-10-04', 200.00),
]

# Insert data into the "orders" table
insert_query = "INSERT INTO orders (user_id, order_date, total_amount) VALUES (%s, %s, %s)"
cursor.executemany(insert_query, order_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into the 'orders' table successfully.")