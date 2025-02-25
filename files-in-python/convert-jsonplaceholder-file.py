import requests
import csv 


url = 'https://jsonplaceholder.typicode.com/users'
file = 'users.csv'

content=[
    ['name','email']
    ]
# send http request to get all the users 
response = requests.get(url)

if response.status_code // 100 ==2 :
    # get the json data from the response
    users = response.json()
    for user in users:
        user_list= [user['name'],user['email']]
        content.append(user_list)
    # open the csv file in write mode
    with open(file,'w+') as csv_file:
        # create a csv writer
        writer = csv.writer(csv_file)
        writer.writerows(content
        )
    with open('users.txt','w+') as file:
        for user in users:
            file.write(f'username -> {user["name"] } email ===> {user["email"]}' +'\n')