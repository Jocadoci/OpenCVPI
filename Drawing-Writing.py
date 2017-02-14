##########################
## Drawing and Writing on Image. ##
##########################

import numpy as np
import cv2

img = cv2.imread('some_picture.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (blue,green,red), 15)
cv2.rectangle(img, (15,25), (200,150), (blue,green,red), 5)
cv2.circle(img, (100,63), 55, (blue,green,red), -1)

pts = np.array([[10,5], [20, 30], [70,20], [50,10]], np.int32)
cv2.polylines(img, [pts], True, (blue,green,red, 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Some text here.', (0, 130), font, 1, (blue,green,red), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
