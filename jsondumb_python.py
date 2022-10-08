#a python script with json.dump to store date to file
import json


#Data to store into file
data_values = [1,2,3,4,6]
data_val2 = ['esi', 'ama', 'kofi']
#file to write to 
filename = 'numbers.json'
with open(filename, 'a') as file:
    json.dump(data_values,file)
    json.dump(data_val2,file)