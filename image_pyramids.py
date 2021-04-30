import cv2 as cv
import numpy as np 

img = cv.imread('images/data/lena.jpg')
layer = img.copy()
gp = [layer] # gp: Gaussian Pyramid

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)
    
layer = gp[len(gp)-1]
cv.imshow('Upper level Gaussian Pyramid', layer)
lp = [layer] # Laplacian Pyramid

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)
# lower_resolution_1 = cv.pyrDown(img)
# lower_resolution_2 = cv.pyrDown(lower_resolution_1)
# higher_resolution = cv.pyrUp(lower_resolution_2)

# cv.imshow("pyrDown image 1", lower_resolution_1)
# cv.imshow("pyrDown image 2", lower_resolution_2)
# cv.imshow("pyrUp image", higher_resolution)
cv.imshow("original image", img)
cv.waitKey(0)
cv.destroyAllWindows()