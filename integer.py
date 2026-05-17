# to code if human have not only tyoe string also numeric string 1 2 3
# exceptions
n = input("Input: ")
# conditionals easily
if n.isnumeric():
    print("Integer.")
else:
    print("Not Integer.") # work easily  down onw

# or directly but show error when wrong input 1 line
#n = int(input("Input:")) value error if enter ab.. as base 10
# this is called exceptions like terminate if input is wrong

# to fix this
# try:
# n = int(input("Input:"))
# print("Integer")
# except ValueError: # if error show this
# print("Not integer.") # look in exceptions.py
