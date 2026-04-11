import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import pyfirmata

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Define parameters
minHand, maxHand = 20, 250
minBar, maxBar = 400, 150
minAngle, maxAngle = 0, 180

# Initialize Arduino board and servo pin
port = "COM12"
board = pyfirmata.Arduino(port)
servoPin = board.get_pin('d:9:s')  # pin 9 Arduino

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from camera")
        break

    hands, img = detector.findHands(img)

    if hands:
        thumbTip = hands[0]["lmList"][4]
        indexTip = hands[0]["lmList"][8]

        # Print the return values of findDistance to understand its structure
        distance_info = detector.findDistance(indexTip, thumbTip)
        print(distance_info)
        
        # Based on the output, adjust the following line
        distance = distance_info[0]
        
        # Interpolate the length to servo value
        servoVal = np.interp(distance, [minHand, maxHand], [minAngle, maxAngle])

        # Draw rectangle and text for length
        cv2.rectangle(img, (100, 100), (360, 30), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f'Length: {int(distance)}', (130, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 3)

        # Draw rectangle and text for servo value
        cv2.rectangle(img, (500, 100), (760, 30), (0, 255, 255), cv2.FILLED)
        cv2.putText(img, f'Servo: {int(servoVal)}', (530, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

        # Draw the servo position bar
        bar = np.interp(distance, [minHand, maxHand], [minBar, maxBar])
        cv2.rectangle(img, (1180, 150), (1215, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (1180, int(bar)), (1215, 400), (0, 255, 0), cv2.FILLED)

        # Write the servo value to the pin
        servoPin.write(servoVal)

    # Display the image
    cv2.imshow("Image", img)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
