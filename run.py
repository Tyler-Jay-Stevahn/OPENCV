import numpy as np
import cv2
import win32gui
import time



CollectData = True

Train = False

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print (hex(hwnd), win32gui.GetWindowText( hwnd ))


#win32gui.EnumWindows( winEnumHandler, None )

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
result = cv2.VideoWriter(('test.mp4'), 
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         30, size)
while CollectData:
    timer = 500
    if cv2.waitKey(1) == ord('q'):
        break
    result.release()
    result = cv2.VideoWriter(str(str(time.time())+'.mp4'), 
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         30, size)
    while timer > 0:
        # Capture frame-by-frame
        ret, frame = cap.read()
        result.write(frame)
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # Display the resulting frame
        cv2.imshow('frame', frame)
        timer = timer - 1
        if cv2.waitKey(1) == ord('q'):
            break


video_capture = cv2.VideoCapture("Video/2021-11-28_17-25-02.mp4") 
#frameRate = video_capture.get(5) #frame rate
i = 0
while Train:  # fps._numFrames < 120
    frame = video_capture.read()[1] # get current frame
    frameId = video_capture.get(1) #current frame number
    #if (frameId % math.floor(frameRate) == 0):
    if (0 == 0):  # not necessary
        i = i + 1
        cv2.imwrite(filename="Frames/Video"+str(i)+".png", img=frame); # write frame image to file
        #image_data = tf.compat.v1.gfile.FastGFile("screens/"+str(i)+".png", 'rb').read() # get this image file
        cv2.imshow("image", frame)  # show frame in window
        cv2.waitKey(1)  # wait 1ms -> 0 until key input



# When everything done, release the capture
cap.release()
print("released cap")
result.release()
print("released final result")
cv2.destroyAllWindows()
