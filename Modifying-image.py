##############################################
## The function of this is basically output an image and modify it. ##
##############################################

import cv2 
import numpy as np
import matplotlib.pyplot as plt

# Upload the image selected and converting it into a gray scale. 
img = cv2.imread('chitanda-san.jpg',cv2.IMREAD_GRAYSCALE) 

# Use the cv2 packages to set the image and wait for the use of a key to stop.
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Use the matplotlib to add pixels scales.
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()
