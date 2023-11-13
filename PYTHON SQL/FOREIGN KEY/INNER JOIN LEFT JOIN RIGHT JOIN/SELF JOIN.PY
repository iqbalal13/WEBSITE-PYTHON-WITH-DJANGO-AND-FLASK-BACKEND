import mysql.connector

# Replace these with your database credentials
host = "localhost"
user = "root"
password = "iqbal"
database = "new_database"

# Create a MySQL database connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Define the SQL query for the self-join
query = """
SELECT e.employee_id, e.employee_name, m.employee_id AS manager_id, m.employee_name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;
"""

# Execute the query
cursor.execute(query)

# Fetch all the records
records = cursor.fetchall()

# Iterate through the records and print them
for record in records:
    print(record)

# Close the cursor and database connection
cursor.close()
connection.close()