s = input("Do you agree? ")
# lower from library
t = s.lower() # to change all into lower rather like YES OR...
if  t in ["Y", "y", "yes", "ye" ]: # adding also yes or anything
    print("Agreed.")
elif t in ["N", "no"]:
    print("Not Agreed.")
# just like agree but in for fast
