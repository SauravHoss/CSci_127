#Saurav Hossain
#10/23/18
#Quarter Image

import matplotlib.pyplot as plt
import numpy as np

imName = input()
outputname = input()

img = plt.imread(imName)
height = img.shape[0]
width = img.shape[1]
outimg = img[height//2:, :width//2]
plt.imsave(outputname, outimg)