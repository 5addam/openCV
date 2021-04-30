import cv2 as cv 
import numpy as np

img = cv.imread('images/data/opencv-logo.png')
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 225, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(f'No. of Contours {len(contours)}')

cv.drawContours(img, contours, 10, (0,255,0), 3)

cv.imshow('Image', img)
cv.imshow('Image GRAY', imgray)
cv.waitKey(0)
cv.destroyAllWindows()