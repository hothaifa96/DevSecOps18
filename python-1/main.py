# print("hello world !")
# print("hello\nworld !")
# print("my name is\thodi")
# print('10')
# print('''hello and welcome to DevSecOps cource
# today we are working and learning
# python''')
#

# print("*"*10) # **********
# print("10-6*4")
# print('10-6=',10-6)

# arithmetic symbols
# + sum
# print(10+5)
# # - sub
# print(10-5)
# # * multi
# print(10*4)
# # / div
# print(10/3)
# # // clean div
# print(10//3)
# # % module
# print(10%3)

# print(8//3)
# print(8 % 3)
# print(8 - (8//3)*3)

# age = 55
# print(age) # 55
# name = 'Donald Trump'
# age = 66
# print(age) # 66
# print(name)

# DATA TYPES
# numeric
# int -> 1 11 -199 +66 1989
# float -> 1.1 1.0 -0.95 1/2
# complex number -> a+bi

# str
# '' "112"  '''hodi''' 'yaouza'

# bool
# True False

# # numbers
# x = 10
# y = 5
# # print(x+y)
# # print(x*y)
# # print(x//y) # => int
# # print(x/y) # => float
# # print(type(x)) # int
# # print(type(y)) #int
#
# # print('x+y')
# # z = x+y+12+51-52/22
# # print(z)
# # print(type(z))
#
# ##
# # int + int =int
# # int - int =int
# # int * int =int
# # int // int =int
# # int / int =float
#
# # float + int =float
# # int - float =float
# # int * float =float
# # float // int =float
# # int / float =float
#
# # - *,/ - = +
# # + *,/ - = -
# # - *,/ + = -
# # + *,/ + = +
#
# print(y)
# y = y+y
# print(y)
# y = y +6
# y += 6 # => y = y +6

# my_age = 4
# my_age //= 2
# print(my_age)

# name = input('please enter you name: ')
# age = input('enter you age : ')
# print('hello ', name)
# print('and you are', age, 'years old')
# # print('hello ', name, '\nand you are', age, 'years old')
#
# print(type(name))
# add new variable named age and ask the user
# to insert his age and print


# input
# print("welcome to age calculator")
# x = int(input('what is your birth year: '))
#
# # print('your age is : ', 2025-x)
# print(f'your age is : {2025 - x} years old')

# # write a python snippet to get the user salary
# # and calculate his taxes
# # tax rate = 18%
# # and take off 13% fee
# # print the salary before and after the taxes
# name = input('please enter your name: ')
# salary = int(input(f'enter your salary {name} [number only] : '))
#
# taxes = salary * 0.18
# fee = (salary - taxes) * 0.13
# print(f'your received:{salary} salary after taxes:{salary-taxes-fee} ')
#
# # challenge: if the user salary goes for his 3
# # divorces equally how much would they have
# # after the payments
# print((salary-taxes-fee) % 3)


# string

# sen = 'cats AND dogs cant play along'
# # sen_len = len(sen)
# # print('*'*sen_len)
# # print(len(sen)) # len of the str
# # print(sen.upper()) # CATS AND DOGS CANT PLAY ALONG
# # print(sen.lower()) # cats and dogs cant play along
# # print(sen.title()) # Cats And Dogs Cant Play Along
# # print(sen.count('a'))
# # print(sen.lower().count('a'))
# # print(sen.find('a'))
# # print(sen[:len(sen)//2]) # first half of the sen
# # print(sen[len(sen)//2:])
# # print(sen[-5:2]) # ''
# print(sen[4::-1])
# print(sen[::-1])


email = input('enter your email :')
print(email[email.find('@')+1:])