##############
## Color Filtering.##
##############

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # Convert the frame of video capture to a hsv color set.
    _, frame =  cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range of what color you want to capture.
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([255,255,255])

    #dark_red = np.unit8([[[12,22,121]]])
    #dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

    # After setting the range of color, this create the mask and also the frame with the color targeted.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv.bitwise_and(frame, frame, mask = mask)

    #####################
    ## Blurring and Smoothing. ##
    #####################
              
    kernel = np.ones((15,15), np.float32)/255
    smoothed = cv2.filter2D(res, -1, kernel)              

    blur = cv2.GaussianBlur(res, (15,15), 0)

    median = cv2.medianBur(res, 15)

    cv2.imshow('smoothed', smoothed)

    cv2.imshow('blur', blur)

    cv2.imshow('median', median)

    ##########################
    ##  Morphological Transformations. ##
    ##########################

    kernel =  np.ones((5,5), np.unit8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)                            
    
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)   

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)              

    ###########################################
              
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)        
    cv2.imshow('res', res)              

    k =  cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
