from Database.database_connection import connectToDatabase

# Function to set a budget for a category
def setBudget(userId, categoryId, budgetAmount):
    conn = connectToDatabase()
    cursor = conn.cursor()
    query = "INSERT INTO Budgets (UserID, CategoryID, BudgetAmount) VALUES (%s, %s, %s)"
    cursor.execute(query, (userId, categoryId, budgetAmount))
    conn.commit()
    print("Budget Set Successfully!")
    cursor.close()
    conn.close()

# Function to view all budgets for a user
def viewBudgets(userId):
    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Budgets WHERE UserID = %s", (userId,))
    budgets = cursor.fetchall()
    cursor.close()
    conn.close()
    print("Following are the budgets: --------")
    return budgets
