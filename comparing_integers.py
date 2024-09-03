#I DONT UNDERSTAND THIS CODE
"""Comparing integers using if statements and comparison operators"""

print('enter two integers, and i will tell you',
      'the relationships they satisfy.')

#read first integer
number1 = int(input('enter the first integer'))

#read second integer
number2 = int(input('enter the second integer'))

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)