import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iqbal",
    database="testdatabase"
)

try:
    mycursor = db.cursor()

    # Uncomment the following lines if you haven't already created the table and inserted data
    # mycursor.execute("CREATE TABLE test(name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM ('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL  AUTO_INCREMENT)")
    # mycursor.execute("INSERT INTO test (name, created, gender) VALUES(%s,%s,%s)", ("tom", datetime.now(), "M"))
    # db.commit()

    mycursor.execute("SELECT * FROM test WHERE gender = 'F'")

    for x in mycursor:
        print(x)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    db.close()
