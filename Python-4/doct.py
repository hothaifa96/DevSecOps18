# #
# # l1 = [1,2,3,4,5]
# # # print(l1)
# # # print(type(l1))
# # # l1.append(6)
# # # print(l1)
# # # l1.remove(3)
# # # l1.reverse()
# # # print(l1)
# # t1 = (1,2,3,4,5) # fixed list immutable
# # # print(t1)
# # # print(type(t1))
# # # # t1[2]=3
# # s1 = {1,2,3,3,3,4,5,5,1,1,2}
# # # print(s1)
# # # print(type(s1))
# # # s1.add(3)
# # # print(s1)
# #
# # names = ['hodi','hodi','chen','chen','mike','eldan']
# #
# # names = list(set(names)) # list ---delete duplicates--> set -> list
# #
# # ()
# # print(names)
#
# # string ->> list char
# # x = 'hodi,love,pizza,and,sushi,and,today,he,ate,toast'
# #
# # l1 = x.split(',')
# # new_x = '@gmail.com '.join(l1)
# # print(l1)
# # print(new_x)
# #
# # ip = input('enter you ip please with subnet mask xx.xx.xx.xx/xx ' )
# #
# #
# # subnet = int(ip[ip.find('/')+1 : ]) //8  # /xx without /
# # ip = ip[:ip.find('/')] # xx.xx.xx.xx
# # ip_bytes = ip.split('.') # [xx,xx,xx,xx]
# # print(ip)
# # print(ip_bytes)
# # print(subnet)
# # #               xx.xx.0.0
# # print('.'.join(ip_bytes[:subnet])+'.0'*(4-subnet))
#
# # dict
#
# # d1 = {
# #     'name': 'hodi',
# #     'dream_car': 'q8',
# #     'age': 90
# #       }
# #
# # # print(d1)
# # # print(type(d1))
# #
# # # d1.clear()
# # # d1.pop('name')
# # # print(d1.get('salary'))
# # # print(d1['salary'])
# # # k = list(d1.keys())
# # # v = d1.values()
# # # print(k)
# # # print(v)
# # kv= d1.items()
# # d1['name'] ='castro'
# # d1['job'] = 'truck driver'
# # print(d1)
# # print(kv)
#
# computer = {
#     'ram': 16,
#     'company': "Sony",
#     'screen': 16,
#     'model': 'gr1',
#     'price': 9720.90,
# }
#
# # for key in computer:
# #     print(f'{key} -> {computer[key]}')
# #
# # for values in computer.values():
# #     print(values)
# print(computer.items())
# for k,v in computer.items():  # [(x,x),(x,x),(x,x),(x,x)]
#     print(f'{k} are {v}')