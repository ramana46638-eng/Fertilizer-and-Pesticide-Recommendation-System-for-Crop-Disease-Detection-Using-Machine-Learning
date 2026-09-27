import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_farming"
    )

    if connection.is_connected():
        print("MySQL connection successful!")

except mysql.connector.Error as error:
    print("MySQL connection failed!")
    print("Error:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")