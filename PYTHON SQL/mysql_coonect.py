import mysql.connector

# Define connection parameters
host = "your_host"
user = "your_username"
password = "your_password"
database = "your_database"

# Establish a connection
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to MySQL database")
except Exception as e:
    print(f"Error: {e}")

# Close the connection when done
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")