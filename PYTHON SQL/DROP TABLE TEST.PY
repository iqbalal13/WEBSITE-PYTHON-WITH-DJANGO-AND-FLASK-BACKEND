import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iqbal",
    database="testdatabase"
)

# Create a cursor
mycursor = db.cursor()

# Define the table name to drop
table_to_drop = "genders"

# SQL query to drop the table
drop_table_query = f"DROP TABLE {table_to_drop}"

# Execute the drop table query
mycursor.execute(drop_table_query)

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()