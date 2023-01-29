import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0) # open camera == False
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera == True:
    success, frame = cam.read()

    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8')) # decode the data in QR Code to UTF-8
        time.sleep(6)

        cv2.imshow("QR_Scanner", frame)
        cv2.waitKey(1) # 3ms for each frame