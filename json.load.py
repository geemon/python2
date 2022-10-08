#a python script to fetch data from json file
import json

filename = 'numbers.json'
with open (filename ) as file:
     display =json.load(file)
print(display)