from PIL import Image
import numpy as np

img = Image.open("face.jpg")
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = (i, j, 100)

img.save("new.png")

