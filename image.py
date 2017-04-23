from PIL import Image
import numpy as np

key = 5;
img = Image.open("face.jpg")
pixels = img.load()


for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = pixels[i, j]
        if i % 2 == 0:
            pixels[i, j] = (r*key, g*key, b*key)
        else:
            pixels[i, j] = (r/key, g/key, b/key)
        # pixels[i, j] = (i, j, 100)

img.save("image_out.jpg")

