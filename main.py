from sys import argv
from os import system

from PIL import Image

# because font chars are not squares
FONT_RATIO_MULTIPLIER = 0.35
# equal to output width
DENSITY = 128

# if runs from the cmd with image passed as a argument
try:
    image_path = argv[1]
    # then tries to receive 2nd argument = density
    try:
        DENSITY = int(argv[2])
    except:
        DENSITY = 128
except:
    # ADD normal IF and check whether the file exists or not
    # then return to sample.png if not
    image_path = input('Image path: ')
    try:
        print('Default density = 128')
        DENSITY = int(input('Desired density (0<): '))
    except:
        DENSITY = 128

assert DENSITY > 0

# open image and get the size
with Image.open(image_path) as img:
    w, h = img.size
    ratio = h/w
    
    # calc new size
    new_w = DENSITY
    new_h = int(ratio * new_w * FONT_RATIO_MULTIPLIER) 

    # resize the image
    img = img.resize( (new_w, new_h), resample=Image.NEAREST )

    # gray mode
    img = img.convert(mode='L')

    # returns the pixels one by one
    pixels = img.getdata()

# 'colors' we use in graded order
chars = ["B","S","#","&","@","$","%","*","!",":","."]
# convert pixel brightness to adequate char
new_pixels = [chars[pixel//25] for pixel in pixels]
# whole image in one string
new_pixels = ''.join(new_pixels)

# string + formatting = result ascii art
pixel_count = len(new_pixels)
ascii_img = [ new_pixels[index:index + new_w] for index in range(0, pixel_count, new_w) ]
ascii_img = '\n'.join(ascii_img)

# save the art into the file
with open('ascii_image.txt', mode='w') as f:
    f.write(ascii_img)

# finally open the file
system('notepad.exe ascii_image.txt')