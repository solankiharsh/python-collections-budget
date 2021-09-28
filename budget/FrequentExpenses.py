# Import the Expense Module

"""
Last month’s spending data is in  data/spending_data.csv, which is a spreadsheet with 4 columns:
Date & Time, Location, Category, and Amount. For example, the first row contains: 12/31/2019 12:00:00,Alaska Air,Travel,-$115.75.
We want to analyze our spending habits in a few different ways.
In this module, we are going to read in this file and display the categories with the most purchases in a graph.

To read in the data, we’ll use the classes in the file named Expense.py.
There are 2 classes -- Expense (which has a vendor, category, and amount) and Expenses
(which has a list of type Expense and a sum of the amounts).
Expenses also has a method read_expenses() which we’ll use to read the .csv file.

To start, open the file named FrequentExpenses.py in the budget directory, and add from .
import Expense to the top of the file.
"""
from . import Expense
import collections
import matplotlib.pyplot as plt


# Read in the Spending Data

"""
Create a variable named expenses and set it equal to calling the Expense.Expenses() constructor. 
Then call the read_expenses() method on expenses and pass in the name of the file data/spending_data.csv.
"""
expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")
print(expenses)

# Create a List of the Spending Categories

"""
Create an empty list called spending_categories. Then, create a for loop with an iterator called expense that loops 
through expenses.list. Inside the loop, we want to append() expense.category to spending_categories.
"""
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
    print(f"Spending categories are as under: \n {spending_categories}")

# Count Categories with a Counter Collection
"""
We want to use the Counter Collection in order to count which categories had the most purchases. 
To start, import collections at the top of the file. 
Then after the for loop, create a new variable called spending_counter, set it to an instance of collections.Counter(), 
and pass spending_categories into the constructor.

Note: If you printed the Counter with print(spending_counter), and run python -m budget.FrequentExpenses, 
you would see the following output: Counter({'Eating Out': 8, 'Subscriptions': 6, 
'Groceries': 5, 'Auto and Gas': 5, 'Charity': 2, 'Gear and Clothing': 2, 'Phone': 2, 
'Travel': 1, 'Classes': 1, 'Freelance': 1, 'Stuff': 1, 'Mortgage': 1, 'Paycheck': 1, 'Home Improvements': 1, 
'Parking': 1, 'Utilities': 1})

You can see it shows the category as the key and the number of times it was used as the value. 'Eating Out' is the most common expense which was done 8 times.
"""
spending_counter = collections.Counter(spending_categories)
print(f"Spending Counter: \n {spending_counter}")

# Get the Top 5 Categories
"""
We can get the top 5 most common categories by calling the most_common() method on spending_counter and 
passing in the value 5. Set the result equal to a variable called top5.
"""
top_5_expenses = spending_counter.most_common(5)
print(f"Top 5 expense categories: \n {top_5_expenses}")

# Convert the Dictionary to 2 Lists
"""
If you’ve used the zip() function before it combines 2 iterables. (For example, zip(list1, list2) 
would combine two lists into a list of tuples). 
We can also use zip(*dictionary_variable) to separate the keys and values of a dictionary into separate lists. 
Since we want to have 2 separate lists for the categories and their counts for the bar graph, 
let’s call zip(*top5) and set the result equal to two variables - categories, count.
"""
categories, count = zip(*top_5_expenses)
print(f"Expense Categories: \n {categories}")
print(f"Expense Counts: \n {count}")

# Plot the Top 5 Most Common Categories
"""
Add import matplotlib.pyplot as plt to the top of the file. Then at the end of the file, call fig, ax = plt.subplots() 
to initialize fig as the Figure, or top level container for our graph. And ax as the Axes, 
which contains the actual figure elements.
"""
fig, ax = plt.subplots()

# Create the bar chart
"""
Next, call ax.bar() with the categories and count lists as the arguments. 
On the next line, add a title by calling ax.set_title() and pass in the string '# of Purchases by Category'.
"""
ax.bar(categories, count)
ax.set_title("# of Purchases by Category")

# Display the graph
"""
Finally, to display the graph, call plt.show(). To see the results yourself, you can run python -m budget.FrequentExpenses 
from the top-level directory. You should see the bar chart pop up in another window automatically.
"""
plt.show()