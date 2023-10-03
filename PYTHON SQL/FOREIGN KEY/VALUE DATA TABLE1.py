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
    (1, 'Value1', '2023-10-05'),
    (2, 'Value2', '2023-10-06'),
    (3, 'Value3', '2023-10-07'),
]

# Execute INSERT INTO statement to add data to the table
insert_query = """
    INSERT INTO table1 (column1, column2, column3)
    VALUES (%s, %s, %s)
"""

cursor.executemany(insert_query, data_to_insert)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data added to 'table1' successfully.")