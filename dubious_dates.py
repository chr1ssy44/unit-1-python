import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
x = datetime.datetime.now()
print(x)
#First I imported datetime then, I created a variable to print the date and time right now.
"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
x = datetime.datetime.now()
print(x.strftime("%m/%d/%Y %X"))
#I created the same variable and print x.strftime then I converted it to the format of MM/DD/YYYY and also show the time.
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
x = datetime.datetime.now()
y = int(input("When is your birthdate? "))
age = print("Your age is", x.year-y)
#I created x as the variable for datetime.datetime.now(), I made a input and coverted it into an interger. Then I set another variable age to print the year and subtract it by the user year of birthyear. Then it will print there current age.