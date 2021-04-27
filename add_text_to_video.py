import cv2 as cv
import datetime
cap = cv.VideoCapture('videos/cats-wwe.mp4')
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#setting widht
# cap.set(3, 3000)
#setting height
# cap.set(4, 1000)

# print(cap.get(3)) # same as print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(4)) # same as print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        font = cv.FONT_HERSHEY_SIMPLEX
        text = f'Width: {cap.get(3)}  Height: {cap.get(4)}'
        dateT = f'{datetime.datetime.now()}'
        cv.putText(frame, dateT, (10,50), font, 1, (255,69,5), 2, cv.LINE_AA)
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv.destroyAllWindows()
