########################
## Image arithmetics and Logic. ##
########################

import cv2
import numpy as np

# Loading... the images need to be the same sizes.
img1 = cv2.imread('some_picture.png')
img2 = cv2.imread('some_picture2.png')
##################################
              
# Unite both images.
add = img1 + img2
# Unite both images by + their pixels.
add = cv2.add(img1, img2)

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Unite both images without losing any value.
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
              
cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Add a second picture to a first.
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

# Creating a mask.
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BYNARY_INV)

cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()  

# Using the mask to converting make the background transparent and place it on the first image.
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask+mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, amsk=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res', img1) 
cv2.waitKey(0)
cv2.destroyAllWindows()
