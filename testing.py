import mysql.connector

# Establish connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="expensetracker"
    )
    if conn.is_connected():
        print("Successfully connected to the database!")

    # Close the connection
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
