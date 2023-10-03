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

# Perform a RIGHT JOIN (effectively) between "orders" and "users" tables
right_join_query = """
    SELECT users.username, orders.order_date, orders.total_amount
    FROM orders
    LEFT JOIN users ON orders.user_id = users.id
"""

cursor.execute(right_join_query)

# Fetch all rows
result = cursor.fetchall()

# Display the retrieved data
if result:
    print("Username | Order Date | Total Amount")
    print("-----------------------------------")
    for row in result:
        username, order_date, total_amount = row
        print(f"{username} | {order_date} | {total_amount:.2f}" if username is not None else f"- | - | -")
else:
    print("No matching data found")

# Close the connection
conn.close()