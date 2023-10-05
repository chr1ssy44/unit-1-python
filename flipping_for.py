"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
a = "hello "
for x in a:
    print(x)
"""I created a variable x which equals to the string hello. Then, I used a for loop to print each letter of the word hello.
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
add = [1,3,5,7]
sum = 0
for num in add:
    sum += num
    print("The sum of this list is: ", sum)
""" I created 2 variables one for my list and one for the starting number. Then, used a for loop to add the elements together.
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
y = ["My name is Christina"]
for x in y:
    print(len(x))
"""I created a variable y equal to a sentence. Then used a for loop and the "len" elemnet to print the length of each word.
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
my_list = dict(color = "Pink", car = "Honda", sky = "Blue", food = "Pizza")
for x in my_list:
    print(x)