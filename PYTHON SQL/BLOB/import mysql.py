import mysql.connector

# Define the database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "iqbal",
    "database": "mydatabase",
}

try:
    # Create a connection to the MySQL database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Create a table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    connection.commit()

    # Retrieve data from the table
    select_query = "SELECT * FROM users"
    cursor.execute(select_query)
    users = cursor.fetchall()
    for user in users:
        print(user)

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()