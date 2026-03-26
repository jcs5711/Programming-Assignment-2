from expense import Expense

def run_tests():
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

if __name__ == "__main__":
    run_tests()