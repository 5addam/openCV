import numpy as np
import cv2 as cv

# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)


def click_event(event, x_axis, y_axis, flags, param):
    
    #create and open new image filled with the rgb of clicked axises
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y_axis, x_axis, 0]
        green = img[y_axis,x_axis, 1]
        red = img[y_axis,x_axis, 2]
        cv.circle(img, (x_axis,y_axis), 3, (0,0,255),-1)
        myColorImg = np.zeros((512,512,3),np.uint8)
        
        #fill img with the given channels
        myColorImg[:] = [blue,green,red]
        
        cv.imshow('color', myColorImg)
        
    # draw lines b/w two points
    # if event == cv.EVENT_LBUTTONDOWN:
    #     cv.circle(img, (x_axis,y_axis), 3, (255,0,21),-1)
    #     points.append((x_axis,y_axis))
    #     if len(points) >=2:
    #         cv.line(img, points[-1], points[-2], (255,0,21),5)
    #         cv.imshow("image", img)
    
    # print axises value 
    # if event == cv.EVENT_LBUTTONDOWN:
        # print(x_axis,', ',y_axis)
        # font = cv.FONT_HERSHEY_SIMPLEX
        # strXY = f'{x_axis} , {y_axis}'
        # cv.putText(img, strXY,(x_axis,y_axis) , font, .5, (255,69,6),2,cv.LINE_AA)
        # cv.imshow("image", img)
    
    # get rgb value of the axises    
    # if event == cv.EVENT_RBUTTONDOWN:
    #     blue = img[y_axis,x_axis, 0]
    #     green = img[y_axis,x_axis, 1]
    #     red = img[y_axis,x_axis, 2]
    #     font = cv.FONT_HERSHEY_SIMPLEX
    #     strBGR = f'{blue} , {green} , {red}'
    #     cv.putText(img, strBGR,(x_axis,y_axis) , font, .5, (0,255,255),2,cv.LINE_AA)
    #     cv.imshow("image", img)
        

# img = np.zeros((512,512,3), np.uint8)
img = cv.imread('images/rPhoto3.jpg')

cv.imshow("image", img)

points = []

cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
