from cs50 import get_int
# like from not form
scores = []

for i in range(3):
    score = get_int("Score: ")
    scores.append(score)  # like putting in at the end of the list
# build in appen function or scores = scores + [score]
# or for append .. scores += [score] like we can add more and more thing to list 
average = sum(scores) / len(scores)

print(f"Average: {average}")
