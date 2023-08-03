import json

with open("database.json", 'r') as f:
    database = json.load(f)

print(database)

# i = 0
# for key, value in database.items():
#     print(key)
#     print(value)
#     i += 1 
#     if i == 2:
#         break