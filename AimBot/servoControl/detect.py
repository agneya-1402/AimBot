import cv2
import numpy as np
import time

faceClassifier  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera Error!")
    exit()

pressed = False
while (pressed == False):
    ret, framework = cap.read()

    if ret == True:
        gray = cv2.cvtColor(framework, cv2.COLOR_BGR2GRAY)
        face = faceClassifier.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 2)

        for (x, y, w, h) in face:
            cv2.rectangle(framework, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        
        text = "Number of Detected Faces = " + str(len(face))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(framework, text, (0, 30), font, 1, (255, 0, 0), 1)

        cv2.imshow("video", framework)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pressed = True
            break


cap.release()
cv2.destroyAllWindows()