--creating database
CREATE DATABASE IF NOT EXISTS expensetracker;
-- Use the database
USE expensetracker;
--creating table : categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(255) NOT NULL
);
--creating table : expenses
CREATE TABLE Expenses (
    ExpenseID INT AUTO_INCREMENT PRIMARY KEY,
    Amount DECIMAL(10, 2) NOT NULL,
    CategoryID INT,
    Date DATE,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
--creating table : budgets
CREATE TABLE Budgets (
    UserID INT,
    CategoryID INT,
    BudgetAmount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (UserID, CategoryID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
INSERT INTO Categories (CategoryID, CategoryName) VALUES
(1, 'Food'),
(2, 'Transportation'),
(3, 'Utilities'),
(4, 'Entertainment'),
(5, 'Health'),
(6, 'Education'),
(7, 'Shopping'),
(8, 'Travel'),
(9, 'Rent'),
(10, 'Savings'),
(11, 'Insurance'),
(12, 'Gifts'),
(13, 'Dining Out'),
(14, 'Gym Membership'),
(15, 'Internet'),
(16, 'Mobile Recharge'),
(17, 'Fuel'),
(18, 'Miscellaneous'),
(19, 'Home Maintenance'),
(20, 'Subscriptions');
INSERT INTO Expenses (ExpenseID, Amount, CategoryID, Date) VALUES
(1, 200.50, 1, '2025-01-01'),
(2, 50.00, 2, '2025-01-02'),
(3, 300.75, 3, '2025-01-03'),
(4, 150.00, 4, '2025-01-04'),
(5, 500.00, 5, '2025-01-05'),
(6, 600.00, 6, '2025-01-06'),
(7, 250.00, 7, '2025-01-07'),
(8, 800.00, 8, '2025-01-08'),
(9, 1200.00, 9, '2025-01-09'),
(10, 100.00, 10, '2025-01-10'),
(11, 400.00, 11, '2025-01-11'),
(12, 75.00, 12, '2025-01-12'),
(13, 300.00, 13, '2025-01-13'),
(14, 200.00, 14, '2025-01-14'),
(15, 500.00, 15, '2025-01-15'),
(16, 150.00, 16, '2025-01-16'),
(17, 250.00, 17, '2025-01-17'),
(18, 90.00, 18, '2025-01-18'),
(19, 350.00, 19, '2025-01-19'),
(20, 50.00, 20, '2025-01-20');
INSERT INTO Budgets (UserID, CategoryID, BudgetAmount) VALUES
(1, 1, 1000.00),
(1, 2, 500.00),
(1, 3, 1500.00),
(1, 4, 800.00),
(1, 5, 2000.00),
(1, 6, 1200.00),
(1, 7, 1000.00),
(1, 8, 3000.00),
(1, 9, 10000.00),
(1, 10, 2000.00),
(1, 11, 1200.00),
(1, 12, 500.00),
(1, 13, 800.00),
(1, 14, 600.00),
(1, 15, 1000.00),
(1, 16, 400.00),
(1, 17, 1500.00),
(1, 18, 300.00),
(1, 19, 700.00),
(1, 20, 100.00);
