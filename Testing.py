from expense import Expense   # imports the Expense class from the expense file

def run_tests():        # function to run tests on the Expense class and the functions in the expense_utils file
    e = Expense("Shopping", 50) 
    assert e.name == "Shopping"
    assert e.amount == 50

    try:
        Expense("", 10)
        assert False
    except ValueError:
        pass

    try:
        Expense("Shopping@#", 10)
        assert False
    except ValueError:
        pass

    try:
        Expense("Coffee", -5)
        assert False
    except ValueError:
        pass 

    expenses = [Expense("Rent", 1000), Expense("Food", 200)]

    print("Tests passed!")

if __name__ == "__main__":   # runs the run_tests function when the program is executed
    run_tests()