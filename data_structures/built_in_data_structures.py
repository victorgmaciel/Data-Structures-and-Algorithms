
"""A list is one of the most commonly used data structures in Python. """

# Lists are used to store item(s) in a single variable 
my_list = ["Bar","Food", "USA"]
#we can see this list by using pythons print function
#print(my_list)

"""One really neat thing about lists, is thatthey can store different data types!"""

another_list = ["Cat", 678, 45.09342, my_list, "name of the game"]

#lets print this list and see the results 
#print(another_list)

#no worries if you don't have your terminal up, this is the print out
"""['Cat', 678, 45.09342, ['Bar', 'Food', 'USA'], 'name of the game']"""

"""Now lets get some important information out there about lists in Python. <br/>
- They are ordered, meaning items in the list have a defined order and that order will NOT change. If you add an item to the list, the item is placed at the end. <br/>
- Lists have the ability to change! So we can add and remove items after the list has been created. 
- Lists can have duplicate values
- As said before, they can be of any data type. 

Its because of these features that a list is mutable and dynamic! 

Lets look back at the first list and see this in action. 
"""

print(my_list[2])

#USA prints out because it is the item at the 2nd index of the ordered list. 
#   0       1       2
["Bar","Food", "USA"]

# Remember, that there are three items and there are three indices. It starts at 0. 

# lets change the item at index[2] to a integer. 

my_list[2] = 1776
print(my_list[2])

# now lets look at that list with its new item. 
print(my_list)

