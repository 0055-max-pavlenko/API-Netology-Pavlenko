
import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'

data = requests.get(url).json()
result = {key["name"]:key["powerstats"]["intelligence"] for key in data if key["name"]=="Hulk" or key["name"]=="Captain America" or key["name"]=="Thanos"}

print(f'Самый умный супергерой из трех: {max(result, key= lambda x: result[x])}')