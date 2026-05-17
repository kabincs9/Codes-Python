from cs50 import get_int
# if we only write import cs50 error with traceback error as some people have named same in cs50
# if you want to use use like  n = cs50.get_int("Height: ")  as the function is inside cs50 library to import cs50
while True: # start a infinite loop that i want to break up when i am redy as not do while like c
      n = get_int("Height: ")
      if n > 0:
            break

for i in range(n):
      print('#')
