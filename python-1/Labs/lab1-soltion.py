# Lab1
# print('welcome to the hunger game')
# print('''how are you U
# no not me you
# im U
# he's me and im u''')
# print('yabadabadoo'*37)

# Lab2

# age √
# @ge X
# 1ge X
# fav color X

# name = 'Jo Biden'
# age = 90.8
# fav_color = 'Blue'
#
# # Lab 3
# print(age)
# print(type(age))
# age = int(age) # 90.8 => 90 Casting
# print(age)
# print(type(age))
#
# new_age = str(age) + ' years old'
# new_age2 = f'{age} years old'
# print(new_age2)
# print(new_age)
#

# Lab4

# a = 99
# b = 41
# print('+',a + b)
# print('-',a - b)
# print('*',a * b)
# print('/',a / b)
# print('//',a // b)
# print('%',a % b)
# print('**',a ** b)

# lab 5
# name = input('enter your name please :')
# age = input('enter your age please :')
#
# print(f'welcome {name} you have {age} years of experience in earth')

# Lab 6

# birth_year = int(input('please enter you birth year'))
# age = 2025 - birth_year
# print(f'your age is  {age}')


# lab 7
# sen = input('please enter a text :')
# print(sen)
# print(len(sen))
# print(sen.upper())
# print(sen.lower())
# print(sen.title())
#

# lab 8
# half_point = len(sen)//2
# print(sen[:half_point])
# print(sen[half_point:])
# print(sen[::-1])
# print(sen[:half_point-1:-1])

# lab 9
# print('welcome to squid game !')
# sen = input('enter a sentence of your choice: ')
# char = input('enter the char of word that you want to find in the sentence: ')
# guess = input('what is the index of the char (you think): ')
#
# print('the real index is :', sen.find(char))
# print(f'your guess is : {guess}')

# etgar 1
#
# name = input('please enter your full name: ')
# shifted_name = name[-1] + name[:-1]
#
# print(shifted_name)

# etgar 2


sentence = input('enter your sentence : ')
jump = int(input('enter your skips: '))

print(sentence[jump::jump])
