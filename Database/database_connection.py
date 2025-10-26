
import mysql.connector

# Function to establish connection to the database
def connectToDatabase():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="expensetracker"
    )

