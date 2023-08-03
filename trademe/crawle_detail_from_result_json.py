import json 
from one_property import get_property_detail

with open("result.json", "r") as f:
    id_url_dict = json.load(f)

id_details_dict = {}

for id, url in id_url_dict.items():
    id_details_dict[id] = get_property_detail(url)
    

with open("database.json", "w") as f:
    json.dump(id_details_dict, f)


