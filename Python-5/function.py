def greet():
    print('hello')


def greet_with_name(name):
    print(f'welcome {name}')


def get_user_age(name):
    age = int(input(f'enter you age {name}: '))
    return age

def email_generator(name,company):
    email = name.lower()+'@'+company+'.com'
    print('email generated successfully ')
    return email


greet()
name = 'chen'
greet_with_name(name)
age = get_user_age(name)

email = email_generator(name,'nike')
print(email)