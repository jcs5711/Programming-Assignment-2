file = "expenses.txt"  # file where expenses will be stored

from expense import Expense #imports the Expense class from the expense file
from expense_utils import load_expenses, save_expenses, view_expenses, total_expenses #imports the functions from the expense_utils file

def welcome():   #displays the welcome message and the menu options to the user
    print("Welcome to your Expense Tracker!")
    print("---------------------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Remove Expense")
    print("5. Exit")
    print("---------------------------------")

def add_expense(expenses):     # function to add an expense to the expense list and save to the file
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expense = Expense(name, amount)
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Invalid Input. Enter a valid amount. {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")

def remove_expense(expenses):      #function to remove an expense from the expense list and save the updated list to the file
    if not expenses:
        print("\n There are no expenses to remove.")
        return
    view_expenses(expenses)
    try:
        number = int(input("Enter the number of the expense to remove: "))
        if number >= 1 and number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print(f"Removed expense: {removed}")
        else: 
            print("Invalid number.")
    except ValueError as e:
        print(f"Enter a valid number. \n")

def main():   # the main function that runs the program and handles the user input and calls the right function based on what they chose
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

if __name__ == "__main__":   #runs the main function when the program is executed
    main()