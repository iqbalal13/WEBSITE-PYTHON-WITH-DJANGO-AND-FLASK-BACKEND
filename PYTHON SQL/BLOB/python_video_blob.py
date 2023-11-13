import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_user',
            password='your_password'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_blob(connection, file_path):
    try:
        cursor = connection.cursor()

        # Read the binary data from the file
        with open(file_path, 'rb') as file:
            binary_data = file.read()

        # Insert the binary data into the BLOB column
        insert_query = "INSERT INTO your_table (blob_column) VALUES (%s)"
        cursor.execute(insert_query, (binary_data,))
        connection.commit()
        print("BLOB data inserted successfully")

    except Error as e:
        print(f"Error: {e}")

def retrieve_blob(connection, output_file_path):
    try:
        cursor = connection.cursor()

        # Retrieve the BLOB data from the database
        select_query = "SELECT blob_column FROM your_table WHERE your_condition"
        cursor.execute(select_query)
        record = cursor.fetchone()

        if record:
            # Write the binary data to a file
            with open(output_file_path, 'wb') as file:
                file.write(record[0])

            print(f"BLOB data retrieved and saved to {output_file_path}")
        else:
            print("No data found")

    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_host', 'your_database', 'your_user', 'your_password',
    # 'your_table', and 'your_condition' with your actual values
    connection = create_connection()

    # Replace 'path_to_your_file' with the path to the file you want to insert
    insert_blob(connection, 'path_to_your_file')

    # Replace 'output_file_path' with the path where you want to save the retrieved file
    retrieve_blob(connection, 'output_file_path')

    if connection:
        connection.close()