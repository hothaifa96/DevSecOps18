import requests

url = "http://127.0.0.1:6020/dish"

res = requests.get(url)

print(res.status_code)
print(res.json())