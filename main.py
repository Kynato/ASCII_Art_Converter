import sys
from PIL import Image

image_path = 'sample.png'

with Image.open(image_path) as img:
    w, h = img.size
    ratio = h/w
    new_w = 120 #why tho?
    new_h = int(ratio * new_w * 0.55) #why?
    img = img.resize( (new_w, new_h) )
    img.show()
    print(img.size)
