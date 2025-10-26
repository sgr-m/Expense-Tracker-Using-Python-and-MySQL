from PythonFunctions.expense_tracker import addExpense, viewExpenses
from PythonFunctions.category_manager import addCategory, viewCategories
from PythonFunctions.budget_manager import setBudget, viewBudgets
from PythonFunctions.report_generator import generateExpenseReport

# Main function to interact with the user
def main():
    while True:
        print("Welcome to the Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Category")
        print("4. View Categories")
        print("5. Set Budget")
        print("6. View Budgets")
        print("7. Generate Report")
        print("8. Exit the Program")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter amount: "))
            categoryId = int(input("Enter category ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            addExpense(amount, categoryId, date)
        elif choice == 2:
            expenses = viewExpenses()
            for expense in expenses:
                print(expense)
        elif choice == 3:
            categoryName = input("Enter category name: ")
            addCategory(categoryName)
        elif choice == 4:
            categories = viewCategories()
            for category in categories:
                print(category)
        elif choice == 5:
            userId = int(input("Enter user ID: "))
            categoryId = int(input("Enter category ID: "))
            budgetAmount = float(input("Enter budget amount: "))
            setBudget(userId, categoryId, budgetAmount)
        elif choice == 6:
            userId = int(input("Enter user ID: "))
            budgets = viewBudgets(userId)
            for budget in budgets:
                print(budget)
        elif choice == 7:
            report = generateExpenseReport()
            # for entry in report:
            #     print(entry)
        elif choice == 8:
            print("Exiting the Program\nGood Bye!")
            break
        else:
            print("Invalid Choice Please Try again!!")
# "__main__":
main()
