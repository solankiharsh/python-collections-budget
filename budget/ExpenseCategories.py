from . import Expense
import matplotlib.pyplot as plt


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if not divided_set_comp == divided_for_loop:
        print("Sets are NOT equal by == test")

    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and 
            b.issubset(a)):
            print("Sets are NOT equal by subset test")


if __name__ == "__main__":
    main()

# Create a method to categorize expenses
"""
We want to create a pie chart that compares different spending categories. 
But first, we need to categorize our spending data. 
We went ahead and wrote a method to do this using a for loop in the 
Expense class called categorize_for_loop(). But now we’re wondering if this would be faster using set comprehension. 
Let’s write a method called categorize_set_comprehension() to test this. 
Then we can use the timeit module to test which one is faster.

In Expense.py, inside the Expenses class, after categorize_for_loop(), 
create a method called categorize_set_comprehension() that has self as a 
parameter and put pass inside the method of the body for now.
"""

# Categorize necessary expenses
"""
Inside categorize_set_comprehension(), create a variable called necessary_expenses set equal to 
empty curly braces, which is where we’ll create the set comprehension. 
Inside the curly braces, we want x for x in self.list then on the next line we want a conditional that checks 
if: x.category is equal to 'Phone' or x.category is equal to 'Auto and Gas' or x.category is equal to 
'Classes' or x.category is equal to 'Utilities' or x.category is equal to 'Mortgage'.
"""

# Categorize food expenses
"""
On the next line, create a variable called food_expenses set equal to a similar set comprehension that 
checks if each category is equal to 'Groceries' or 'Eating Out'.
"""

# Categorize unnecessary expenses
"""
Then, to categorize the remaining expenses, create a variable called unnecessary_expenses. 
Set it equal to calling set() with self.list as a parameter. Then use set subtraction to subtract necessary_expenses and 
food_expenses from that set. This should all be on one line of code.
"""

# Return Categories
"""
Finally, to return the sets together, return a list with the following variables inside: necessary_expenses, 
food_expenses, unnecessary_expenses.
"""

# Use categorize_set_comprehension
"""
In ExpenseCategories.py, we went ahead and called expenses.categorize_for_loop(). 
Now we want to call categorize_set_comprehension() and see if we get the same results.

Create a variable named divided_set_comp and set it equal to expenses.categorize_set_comprehension().
"""

# Check that the categorized sets are equal
"""
Add an if statement that checks if divided_set_comp and divided_for_loop are not equal. 
If they are not equal, print the following: 'Sets are NOT equal by == test'.

If we run this, we should see nothing printed to the screen since all of the sets within the list should be equal.
"""

# Create for loop for subset test
"""
We can also perform mathematical set operations in Python. For instance, another way of showing that two sets are 
equal is to check if both sets are subsets of each other.

To demonstrate this, let’s create a for loop to look at each set in divided_set_comp and divided_for_loop. 
We can use zip() to return a list of tuples for a for loop like so: for a,b in zip(divided_for_loop, divided_set_comp). 
Put pass inside the for loop for now.
"""

# Check that the categorized sets are equal by subset test
"""
Inside the for loop replace pass with a conditional that checks if a is a subset of b and b is a subset of a 
using the issubset() method. Add a not operator in front of the conditional, 
since we only want to print something if the equality test fails. 
Make sure you have parenthesis around the whole expression, otherwise it will only test not on the first part. 
Inside the if statement, print the following: "Sets are NOT equal by subset test".
"""