import cv2 as cv
from  matplotlib import pyplot as plt

img = cv.imread('images/data/lena.jpg',-1)
cv.imshow('image', img)

#matplotlib shows the image in rgb (cv reads it in bgr)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
#hides x and y axis values
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()