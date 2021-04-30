import cv2 as cv
import numpy as np

cap = cv.VideoCapture('images/data/vtest.avi')
ret, frame_1 = cap.read()
ret, frame_2 = cap.read()

while cap.isOpened():
    # absolute difference b/w two frames
    diff = cv.absdiff(frame_1, frame_2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours, heriarchy = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # cv.drawContours(frame_1, contours, -1, (0,255,0), 3)
    for contour in contours:
        (x_axis, y_axis, width, height) = cv.boundingRect(contour)
        
        if cv.contourArea(contour) < 900:
            continue
        cv.rectangle(frame_1, (x_axis, y_axis), 
                     (x_axis+width, y_axis+height),
                     (0,255,0), 3)
        cv.putText(frame_1,
                   "Status: {}".format('Movement'),
                   (10, 20),
                   cv.FONT_HERSHEY_SIMPLEX,
                   1,
                   (0,0,255),
                   3)
    cv.imshow('Video', frame_1)
    
    frame_1 = frame_2
    ret, frame_2 = cap.read()
    
    if cv.waitKey(40) == 27:
        break
cv.destroyAllWindows()
cap.release()