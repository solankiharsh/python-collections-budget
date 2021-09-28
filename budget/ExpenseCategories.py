from . import Expense
import matplotlib.pyplot as plt
import timeit

# Import timeit
"""
We want to use the Python timeit module to time whether categorizing expenses was faster using a for loop or 
set comprehension. 
First, we need to import timeit at the top of the ExpenseCategories.py file.
"""

# Call timeit.timeit()
"""
After the for loop for the subset test, call timeit.timeit() with the following 4 arguments:
stmt = "pass"

This will eventually be the line of code we want to time the execution of.
setup = 

'''
'''
This multi-line string will eventually hold the lines of code that are required for stmt to run.
number=100000

This is the number of executions to time.
globals=globals()

This specifies the namespace to execute the code.
"""

# Pass the code to timeit.timeit()
"""
Now that we know how to use timeit.timeit(), let’s pass in the actual code we want to time. Replace stmt = "pass" with stmt = "expenses.categorize_for_loop()". Also set setup equal to the following multi-line string:

'''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
'''
"""

# Print the timeit result
"""
Wrap the entire timeit.timeit() call from the previous task in a print() statement. 
Then it will print out the total number of seconds to execute the statement the specified number of times.

If you test this by running python -m budget.ExpenseCategories you should see around ~1.5 seconds printed out.
"""

# Duplicate the timeit.timeit() call for set comprehension
"""
Now that we’ve set up the timer for expenses.categorize_for_loop(), let’s set up the timer to time 
expenses.categorize_set_comprehension(). Copy and paste the entire print(timeit.timeit(...)) 
code from the previous tasks. Then replace stmt = "expenses.categorize_for_loop()" 
with stmt = "expenses.categorize_set_comprehension()".

If you test this by running python -m budget.ExpenseCategories you should see 
around ~1.6 seconds printed out for the set comprehension method.

Set comprehension may be faster than a for loop in general for a single loop. 
However, we had 2 set comprehensions that each required looping to check separate 
conditionals whereas the for loop method only used one iteration to check the conditionals.
"""

# Create the figure and axes
"""
Now that we’ve determined which categorization method was faster, 
we want to create a pie chart comparing the expense totals for each category.

After the timeit() code, call fig,ax=plt.subplots() to initialize fig as the Figure and ax as the Axes.
"""

# Create the list of labels
"""
Create a variable called labels and set it equal to a list with the following values: 'Necessary', 'Food', 'Unnecessary'
"""

# Create the list of sums
"""
Inside the divided_set_comp list we have three sets of expenses divided by category. 
Now we want to create a list that has a sum for each of those expense amounts. 
Create a variable called divided_expenses_sum and set it equal to an empty list.
"""

# Sum the amounts in each set
"""
Create a for loop that has an iterator called category_exps and loops through divided_set_comp. 
Inside the for loop, we want to sum the expense amounts for each set using a list comprehension 
and append that sum to the divided_expenses_sum list. Inside the for loop, call divided_expenses_sum.append(). 
Then inside the append(), call sum(). Inside sum(), we want the list comprehension 
that returns x.amount for x in category_exps.
"""

# Create the pie chart
"""
Next, call ax.pie() with the following arguments:
divided_expenses_sum
labels = labels
autopct = '%1.1f%%'
(This will format the percentage.)
"""

# Show the figure
"""
Finally, to display the graph, call plt.show().

To see the results yourself, you can run python -m budget.ExpenseCategories from the top-level directory. 
You should see the pie graph pop up in another window automatically.
"""


from . import Expense
import timeit
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


    print(timeit.timeit(stmt = "expenses.categorize_for_loop()",
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''',
                        number=100000,
                        globals=globals()))

    print(timeit.timeit(stmt = "expenses.categorize_set_comprehension()",
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''',
                        number=100000,
                        globals=globals()))

    fig, ax = plt.subplots()
    labels = ['Necessary', 'Food', 'Unnecessary']

    divided_expenses_sum = []
    for category_exps in divided_set_comp:
        divided_expenses_sum.append( sum(x.amount for x in category_exps) )

    ax.pie(divided_expenses_sum, labels=labels, autopct='%1.1f%%') #, shadow=True, startangle=90)

    plt.show()


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