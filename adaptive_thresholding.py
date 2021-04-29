import cv2 as cv
import numpy as np

frame = cv.imread('opencv-master/samples/data/sudoku.png',  0)
#threshold returns two values (return, threshold)
# ret, thresh_bin = cv.threshold(frame, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(frame,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,15,2)

cv.imshow('frame', frame)
# cv.imshow('thresh_bin', thresh_bin)
cv.imshow('thresh_adapt', th2)
key = cv.waitKey(0)
cv.destroyAllWindows()
