import serial
import cv2
import math
from cvzone.HandTrackingModule import HandDetector

serialcomm = serial.Serial('COM5', 9600)
serialcomm.timeout = 1
cap = cv2.VideoCapture(0) 
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (500, 500))
    hands, _ = detector.findHands(img)  # Use findHands to get hand landmarks
    if hands:
        hand = hands[0]  # Assuming only one hand is detected
        x1, y1 = hand['lmList'][4][0], hand['lmList'][4][1]
        x2, y2 = hand['lmList'][8][0], hand['lmList'][8][1]
        cv2.circle(img, (x1, y1), 7, (0, 255, 255), 1)
        cv2.circle(img, (x2, y2), 7, (0, 255, 255), 1)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        d = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 1.0)
        d = int((d / 110) * 255)
        if 0 < d < 256:
            cv2.putText(img, str(d), (20, 30), cv2.FONT_HERSHEY_COMPLEX, .7, (255, 255, 255), 1)     
            serialcomm.write(str(d).encode() + b'\n')

    cv2.imshow('Image', img)  
    if cv2.waitKey(20) & 0xFF == 27:
        break        

cv2.destroyAllWindows()
