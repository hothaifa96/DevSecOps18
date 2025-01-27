# # print hello 5 times
#
# # c = 0
# # while c < 5:
# #     print('hello',c)
# #     c += 1
#
# # range in  python
# # range(10) -> 0,1,2,3,4,5,6,7,8,9
# # range(5,10) -> 5,6,7,8,9
# # range(0,10,2) -> 0,2,4,6,8
# # print(list(range(10)))
# # print(list(range(5,10)))
# # print(list(range(0,10,2)))
# # print(list(range(0,-10,-1)))
#
# # [0,1,2,3,4]
# #        ^
# #        n
# # for n in range(5):
# #     print('hello',n)
#
# # print all the odd numbers between 0-100
# # while -
# # x=0
# # while x < 100:
# #     if x % 2 == 1:
# #         print(x)
# #     x += 1
# # # for -
# # for y in range(100):
# #     if y%2 ==1:
# #         print(y)
# # python for way -
# # for z in range(1, 100, 2):
# #     print(z)
#
# # for x in range(0,1000,7):
# #     print(x)
#
# # ask the user to enter a number of rows for the triangle
# # s =4
# # *
# # **
# # ***
# # ****
#
# # for r in range(4):
# #     for c in range(4):
# #         if c <=r:
# #             print('*',end='')
# #     print()
#
# # for i in range(1,5):
# #     print('*'*i)
#
# # Write a Python program to construct
# # the following pattern, using a nested loop number.
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# # 7777777
# # 88888888
# # 999999999
#
# # for i in range(1, 10):
# #     print(f'{i}' * i)
# # https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# # 31. Write a Python program to calculate a dog's
# # age in dog years.
# # Note: For the first two years, a dog year
# # is equal to 10.5 human years. After that,
# # each dog year equals 4 human years.
# # Expected Output:
# #
# # Input a dog's age in human years: 15
# # The dog's age in dog's years is 73
#
# # human_years = int(input('enter dogs age in human years: '))
#
# # dogs_years = 0
# # for year in range(1,human_years+1):
# #     if year <= 2 :
# #         dogs_years += 10.5
# #     else:
# #         dogs_years +=4
# #
# # print(f'The dogs age in human years is {human_years}')
# # print(f'The dogs age in dogs years is {dogs_years}')
#
# # s = 0
# # if human_years >= 2 :
# #     s = 21 + (human_years-2)*4
# # else :
# #     s = 10.5 * human_years
# #
# # print(s)
#
# # g_c =0
# # word = 'google gugugle '
# # for c in word:
# #     if c =='g':
# #         g_c+=1
# #
# # print(word.count('g'))
# # print(g_c)
#
# # ask the user to enter his fav dish
# # 1 - count the spaces using loops
#
# # dish = input('enter your fav dish :')
# # c = 0
# # for n in dish:
# #     if n == ' ':
# #         c += 1
# # print(f'the number of spaces is {c}')
#
#
# # ask the user to insert a pin of 4 digits
# # he can insert a pin 3 times
# # if the pin is correct print welcome home
# # if the pin isn't right in the 3 times print
# # you cant access
#
# # pin = '0140'
# # for i in range(3):
# #     user_pin = input('enter your pin :')
# #     if user_pin == pin:
# #         print('welcome home')
# #         continue
# # else:
# #     print('U got it wrong')
#
# # ask the user to insert a password
# # if the password length greater than 10 print pass
# # else ask them to inter the password again
#
#
# # while True:
# #     password = input('enter your password')
# #     if len(password) >= 10:
# #         break
# #     print('short password try again : ')
# #
# # print('pass')
#
#
# # ask the user to insert a numbers
# # if the user input is odd add it to the odds
# # and if the user input is even multiple by
# # the other evens
# # if the users inserts 0 then stop the program
#
# # input 6 7 18 2 3 9
# # odds_sum: 19
# # even_multi: 216
#
# odds_sum = 0
# even_multi = 1
#
# while True:
#     user_input = int(input('enter a number'))
#     if user_input == 0:
#         break
#     if user_input % 2 ==0:
#         even_multi *= user_input
#     else:
#         odds_sum += user_input
#
# print(f'odds sum {odds_sum}')
# print(f'even mult {even_multi}')


# lists

# numbers = [100,5,8,20,18,5]
# # read items
# # print(numbers)
# # # print(type(numbers))
# # print(numbers[0])
# # print(numbers[-1])
# # print(numbers[1:3])
# # print(numbers[::2])
# # print(numbers.index('flafel')) # index of the first elemnt
# # print(numbers.count(8))
# # print(len(numbers))
# print(numbers)
# # numbers.clear()
# # x = numbers.remove('jackson') #by value
# # print(numbers.pop(0)) # index
# # numbers.sort(reverse=True)
# # numbers.reverse()
# # insert
# numbers.append(199)
# numbers.insert(1, 99)
# numbers[0] = 8888
# numbers.append([1,2,3])
# numbers.extend([1,2,3,4,5])
# print(numbers)

# ask the user to insert his ex's names
# save the name into a list if the name contains a
# exit the loop and print the list if the user insert
# the same name twice

# exs = []
# while True:
#     name = input(' enter you ex name please : ')
#     if name in exs:
#         break
#     if 'a' in name:
#         exs.append(name)
#
# print(exs)


#
# numbers = [100, 8, 15, 44, 22, 1776]
#
# # avg
# # avg = sum(numbers)/len(numbers)
# # sum = 0
# # for n in numbers:
# #     sum+=n
# # print(f'avg = {sum / len(numbers)}')
# # max
# # print(max(numbers))
# # # for n in numbers:
# # #     if n > max:
# # #         max = n
# # # print(f'max = {max}')
# # numbers.sort()
# # print(f'max {numbers[-1]}')
# # # min
# # print(min(numbers))
# #
# # print(f'min {numbers[0]}')
#
# # count of numbers that divide by 5 without remaining
# # c = 0
# # for n in numbers:
# #     if n % 5 == 0:
# #         c += 1
# # print(c)
#
# for n in numbers[:len(numbers)//2]:
#     print(n)
#

