import os 
import json 

f = open("id_descript.txt", "r")
data = f.read()
id_description_dict = json.loads(data)
# print(id_description_dict)
print(len(id_description_dict))
print(type(id_description_dict))

mdfile = open("get_barcodes.md", "w")
header = f"| id | description | images | barcode |\n"
mdfile.write(header)
below_header = f"| ---- | ---- | ------------- | ------- |\n"
mdfile.write(below_header)

sorted_dict = dict(sorted(id_description_dict.items(), key=lambda item: item[0]))
for k, v in sorted_dict.items():
    line = f"| {k} | {v} | ![](./images/{k}.jpg) |  |\n"
    mdfile.write(line)