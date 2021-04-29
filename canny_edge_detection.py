import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/data/lena.jpg', 0)
canny = cv.Canny(img, 100, 200)

titles = ['image', 'Canny']
images = [img, canny]
for i in range(len(titles)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()