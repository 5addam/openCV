import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/data/messi5.jpg', 0)
laplacian = cv.Laplacian(img, cv.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1)

sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

sobelCombined = cv.bitwise_or(sobel_x, sobel_y)

canny = cv.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'Sobel Combined', 'Canny']
images = [img, laplacian, sobel_x, sobel_y, sobelCombined, canny]
for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()