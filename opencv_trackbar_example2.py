import cv2 as cv
import numpy as np

def nothing(pos):
    print(pos)

cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 0, 255, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image',0, 1, nothing)
while(1):
    img = cv.imread('images/messi.jpeg')
    pos = cv.getTrackbarPos('CP','image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (150,150), font, 4, (0,0,255))
    
    k= cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        pass #don't change any values
    else:
        #change to rbg channles of the image
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    img = cv.imshow('image', img)
    
cv.destroyAllWindows()