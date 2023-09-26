print("Welcome to my Calculator-inator 9000!")

one = int(input('Enter the first number:'))
two = int(input("Enter the second number:"))

print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Exponent')
print('6.Floor Division')
print('7.Remainder')

opp = input('Enter a choice:')

print('Result:')

if  opp == '1':
    print(one + two)
elif opp == '2':
    print(one - two)
elif opp == '3':
    print(one*two)
elif opp == '4':
    print(one/two)
elif opp == '5':
    print(one**two)
elif opp == '6':
    print(one//two)
elif opp == '7':
    print(one%two)

# I made two variables first for both of the number typed in by the user. Then, I made the list for the operations, after I made another input fot the choice of operation selected. I made if and elif statements for the operations to print out the results.
