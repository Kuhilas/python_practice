import json

# Exercise of creating, transforming, writing and loading .jsons

# 3.2 create python dict

fantasy_items = {
    "name": "Flaming Sword",
    "price": 5000,
    "weight": 20 ,
    "is_magical": True,
    "damage":[20, 50]
} 

print(f"Original data:\n{fantasy_items}\n")

# 3.3 Encode Python dictionary to JSON string

json_fantasy_items = json.dumps(fantasy_items)
# print(json_fantasy_items)

# 3.4 Decode Python dictionary to JSON string

decoded_fantasy_items = json.loads(json_fantasy_items)
# print(decoded_fantasy_items)

# 3.5 Write a .json file 

with open("Fantasy_items.json", "w") as f:
    json.dump(fantasy_items, f, indent=4)

with open("Fantasy_items.json", "r") as f:
    new_dict = json.load(f)

# 3.7-3.9 add a new key value pair, new array/list and new object/dict

new_dict["rarity"] = 'uncommon'
new_dict["sellers"] = ["John", "Peter", "Mary"]
new_dict["description"] = {"text": "This is a flaming sword", "creator": "unknown", "importantYears": [33, 44, 555]}

# 3.10-3.13 Print out price, Peter from sellers and 555 from the nested dict. 

print(new_dict)
print(new_dict["price"])
print(new_dict["sellers"][1])
print(new_dict["description"]["importantYears"][2])

# Extra: Print example line with one line of code 

print(f"Description: {new_dict['description']['text']}\nImportant year: {new_dict['description']['importantYears'][2]} ")

# 9. Remove price, seller and description from the Python object.

del new_dict["price"]
del new_dict["sellers"]
del new_dict["description"]

print("\nFinal dict")
print(new_dict)