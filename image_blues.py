#Saurav Hossain
#09/3/18
#This makes pictures blue

import matplotlib.pyplot as plt
import numpy as np


img = plt.imread(input())
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[:,:,0] = 0          
img2[:,:,1] = 0         

#nos: 0 = R; 1 = G; 2 = B

plt.imshow(img2)         
plt.imsave(input(), img2) 