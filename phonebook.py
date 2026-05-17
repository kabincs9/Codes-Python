names = ["Yuliia", "David", "Jhon"]

name = input("Name: ")

for n in names:
    if name == n: # current name that we are searching for
        print("Found")
        break
    else:
        print("Not found")
# if we use enter it will continue # in next line before like next
# or directly
# if name in names:
# print("Found")
# else:
# print("Not found")
