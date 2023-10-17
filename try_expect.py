try:
 age = int(input('Enter your age: '))
except:
 print("Unable to convert into an integer")
# I put the first line of code into  a try and expect statement and if the user types their answer as a string instead of an error the message would be, "Unable to convert into an integer".
faveNum = int(input('What is your favorite number: '))

if age <= 21:
 print('You are not allowed to enter, you are too young.')
else:
 print('Welcome, you are old enough.')
try:
 print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
 print("Unable to divide by zero")
#I put this line of code into  a try and expect statement and if the user puts '0' instead of an error the message would be, "Unable to convert into an integer".

