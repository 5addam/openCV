import cv2 as cv

# reads image from the given path
# img = cv.imread('images/rPhoto2.jpeg')

# open img in a new window
# cv.imshow("Image",img)
# reading videos
capture = cv.VideoCapture('videos/cats.mp4')

# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))

# read video frame by frame
while capture.isOpened:
    isTrue, frame = capture.read()

    # if letter 'd' is presded, stop the video
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

    elif isTrue: #frame is available
        width = capture.get(cv.CAP_PROP_FRAME_WIDTH) #frame width
        height = capture.get(cv.CAP_PROP_FRAME_HEIGHT) #frame height
        
        # out.write(frame)
        # convert img to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        #show frame
        cv.imshow("Video", gray)
    else: #frame not read properly || end of frames
        break

capture.release()
out.release()
cv.destroyAllWindows()

# waits for a key to be pressed(delay)
# cv.waitKey(0)
