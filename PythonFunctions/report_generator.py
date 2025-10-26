from Database.database_connection import connectToDatabase
import csv
# Function to generate an expense report by category
def generateExpenseReport():
    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT CategoryName, SUM(Amount)
        FROM Expenses
        JOIN Categories ON Expenses.CategoryID = Categories.CategoryID
        GROUP BY CategoryName
    """)
    report = cursor.fetchall()
    # Write the rows into a CSV file
    with open("expenseReport.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Category Name", "Amount"])
        # Write the data rows
        writer.writerows(report)

    print("Data successfully exported to ExpenseReport.csv")
    cursor.close()
    conn.close()
    return report
