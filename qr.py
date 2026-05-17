import os
#  from os library and import that persons library qr code
import qrcode
img = qrcode.make("https://youtu.be/xvFZjo5PgG0")
img.save("qr.png", "PNG")
# portable network graphic give me that type of file
# run this also code qr.png also
