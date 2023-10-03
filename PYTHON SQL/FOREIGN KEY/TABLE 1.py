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

# Specify the new table name and its columns
new_table_name = "table1"
create_table_query = """
    CREATE TABLE IF NOT EXISTS {} (
        column1 INT,
        column2 VARCHAR(255),
        column3 DATE
    )
""".format(new_table_name)

cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Table '{new_table_name}' created successfully without a primary key.")