'''
TASK 1 Even or Odd
Determine if a number is even or odd.
# First I made a variable called (number) then made the input a interger. I put if the the number is divided by 2 and the remainder 
equals 0 the number is even otherwise the number is odd.
'''
number = int(input('Enter any number:'))
if number % 2 & number == 0:
    print('This number is even!')
else:
    print('This number is odd!')

'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.
# I made a variable called (do) then I made the input a interger. I made a if, elif, and else statement to determine if the numbers are positive, 
negative, or zero. I made the first if to be greater than zero, the elif statement to equal zero then the else for anything other than 
the first two statements.
EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
do = int(input('Enter a number:'))
if do > 0:
    print("This number is positive!")
elif do == 0:
    print('This number is zero!')
else:
    print('This number is negative!')
'''
TASK 3: Largest of Three
# In created three varaible with random numbers, than I found the max number out of the three nunbers.
Find and print the largest of three numbers.
'''
x = 10
y = 200
z = 5
print(max(x,y,z))
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
# I made leap_year false because its not a leap year. Then I made a if statement to print if its true or not.
''' 
leap_year = False
if leap_year:
    print("Its a LEAP year!")
else:
    print("Its not a LEAP year.")
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''