import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

frame = cv.imread('opencv-master/samples/data/gradient.png',0)
#threshold returns two values (return, threshold)
ret, thresh_bin = cv.threshold(frame, 50, 255, cv.THRESH_BINARY)
ret, thresh_bin_inv = cv.threshold(frame, 200, 255, cv.THRESH_BINARY_INV)
ret, thresh_trunc = cv.threshold(frame, 127, 255, cv.THRESH_TRUNC)
ret, thresh_tozero = cv.threshold(frame, 127, 255, cv.THRESH_TOZERO)
ret, thresh_tozero_inv = cv.threshold(frame, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['original','binary','binary_inv','trunc','tozero','tozero_inv']
images = [frame,thresh_bin,thresh_bin_inv,thresh_trunc,thresh_tozero,thresh_tozero_inv]

for i in range(6):
    #2rows, 3columns, index
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

# cv.imshow('frame', frame)
# cv.imshow('thresh_bin', thresh_bin)
# cv.imshow('thresh_bin_inv', thresh_bin_inv)
# cv.imshow('thresh_trunc', thresh_trunc)

plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()
