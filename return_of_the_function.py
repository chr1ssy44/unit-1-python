import math
"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def number(a):
    return math.sqrt(a)
y = number(25)

assert number(25) == 5
# The first assertion is True so nothing happened in the console.
assert number(16) == 4
# The second assertion is also True  because the squareroot of 16 is 4.
print(y)
#I import the math module and I created a function then return my function as math.sqrt(a) to find the square of the variable y which I set as 25.
"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area(c,d):
    return c*d
x = area(15,4)

assert area(15,4) == 60
#The first assertion is True so nothing happened in the console.
try:
 assert area(9,9) == 80
except:
   print("9 times 9 is not equal to 80.")
# For the second assertion i used try/expect to have to have an error but to say it gracefully instead of an AssertionError. So it would print to expect instead of posting an error.
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

assert temp(21) == 32.46666666666667
# The first assertion is True so nothing happened in the console.
assert temp(35) == 32.77777777777778
# The second assertion is True so nothing happened in the console.
print(z)

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""