from PIL import Image, ImageFilter # taking from library import ...
before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.FIND_EDGES)#INBUILD FEATURE LIKE FIND_EDGES
after.save("out.bmp")
# code edge.py .... python edge.py .. code out.bmp

