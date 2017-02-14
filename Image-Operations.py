##################
## Image Operations. ## 
##################

import numpy as np
import cv2

# Loading the image.
img = cv2.imread('some_picture.jpg', cv2.IMREAD_COLOR)

# Selecting a particular pixel and print the color value. 
px = img[55,55]
print(px)

# Converting a particular pixel and change the color value.
img[55,55] = [blue,green,red]
px = img[55,55]
print(px)

# 'Region of Image', all the pixel values.
roi = img[100::150, 100::150]
print(roi)
              
# Converting the selected region of image and filling it on any color.
img[100::150, 100::150] = [blue, green, red]
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cut and paste, the selected region of image.
any_name = img[Re::gi, o::n]
img[0::gi-Re, 0::n-o] = any_name
