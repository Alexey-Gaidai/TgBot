import requests
import json

response = requests.get("https://reqres.in/api/users/2")
mail = response.json()

print(mail["data"]["email"])