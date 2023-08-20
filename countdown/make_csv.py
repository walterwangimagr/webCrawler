import os 
import json 

f = open("id_descript.txt", "r")
data = f.read()
id_description_dict = json.loads(data)
# print(id_description_dict)
print(len(id_description_dict))