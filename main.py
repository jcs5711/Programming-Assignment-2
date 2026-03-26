file = "expenses.txt"

def welcome():
    print("Welcome to your Expense Tracker!")
    print("--------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print(3. Total Expenses)
    print("4. Remove Expense")
    print("5. Exit")

def load_expenses():
    expenses = []
    try:
        with open(file, 'r') as f:
            for line in f:
                name, amount = line.strip().split(',')
                expenses.append((name, amount))
    except FileNotFoundError:
        print("File doesnt exist.")
    except Exception as e:
        print(e)
    return expenses

def add_expense():
    try:
        name = input("Enter expense name: ")