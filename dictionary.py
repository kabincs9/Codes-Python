words = set()
#check function
#to define as function
def check(word):
    retrun word.lower() in words
# load
# dictionary as input
def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
        return true

def size():
return len(words) # as words mentioned or allocated

def unload():
    return True # we dont need to free that one in python as it does for you
# week5 written in python ... like only 12 lines
