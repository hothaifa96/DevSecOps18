
class Circle:
    r = 5
    color = 'Black'


# print(Circle.r)
# Circle.r = 5.5
# print(Circle.r)
# print(Circle)
c1 = Circle()
c2 = Circle()
print('before change')
print(f'c1.r -> {c1.r}')
print(f'c2.r -> {c2.r}')
c2.border = 'dotted'
print(f'c2.border -> {c2.border}')  # ? Output - c2.border -> dotted
# print(f'c1.border -> {c1.border}')  # error
c1.r = 103
print(c1.color)
# del c1.color #TBD
print('after change')
print(f'c1.r -> {c1.r}')
print(f'c2.r -> {c2.r}')
print(c1.color)