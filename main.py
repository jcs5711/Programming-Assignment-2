file = "expenses.txt"

def welcome():
    print("Welcome to your Expense Tracker!")
    print("---------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
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

def save_expenses(expenses):
    with open(file,'w') as f:
        for e in expenses:
            f.write(f"{e['name']},{e['amount']}\n")

def add_expense(expenses):
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expenses.append((name, amount))
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid Input. Enter a valid amount.")
    
    except Exception as e:
        print(f"An error has occurred: {e}")

def view_expenses(expenses):
    print("\nExpenses:")
    i = 1
    for e in expenses:
        print(f"{i}. {e['name']}: ${e['amount']}")
        print()

def total_expenses(expenses):
    total = 0 
    for e in expenses: 
        total += e["amount"]

    print(f"Your Total Expenses are ${total}")


