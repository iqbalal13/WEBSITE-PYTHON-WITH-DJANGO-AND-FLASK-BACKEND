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

# Define sample data to insert
data_to_insert = [
    (1, 'iqbal', '20'),
    (2, 'al', '21'),
    (3, 'banawi', '22'),
]

# Execute INSERT INTO statement to add data to your_table_name
insert_query = """
    INSERT INTO new_table (id, name, age)
    VALUES (%s, %s, %s)
"""

cursor.executemany(insert_query, data_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data added to 'your_table_name' successfully.")