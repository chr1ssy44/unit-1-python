'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
x = int(input("Enter a number:"))

if x > 10 and x % 2 == 0:
    print("True")
else:
    print("False")
## I created a variable for the input then made a if condition with the 'and' operator for if the input is even and greater than 10. Then it would print if the statement is true or false.
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
price = int(input("Enter your age and student status:"))

if price < 18:
    print("Price is $10!")
else:
    print("Price is $20!")
## I made a variable set as 'price' and made a if condition if the student is less than or older than 18 years old.
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
my_list = ['apple','orange','grapes','watermelon','pinapple','mango']
fruits = input("Enter a random fruit:")

if fruits in my_list:
    print("Yes, that fruit is on the list!")
else:
    print("No, that fruit is not on the list:(")
## I created a list of fruits, then I made a inout with the variable 'fruits'. I made a condition to print if the input  the user put is in the list I created is true or false.
'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
y = int(input("Enter a year:"))


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
z = 5
w = 7

Zone_A = float(input("Enter your shipping info for Zone A:"))
Zone_B = float(input("Enter your shipping info for Zone B:"))
if Zone_A > 1 and Zone_B > 1:
    print(z * 2.2046 * Zone_A)
    print(w * 2.2046 * Zone_B)
else:
    print("Error")


## I made two variables for each zone and  made three other variables for the cost per kilogram and how much a kilo is. Then I printed the result by multiplying the input and the variables.
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''