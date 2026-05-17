people = {
  "Yuliia": "+1-617-495-1000",
  "David": "+1-617-495-1000",
   "Jhon": "+1-617-495-1000"
}
# other in dictionaryphonebook
name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}") # name location
else:
    print("Not Found")


# The in operator is used to check if a value is present within a sequence
# (like a list, tuple, string, set) or a collection
# (like a dictionary, where it checks for keys)
# It returns True if the value or key is found, and False otherwise. 
