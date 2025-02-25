import requests 

todos_url = "https://jsonplaceholder.typicode.com/todos"

res = requests.get(todos_url)

if 199 < res.status_code< 300:
    print(f"Request was successful status code {res.status_code}")
    todos = res.json()
    for todo in todos:
        print(f"Title: {todo['title']} ",end=' ')
        user_url = f"https://jsonplaceholder.typicode.com/users/{todo['userId']}"
        user_res = requests.get(user_url)
        user = user_res.json()
        print(f"User Name: {user['name']}")
else:
    print('try again later please ')