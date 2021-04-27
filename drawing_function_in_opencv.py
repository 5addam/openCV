import cv2 as cv
import numpy as np

# img = cv.imread('images/rPhoto2.jpeg',1)
img = np.zeros([])

#image, starting point, ending point, line color, thickness
img = cv.line(img,(0,0),(255,255),(255,255,0),5)
img = cv.arrowedLine(img,(0,255),(255,255),(255,1,0),5)
img = cv.rectangle(img, (384,0), (510,128), (0,0,255),5)
img = cv.circle(img, (500,45), 45, (255,0,255),-1)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, "OpenCV", (10,600), font, 4, (255,69,240),10,cv.LINE_AA)
cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()