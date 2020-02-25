import cv2,time
first_frame = None
video =cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
   check,frame = video.read()    
   print(check)
   print(frame)
   
 
   
   key=cv2.waitKey(1000)
   gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   gray=cv2.GaussianBlur(gray,(21,21),0)
   
   if first_frame is None:
       first_frame=gray
       continue
   delta_frame=cv2.absdiff(first_frame,gray)
   
#    thresh_delta= cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
   
   
    
   cv2.imshow("Gray Frame",gray)
   cv2.imshow("Delta Frame",delta_frame)
   cv2.imshow("th",thresh_delta)         
   if key==ord('q'):
       break
   
video.release()

cv2.destroyAllWindows()


