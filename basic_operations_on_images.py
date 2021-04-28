import cv2 as cv



img = cv.imread('images/messi.jpeg')
img2 = cv.imread('images/rolando.jpg')

print(img.shape) # returns a tuple of number of rows, columns, and channels
print(img.size)  #returns total no. of pixels is accessed
print(img.dtype) #returns Image dataType is obtained

b,g,r = cv.split(img) #split image into three channels
img = cv.merge((b,g,r)) #merge channels into an image


#copying objects in an image
#upper-left and lower-right y-axises , upper-left and lower-right x-axises 
# ball = img[380:450, 400:470] #copying all the pixels of the ball
# print(ball.shape)
# print(ball.size)
#creating ball on different coordinates on images
# img[400:470, 100:170] = ball

#to add two images they need to be of the same array-size
img = cv.resize(img, (512,512))
img2 = cv.resize(img2, (512,512))
# dst = cv.add(img, img2)
dst = cv.addWeighted(img, .6, img2, .4, 0)

cv.imshow('image', dst)
cv.waitKey(0)
cv.destroyAllWindows()
