from expense import Expense

def load_expenses(filename="expenses.txt"):
    expenses = []
    try:
        with open(filename, 'r') as f: 
            for line in f:
                line = line.strip()
                if line:
                    name , amount = line.strip(',')
                    expenses.append(Expense(name.strip(), float(amount)))
    except FileNotFoundError:
        print("files does not exist.")
    except Exception as e:
        print(f"An error occurred while loading your expenses: {e}")
    return expenses

def save_expenses(expenses, filename="expenses.txt"):
    with open(filename, 'w') as f:
        for e in expenses:
            f.write(f"{e.name},{e.amount}\n")

def view_expenses(expenses):
    print("\nExpenses:")
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e}")

def total_expenses(expenses):
    total = sum(e.amount for e in expenses)
    print(f"\nYour Total Expenses are ${total:.2f}")