# # class Employee:
# #     def __init__(self, name, salary):
# #         self.name = name
# #         self.salary = salary
#
#
# # emp5 = Employee(salary=10000 , name= 'hodi')
# # # define 3 emp form the user input
# # employees = []
# # for i in range(3):
# #     while True:
# #         name = input('please enter the employee name:')
# #         if name == '' or name.isdigit() or name.isspace():
# #             continue
# #         salary = input('enter salary (numbers)')
# #         if salary.isdigit():
# #             salary = int(salary)
# #         else:
# #             continue
# #         emp = Employee(name,salary)
# #         employees.append(emp)
# #         break
# #
# # print(employees)
# # for emp in employees:
# #     print(f'{emp} employee name :{emp.name} salary = {emp.salary}')
#
# # emp1 = Employee('chen',19000)
# # emp2 = Employee('lev',29000)
# #
# # print(emp1.name)
# # print(emp2.name)
#
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #
# #
# # p1 = Person('dana',20)
# # p2 = Person('mike',30)
# #
# #
# # print(p1.name)
# # print(p1.age)
# # print(p2.name)
# # print(p2.age)
#
#
# class Dog:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     def bark(self):
#         if self.age>3:
#             print(f'{self.name} says : whrooph wrooooph')
#         else:
#             print(f'{self.name} says : howw howww')
#
#     def __str__(self):
#         return f'from Class Dog<< name-{self.name} age-{self.age}>>'
#
#
# dog1 = Dog('jojo',4 , 'husky')
# dog2 = Dog('pita',3 , 'nakniik')
#
# print(dog1)
# print(dog2)
# # dog1.bark()
# # dog2.bark()
#
#

import math
class Point:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.distance = self.calc_distance()

    def __str__(self):
        return f'({self.x},{self.y}) with the color -> {self.color}'
    def calc_distance(self):
        dis = math.sqrt(self.x**2 + self.y**2)
        return dis


p1 = Point(3,6,'black')
p2 = Point(9,1,'white')

print(p1)
print(f'distance {p1.distance}')
print(p2)
print(f'distance {p2.distance}')

# print(p1.calc_distance())
# print(p2.calc_distance())

