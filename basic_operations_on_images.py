import cv2 as cv

img = cv.imread('images/rPhoto3.jpg')

print(img.shape) # returns a tuple of number of rows, columns, and channels
print(img.size)  #returns total no. of pixels is accessed
print(img.dtype) #returns Image dataType is obtained

b,g,r = cv.split(img) #split image into three channels
img = cv.merge((b,g,r)) #merge channels into an image

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
