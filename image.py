from PIL import Image
import numpy as np

key = 123;
img = Image.open("face.jpg")
pixels = img.load()


for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = pixels[i, j]
        if i % 2 == 0:
            pixels[i, j] = (r*5, g*5, b*5)
        else:
            pixels[i, j] = (r/5, g/5, b/5)
        # pixels[i, j] = (i, j, 100)

img.save("image_out.jpg")

