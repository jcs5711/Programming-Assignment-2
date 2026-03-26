file = "expenses.txt"

from expense import Expense

def welcome():
    print("Welcome to your Expense Tracker!")
    print("---------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Remove Expense")
    print("5. Exit")
    print("---------------------------------")

def load_expenses():
    expenses = []
    try:
        with open(file, 'r') as f:
            for line in f:
                name, amount = line.strip().split(',')
                expenses.append({"name": name, "amount": float(amount)})
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
        expenses.append({"name": name, "amount": amount})
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
        print(f"{i}. {e['name']} = ${e['amount']}")
        i += 1
    print()

def total_expenses(expenses):
    total = 0 
    for e in expenses: 
        total += e["amount"]

    print(f"Your Total Expenses are ${total}")

def remove_expense(expenses):
    if not expenses:
        print("\n There are no expenses to remove.")
        return
    
    view_expenses(expenses)
    try:
        number = int(input("Enter the number of the expense to remove: "))
        if number >= 1 and number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"Removed expense: {removed['name']} - {removed['amount']}")
        else: 
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number. \n")

def main():
    welcome()
    expenses = load_expenses()
    while True:
        choice = input("Enter you choice: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            remove_expense(expenses)     
        elif choice == '5':
            print("Thank you for using the Expense Tracker!") 
            break
        else:
            print("Invalid Input")  


main()
    
