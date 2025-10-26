from Database.database_connection import connectToDatabase

# Function to add a new expense
def addExpense(amount, categoryId, date):
    conn = connectToDatabase()
    cursor = conn.cursor()
    query = "INSERT INTO Expenses (Amount, CategoryID, Date) VALUES (%s, %s, %s)"
    cursor.execute(query, (amount, categoryId, date))
    conn.commit()
    print("Expenses added Successfully!")
    cursor.close()
    conn.close()

# Function to view all expenses
def viewExpenses():
    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Expenses")
    expenses = cursor.fetchall()
    cursor.close()
    conn.close()
    print("Expenses:----------")
    return expenses
