import requests
import json

link = input("Which link should I extract tags from ? ")

req = requests.get(f'{link}.json')

jsonArray = json.loads(req.text)

print(jsonArray["tag_string"].replace(" ", ", ").replace("(", "\(").replace(")", "\)"))
