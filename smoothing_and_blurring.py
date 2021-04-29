import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/data/lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateral_filter = cv.bilateralFilter(img, 9, 75, 75)

titles = ['image','2d convolution', 'blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gaussian_blur, median, bilateral_filter]

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()