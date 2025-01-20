# is_hot = True
# is_cold = False

# print(3 > 6)
# print(8 >= 9)

# x = 8
# y = 9
# print(x >= y)
#
# x = int(input('enter a number 0-9'))
# y = int(input('enter a number 0-9'))
# print(x >= y)


# password = "P@ssw0rd!"
#
# user_password = input('enter your password')
# print(password == user_password)

# x = 5
# y = 9
# z = 8
#
# print(x > y and x > z) # is x max ?
# print(y > x or y > z) # is y max ?
# print(y < x > z) # x > y and x > z

# a1 = 0 # False
# a2 = 1 # True
# a3 = -77 # True
# b1 = 0.0 # False
# b2 = 66.199 # True
# c1 = '' # False
# c2 = 'False' # True
# print(bool(c1))
# print(bool(c2))


#if statements

# is_gas_level_low = False
#
# if is_gas_level_low:
#     print('fill the car up...')
# else:
#     print('gas is ok ...')
# print('car is on')

# if logical_expression:
#     # True block
# else:
#     # false block


# number1 = int(input('enter a number'))
# number2 = int(input('enter a number'))
#
# if number1 > number2:
#     print(f'{number1} is greater')
# else:
#     print(f'{number2} is greater')
# print('adios')


# salary = int(input('enter your salary : '))
#
# if salary > 25000:
#     tax = 0.4
# elif salary > 10000:
#     tax = 0.2
# else:
#     tax = 0.01
#
# print(salary*(1-tax))

# exercise:
# a hot day is a day with temp greater or equals
# to 30C
# write a python code to get the temp
# from the user and print if the day is hot or cool
# if the user input is greater than 50
# this indicates that the user gave you the temp in F
# please convert the f to c in case of input greater than 50
# °C = (°F - 32) ÷ (1.8)
# if statement:
#     true block
# else:
#     false block

# temp = float(input('enter the temp in your area: '))
#
# if temp > 50:
#     temp = (temp-32) / 1.8
#
# if temp >= 30:
#     print('what a hot day you got')
# else:
#     print('chill man its a good day you havin')



# golden password  len >= 10    len <= 16 and contains 3 'a'

# password = input('enter a password to check if its a golden')
# if 16 >= len(password) >= 10 and password.count('a') == 3:
#     print('golden password')
#


# x = 'hodi'

# count => str
# x.count()

# global
# len('hodi') # => number
# abs(11) -> 11
# abs(-11) -> 11

# print(abs(-999))
# round(6.6)  # => 7
# round(1.2)  # 1
# round(-1.9) # -2

import math
print(math.e)
print(math.pi)
print(math.sqrt(144))
print(144 ** (1/2))
