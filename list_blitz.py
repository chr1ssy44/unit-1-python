"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
my_list = ['Demon Slayer','Erased','Hunter x Hunter','Baki']
print(my_list)
""" I created a variable name called "my_list" then I placed four items in the list. I printed my list.
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
""" 
my_list.append('Lie in April')
print(my_list)
""" I added my new item by using the element "append" then I printed my list.
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
my_list.remove('Hunter x Hunter')
print(my_list)
""" I used the remove element to delete my item 'Hunter x Hunter then printed my list.
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
my_list[3] = 'Soul Eater'
print(my_list)
""" I modified my list by using the index of one of my items to change it to 'pinapples'.
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
my_list.append('AOT')
my_list.append('JOJO')
print(my_list)
""" I used the append element to add two new items to the list.
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del my_list[5]
print(my_list)
""" I used the del element to delete index [5] which is 'JOJO'.
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
list = my_list[0:2]
print(list)
""" I created a new variable named 'list' and made it equal my first to items from my first variable 'my_list'.
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list. I created a new variable 'anime' then I extended my list by putting my first two list together. 
"""
anime = my_list + list
print(anime) 
