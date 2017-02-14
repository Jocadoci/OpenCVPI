##################################################################
## The code's function is to set the webcam and also turning it gray color on another window. ##
##################################################################

import cv2
import numpy as np

# The function 'cap' is to capture the first camera in your system.
cap = cv2.VideoCapture(0)
# 'fourcc' is set to write the camera captured to display it in 'XVID' format.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 'out' function is saving the video giving it at preset sizes and format.
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# While the code is receiving the signal of the camera is goinf to display it.
while True:
    ret, frame =  cap.read()
    cv2.imshow('frame', frame)

    # Get it the frame to conver it to gray scale.
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('gray', gray)

    # Outwriting/saving the video.
    out.write(frame)

    # The while is going to proceed until the key 'q' is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q')
        break

cap.release()
out.release()
cv2.destroyAllWindows()
