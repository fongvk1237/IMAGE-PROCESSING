import cv2
import numpy
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_detect = face_cascade.detectMultiScale(gray_img,1.2,5)
        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=3)
            cv2. imshow("Output",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("e"):       
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()