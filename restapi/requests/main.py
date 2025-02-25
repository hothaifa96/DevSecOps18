import requests 

# url = 'https://jsonplaceholder.typicode.com/users'

# response = requests.get(url)

# print(f'the status code for the url {url} -> {response.status_code}')
# if response.status_code // 100 == 2:
#     print('the url is working fine')
# else:
#     print('the site isnt responsing please check again')

# users = response.json() # [ dict , dict ,dict]
# print(f'the type of users is { type(users)}')
# print(f'the type user[0] are {type(users[0])}')
# print(f'the type user[0]["name"] are { type(users[0]["name"])}')

# for user in users:
#     print(user["email"])



response2 = requests.get('https://reqres.in/api/users')
print('success' if response2.status_code < 300 else 'error')

data = response2.json()
print(type(data))
users = data['data']
print(type(users))

print(f'the number of users in this api is {len(users)}')
print(type(users[3]))
print(f'the email of the 4th user is {users[3]["email"]}')
print(f'the avatar of the last user is {users[-1]["avatar"]}')


# list all the names and the email of the users using one loop 
# formatted    name ---- email

for user in users:
    print(f'{user["first_name"]} ------ {user["email"]}')