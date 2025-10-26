from Database.database_connection import connectToDatabase

# Function to add a new category
def addCategory(categoryName):
    conn = connectToDatabase()
    cursor = conn.cursor()
    query = "INSERT INTO Categories (CategoryName) VALUES (%s)"
    cursor.execute(query, (categoryName,))
    conn.commit()
    print(f"Category {categoryName} added successfully!")
    cursor.close()
    conn.close()

# Function to view all categories
def viewCategories():
    conn = connectToDatabase()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Categories")
    categories = cursor.fetchall()
    print("Following are the Categories: -------")
    cursor.close()
    conn.close()
    return categories
