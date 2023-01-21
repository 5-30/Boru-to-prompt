import requests
import json

link = input("Which link should I extract tags from ? ")

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
    }
req = requests.get(f'{link}.json', headers=headers)

jsonArray = json.loads(req.text)

print(jsonArray["tag_string"].replace(" ", ", ").replace("(", "\(").replace(")", "\)"))