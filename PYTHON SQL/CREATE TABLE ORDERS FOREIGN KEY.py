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

# Create a table
table_name = "orders"
create_table_query = """
    CREATE TABLE orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        order_date DATE,
        total_amount DECIMAL(10, 2),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
"""
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(" table created successfully.")