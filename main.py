import cv2
import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if success:
        print(img)#getting None
        print(success)#getting False
        cv2.imshow("video", img)
        cv2.waitKey(1)
        if 0xFF == ord('q') :
            break
