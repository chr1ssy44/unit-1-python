import math
"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def number(a):
    return math.sqrt(a)
y = number(25)

print(y)
#I import the math module and I created a function then return my function as math.sqrt(a) to find the square of the variable y which I set as 25.
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area(c,d):
    return c*d
x = area(15,4)

print(x)
#I created a function and put two variable in the parameter then return it as c * d to find the area of the variable x which is 15 and 4.
"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def temp(e):
    return e/9/5+32
z = temp(21)

print(z)

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""