from PIL import Image, ImageFilter
import numpy as np
import math
from random import randint
np.set_printoptions(threshold='nan') # prints np arrays untruncated

# completely destroys image's data, no chance at recovery
def destroy(matrix, key):
    for i in range(key):
        matrix = swapRow(matrix, randint(0, matrix.shape[0]-10), randint(0, matrix.shape[0]-10))
    for i in range(key):
        matrix = swapCol(matrix, randint(0, matrix.shape[1]-10), randint(0, matrix.shape[1]-10))
    return Image.fromarray(matrix, 'RGB')

def encrypt(matrix, key):
    for i in range (key):
        for j in range(matrix.shape[0]-10):
            matrix = swapRow(matrix, j, (j+key)%(matrix.shape[0]-10))
    return Image.fromarray(matrix, 'RGB')

#def decrypt():
    # decrypt the image

def swapRow(matrix, row1, row2):
    temp = matrix[row1,:]
    matrix[row1,:] = matrix[row2,:]
    matrix[row2,:] = temp
    return matrix

def swapCol(matrix, col1, col2):
    temp = matrix[:,col1]
    matrix[:,col1] = matrix[:,col2]
    matrix[:,col2] = temp
    return matrix


img = Image.open("face.jpg")
key = 1234
matrix = np.array(img)
img = encrypt(matrix, key)
img.show()
