import json

person ={"Name": "Jhon", "Age": 30, "City": "New york", "hasChildren": False, "titles": ["Engg", "Programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('person.json', 'r') as file:
    person = json.loads(file)
    print(person)