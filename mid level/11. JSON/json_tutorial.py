import json

person ={"Name": "Jhon", "Age": 30, "City": "New york", "hasChildren": False, "titles": ["Engg", "Programmer"]}

# personJSON = json.dumps(person)
# personJSON = json.dumps(person, indent=4)
# personJSON = json.dumps(person, indent=4, separators=('; ', '= '))
# personJSON = json.dumps(person, indent=4, sort_keys=True)
personJSON = json.dumps(person, indent=4, sort_keys=True)

print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)