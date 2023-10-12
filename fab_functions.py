# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
def my_function(name):
    print("Greetings " + name)
my_function("Christina")
#I made my function and put 'name' in the parameter and I printed "Greeting" plus the parameter(name). Then I called my function and print my name in the parantheses so the output would be "Greetings Christina".

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
def sum_numbers(a,b):
    print(a + b)
sum_numbers(7,6)
#I made my function sum_numbers then the parameter a,b, Then I printed a plus b and called the function and put the number 7 and 6 to print the sum of those two numbers.

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.
import math
def factorial(n):
    print(math.factorial(n))
factorial(6)
# I imported math then made my function and printed math.factorial with the paramenter 'n'. I called the fuction and put 6 in the parameter.

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
def is_even(num):
    print(num%2 & num==0)
    return True
is_even(10)


# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
