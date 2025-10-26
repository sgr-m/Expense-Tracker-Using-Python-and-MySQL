# ExpenseTracker

A simple Python-based CLI application to track personal expenses, manage categories, set budgets, and generate reports.

## Project Structure

```
ExpenseTracker/
├── database_connection.py # Database connection setup
├── expense_tracker.py # Manages expense-related operations (add, view)
├── category_manager.py # Handles category-related operations (add, view)
├── config.py # Optional configuration data for db connection
├── budget_manager.py # Manages budget operations (set, view)
├── report_generator.py # Generates reports for expenses by category
└── user_interface.py # CLI for interacting with system
```

## Features

- Add and view expenses.
- Manage categories for expenses.
- Set and view budgets.
- Generate expense reports by category.
- Command-line interface for easy interaction.

## Installation

1. Clone the repository:
git clone https://github.com/your-username/ExpenseTracker.git

2.Navigate to the project folder: cd ExpenseTracker

3. Install required packages: pip install -r requirements.txt

## Usage
Run the CLI interface: python user_interface.py

## License
This project is licensed under the MIT License. See the LICENSE file for details.
