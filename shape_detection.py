import cv2 as cv
import numpy as np

img = cv.imread('images/data/shapes.jpg')
text_color = (0,0,0)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY)

contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 
                             0.01*cv.arcLength(contour, True), 
                             True)
    cv.drawContours(img, [approx], 0, (0,255,0), 1)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv.putText(img, 'Trianlge', (x,y), cv.FONT_HERSHEY_SIMPLEX,
                   0.5, text_color, 1)
    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(contour)
        aspect_ratio = float(w)/h
        print(aspect_ratio)
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            cv.putText(img, 'Square', (x,y), cv.FONT_HERSHEY_SIMPLEX,
                       0.5, text_color, 1)
        else: 
            cv.putText(img, 'Rectangle', (x,y), cv.FONT_HERSHEY_SIMPLEX,
                       0.5, text_color, 1)
    elif len(approx) == 5:
        cv.putText(img, 'Pentagone', (x,y), cv.FONT_HERSHEY_SIMPLEX,
                   0.5, text_color, 1)
    elif len(approx) == 6:
         cv.putText(img, 'Hexagone', (x,y), cv.FONT_HERSHEY_SIMPLEX,
                   0.5, text_color, 1)
    elif len(approx) == 10:
        cv.putText(img, 'Star', (x,y), cv.FONT_HERSHEY_SIMPLEX,
                   0.5, text_color, 1)
    else:
        cv.putText(img, 'Circle', (x,y), cv.FONT_HERSHEY_SIMPLEX,
                   0.5, text_color, 1)

cv.imshow('shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()