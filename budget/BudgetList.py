from . import Expense
# Create the BudgetList class
"""
In the budget directory, open the BudgetList.py file. Inside that file, create a class
called BudgetList with only pass inside the class for now.
"""
# Create the constructor
"""
Replace pass with a constructor that has two parameters - self and budget. Then initialize the following class variables:

self.budget to the passed-in budget
self.sum_expenses to 0
self.expenses to an empty list
self.sum_overages to 0
self.overages to an empty list
"""

# Define the append method
"""
Define an append method that has two parameters - self and item. Put pass inside the method for now.
"""


class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if self.sum_expenses+item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return len(self.expenses) + len(self.overages)


def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print("The count of all expenses: " + str(len(myBudgetList)))


if __name__ == "__main__":
    main()

# Add items to expenses that are under budget
"""
Replace pass with an if statement that checks if self.sum_expenses plus the passed-in item is less than self.budget. 
Inside the if block, call append() on self.expenses and pass in item. 
Also inside the if block, add item to self.sum_expenses.
"""

# Add items to overages that are over budget
"""
After the if block, add an else block that calls append() on self.overages and passes in item. 
Also, increase self.sum_overages by item.
"""