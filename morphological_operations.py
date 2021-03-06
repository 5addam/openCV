import cv2 as cv
import numpy  as np
from matplotlib import pyplot as plt

#morphological operations are performed on binaray images

img = cv.imread('images/data/smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

#kernal is just a sqaure or some shap we want to apply on image
kernal = np.ones((4,4), np.uint8) # white square

dilation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal, iterations=2)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)

titles = ['images', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(titles)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()