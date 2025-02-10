# txt = 'yaba daba doo'
#
# txt.upper()
# t1 = (1,2,3,4)
# number1 = 1

class Rectangle:
    a = 4
    b = 2


r1 = Rectangle()
r2 = Rectangle()
print(r1)  # -> <__main__.Rectangle object at 0x10480d050>
print(type(r1)) # --> <class '__main__.Rectangle'>
print('before change r1.b')
print(r1.b)
print(r2.b)
print('after change r1.b')
r1.b = 10
Rectangle.b = 100
print(r1.b)
print(r2.b)


print(f'Rectangle.b -> {Rectangle.b}')