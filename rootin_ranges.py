"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for x in range(1,11):
    print(x)
""" I made the range from 1-11 so the loop will start at 1 and end at 10.
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for x in range(900,1001,10):
    print(x)
"""I made the range start at 900 and end at 1001 and the last number states what I want to number to be counted by so I put the number 10.
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for x in range(1,108,9):
    print(x)
""" I made the range start a 1 and end at 108 and made it count by 9.
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
dum = range(1,11)
sum = 0
for num in dum:
    sum += num
    print(sum)
""" I set range with the variable "dum" and made another variable sum equal to 0. Then I used a for loop to add sum and num to add all the numbers from 1 to 10.
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
The output is the * counted by 1 row by row.
- Explain the iterative process that this code executes to get that output
"""
#The variable row is set to the number 5.Then used a for loop for i in range of the variable rows which is equaled to 5. 
#So I think since in the second line of code the range add 1 to i, so it now it becomes 6 so the range is 1,6.
#Since the print says to print the '*' but end = '' meaning to put spaces in between the *.
#The second print is empty so the range numbers don't show at the end of each *.
rows = 5 
 
for i in range(rows): 
     for j in range(i + 1):
         print('*', end=' ')
     print()