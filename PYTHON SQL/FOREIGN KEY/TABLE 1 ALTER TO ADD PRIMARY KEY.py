import mysql.connector

# Replace with your database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "iqbal",
    "database": "new_database"
}

# Connect to the MySQL server
conn = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Specify the column name to be set as the primary key
primary_key_column = "column1"  # Replace with the name of the column you want as the primary key

# Execute an ALTER TABLE statement to add the primary key
alter_table_query = f"ALTER TABLE table1 ADD PRIMARY KEY ({primary_key_column})"
cursor.execute(alter_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Primary key added to 'table1' successfully.")