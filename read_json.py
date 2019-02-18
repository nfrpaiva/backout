import json
from pprint import pprint
with open('data.json') as file:
    data = json.load(file)
pprint(data, indent=2)
json.dump
