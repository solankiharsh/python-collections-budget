# Import Matplotlib
# Now we want to show a bar graph comparing the expenses, overages, and budget totals.
# First, we need to add import matplotlib.pyplot as plt to the top of the file after from . import Expense.

from . import Expense
import matplotlib.pyplot as plt


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

    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self

    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()




# Create the __iter__() method
"""
Next, we want to create an iterator for BudgetList by implementing __iter__() and __next__() to iterate the 
expenses list first and then continue iterating the overages list. Once those are implemented and 
you can get an iterator from BudgetList, it will be an iterable that will allow 
you to seamlessly iterate over the expenses and overages lists.

To start, inside the BudgetList class, at the bottom, define an __iter__ 
method that has self as a parameter. Put pass inside the body of the method for now.
"""

# Finish __iter__()
"""
We are going to take advantage of the built in iterator for the expenses and 
overages list types and will use their built-in iterators to make a new custom iterator.

Inside __iter__(), remove pass and replace it with a new iter object with iter() and 
pass self.expenses into the constructor. On the next line, set self.iter_o to another iter() 
object with self.overages in the constructor. Finally to finish the method, return self.
"""

# Create next()
"""
After the __iter__() method, define the method __next__() with self as a parameter. 
Put pass inside the body of the method for now.
"""

# Finish __next__()
"""
Inside __next__(), remove pass and replace it with a try: block. 
Inside the try: block, return a call to __next__() on self.iter_e.

On the next line add an except block, with StopIteration as stop as the exception. 
Inside the except block, return a call to __next__() on self.iter_o.
"""


def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print("The count of all expenses: " + str(len(myBudgetList)))
    for entry in myBudgetList:
        print(entry)
    fig, ax = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green','red','blue'])
    ax.set_title('Your total expenses vs. total budget')
    plt.show()


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

# Test the iterable
"""
We can now test that BudgetList works as an iterable by using it in a for loop. 
In main(), after the print() statement, create a for loop that has an iterator called entry and 
loops through myBudgetList. 
Inside the for loop, call print() with entry as an argument.
If we run python -m budget.BudgetList, the output should be 
"The count of all expenses: 37" followed by each of the 37 amounts.
"""

# Create the figure and axes
"""
Then at the end of main(), call fig, ax = plt.subplots() to initialize fig as the Figure, or top level container 
for our graph. And ax as the Axes, which contains the actual figure elements.
"""

# Create the list of labels
"""
Create a variable called labels and set it equal to a list with the following values: 'Expenses', 'Overages', 'Budget'.
"""

# Create the list of values
"""
Create a variable called values and set it equal to a list with the following properties from myBudgetList: 
sum_expenses, sum_overages, and budget.
"""

# Create the bar graph
"""
Next, call ax.bar() with the labels and values lists as parameters, and color=['green','red','blue'] as a parameter.
"""

# Set the title
"""
To add a title, call ax.set_title() and pass in the string 'Your total expenses vs. total budget'.
"""

#Show the figure
'''
Finally, to display the graph, call plt.show().
To see the results yourself, you can run python -m budget.BudgetList from the top-level directory. 
You should see the bar chart pop up in another window automatically.
'''

