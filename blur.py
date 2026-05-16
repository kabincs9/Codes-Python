# like blur in week 4 using python
# which already come from image so
# from python library 
from PIL import Image, ImageFilter
# to open the file
before = Image.open("bridge.bmp") # after filteration
after = before.filter(ImageFilter.BoxBlur(1))# passing as a agrument
after.save("out.bmp")# save this file
# so to copy from problem cp srcweek4/.....bridge.bmp then code ... python
# if we do some change like 1 to 10 again ls then there come out.bmp code out.bmp it goes here
