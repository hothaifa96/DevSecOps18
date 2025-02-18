#
# class Student:
#     def __init__(self,name,age,id,courses):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.courses = courses
#
#     def __str__(self):
#         return f'{self.courses}<=>{self.id}<=>{self.name}<=>{self.age}'
#
# st1 = Student('zohar',20,314664332,['DevSecOps'])
# st2 = Student('amir',55,7657657655,['DevSecOps','cooking for zero to hero'])
#
# print(st1)
# print(st2)
#


class Vehicle:
    def __init__(self, make, model, year: int):
        self.make = make
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f'{self.make}  {self.model} {self.year}'

    def move(self):
        print('moving ....')


class Car(Vehicle):
    def __init__(self, make, model, year: int, hp, gear, wheels):
        super().__init__(make, model, year)
        self.hp = hp
        self.gear = gear
        self.wheels = wheels


class Plan(Vehicle):
    def __init__(self, make, model, year: int, engine_make, seats):
        super().__init__(make, model, year)
        self.engine_make = engine_make
        self.seats = seats


class Coupe(Car):
    def __init__(self, make, model, year: int, hp, gear, wheels, cc):
        super().__init__(make, model, year, hp, gear, wheels)
        self.cc = cc
        
    def move(self):
        print('0 to 100 in 2.9')


car1 = Car('mazda', '3', 2023, 200, 5, 4)
plan1 = Plan('boeing', '787', 2010, 'rolls royce', 300)
car2 = Coupe('bmw', 'm4 gt4', 2024, 900, 7, 4, 3000)
vehicle1 = Vehicle('bmw', 'm4 gt4', 2024)
print(car1)
print(plan1)

car1.move()
plan1.move()
car2.move()
print(isinstance(car1, Car))
print(isinstance(car1, Vehicle))
print(isinstance(plan1, Car))
