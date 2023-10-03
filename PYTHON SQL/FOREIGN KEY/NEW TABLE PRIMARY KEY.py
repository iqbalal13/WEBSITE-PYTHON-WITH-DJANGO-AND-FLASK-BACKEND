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

# Specify the table name and the column to be set as the primary key
table_name = "your_table_name"  # Replace with your actual table name
primary_key_column = "id"  # Replace with the name of your primary key column

# Execute an ALTER TABLE statement to add the primary key
alter_table_query = f"ALTER TABLE {table_name} ADD PRIMARY KEY ({primary_key_column})"
cursor.execute(alter_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Primary key added to the '{table_name}' table successfully.")