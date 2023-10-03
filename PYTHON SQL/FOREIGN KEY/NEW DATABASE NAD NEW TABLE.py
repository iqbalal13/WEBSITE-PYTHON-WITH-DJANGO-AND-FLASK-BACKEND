import mysql.connector

# Replace with your database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "iqbal"
}

# Connect to the MySQL server
conn = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a new database (if it doesn't exist)
new_database_name = "new_database"
create_database_query = f"CREATE DATABASE IF NOT EXISTS {new_database_name}"
cursor.execute(create_database_query)

# Switch to the new database
cursor.execute(f"USE {new_database_name}")

# Create a new table with a primary key
new_table_name = "new_table"
create_table_query = """
    CREATE TABLE IF NOT EXISTS new_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
"""
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database '{new_database_name}' and table '{new_table_name}' created successfully.")