# phonebook type
people = [
    {"name": "Yuliia", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "Jhon", "number": "+1-617-495-1000"}
]

name = input("Name: ")
for person in people: #first iteration yuliia like ..looking the people from that list
    if person["name"] == name: # if this person name field has this name then it is like indexing into a ditionary like in c like brackrt 1 2 3
        number = person["number"] # by looking their number field and get their number
        print(f"Found {number}")
        break
else:
    print("Not Found")
    # in short go to phonebookfast.py
