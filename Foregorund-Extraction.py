##########################
## GrabCut Foreground Extraction. ##
##########################

import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread('some_image.jpg')
mask = np.zeros(img.shape[:2], np.unit8)

bgdModel =  np.zeros((1,65), np.float64)
fgdModel =  np.zeros((1,65), np.float64)

# This is the rectangle that is going crop the selected.
rect = (161, 79, 150, 150)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
