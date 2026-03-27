import re   #imports the regular expression module

class Expense:     #class to represent an expense with a name and an amount, and includes validation for the name and amount
    def __init__(self, name: str, amount: float):
        if not name or not re.match(r'^[A-Za-z0-9\s\-.,!]+$', name.strip()):
            raise ValueError("Invalid expense name. Please stick to letters, numbers, spaces, and basic punctuation.")
        
        if amount <= 0:
            raise ValueError("Amount has to be greater than zero.")
        
        self.name = name.strip()
        self._amount = round(float(amount), 2)
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("Amount has to be greater than zero.")
        self._amount = round(float(value),2)
    def __str__(self):
        return f"{self.name} = ${self.amount:.2f}"
