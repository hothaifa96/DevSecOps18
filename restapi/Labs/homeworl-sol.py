######## Lab 1 ########

import requests
url = "https://reqres.in/api/users"

response = requests.get(url)
if 199 < response.status_code <300 :
    print("Request was successful")
    # print(response.headers)
    data = response.json()
    users = data["data"]
    print(type(users))
    path = input('please enter the file name or path ')
    with open(path,'w+') as file:
        for user in users: # iteration on a list of dic [{},{},{}.....{}]
            # print(user)
            file.write(f'{"*"*20} {user["id"]} {"*"*20} \n')
            for k,v in user.items() : # iteration over a dict items [key.value),(),]
                if k == "id":
                    continue
                file.write(f"{v} \n",)
    print("all the data in the file go check for yourself",path)
else:
        print(f"Request was not successful status code {response.status_code}")