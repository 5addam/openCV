import cv2 as cv
import numpy as np
path = 'opencv-master/samples/data/'
img1 = np.zeros((300,300,3), np.uint8)
img1 = cv.rectangle(img1, (100,200), (200,100), (255,255,255), -1)
img2 = cv.imread(f'{path}b&w.jpg')
img2 = cv.resize(img2, (300,300))

bit_and = cv.bitwise_and(img1, img2)
bit_or = cv.bitwise_or(img1, img2)
bit_xor = cv.bitwise_xor(img1, img2)

cv.imshow('image1', img1)
cv.imshow('image2', img2)

cv.imshow('bitAnd', bit_and)
cv.imshow('bitOr', bit_or)
cv.imshow('bitXor', bit_xor)

cv.waitKey(0)
cv.destroyAllWindows()