import csv
# csv can do It can read data row by row, with each row represented as a list of strings.
#It can handle different delimiters (e.g., comma, semicolon, tab) using the delimiter parameter.
#It can manage quoting rules, including handling fields that contain the delimiter character by enclosing them in quotes.
#The DictReader class allows reading data as dictionaries, where each row is a dictionary mapping header names to values.
# for a  Any new data written to the file will be added to the end of its existing content.
# for a If the specified file does not already exist, Python will create a new, empty file with that name before appending the data.
file = open("csvphonebook.csv", "a") # a is like a there are all different like b t ...
name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file) # which say open a file and be redy to write hereafter

writer.writerow([name, number])
file.close()
# run two time run code csvphonebook.csv also
# then when we run and add name number it will be saved in next file that was open csv
 # go to phonedictionary.py for more 
