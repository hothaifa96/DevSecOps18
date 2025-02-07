# short hand if [list comprehension]

# requirements
# for -> list
# output -> new list
#
# user_salary = [10,12,16,71,1,2,16,71,8,10,11,11]
# bl = []
# for salary in user_salary :
#     if salary > 10 :
#         bl.append(salary)
#
# print(bl)

#``
# user_salary = [10,12,16,71,1,2,16,71,8,10,11,11]
# bl = [salary*0.2 for salary in user_salary if salary>10]
# print(bl)
#

# l1 = []
#
# for i in range(101):
#     l1.append(i)
#
# print(l1)
l1 = [i**0.5 for i in range(101) if i % 4 == 0]
print(l1)