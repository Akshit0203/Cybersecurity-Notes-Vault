import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from pyfirmata import Arduino, util
import time

# Initialize Arduino
board = Arduino('COM5')  # Replace 'COM10' with your Arduino's port
led_pin = 13  # Pin for the LED
board.digital[led_pin].mode = 1  # Set pin as OUTPUT

# Initialize camera
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Virtual button coordinates and size for the LED
button_pos = (50, 100)  # X, Y coordinates for the button
button_size = 100  # Width and height of the button

led_state = False  # Initially, the LED is off
finger_in_button = False  # To track if finger is in the button area
prev_finger_state = False  # To track the previous state of the finger in the button area
prev_click_time = 0
click_threshold = 0.5  # Minimum time between two clicks (in seconds)

checkbox_color = (0, 255, 0)  # Color for the checkbox (initially green)

def update_checkbox_color():
    global checkbox_color, led_state
    if led_state:
        checkbox_color = (0, 0, 255)  # Red if LED is on
    else:
        checkbox_color = (0, 255, 0)  # Green if LED is off

# Create a named window and set it to full screen
cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip the image horizontally

    hands, img = detector.findHands(img)
    
    # Draw virtual button and checkbox
    cv2.rectangle(img, button_pos, (button_pos[0] + button_size, button_pos[1] + button_size), checkbox_color, cv2.FILLED)
    cv2.putText(img, 'LED 1', (button_pos[0] + 10, button_pos[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    if hands:
        hand = hands[0]
        lmList = hand['lmList']  # List of 21 landmarks points
        cursor = lmList[8]  # Index finger tip position

        # Check if cursor is inside the button region
        if button_pos[0] < cursor[0] < button_pos[0] + button_size and button_pos[1] < cursor[1] < button_pos[1] + button_size:
            cv2.rectangle(img, button_pos, (button_pos[0] + button_size, button_pos[1] + button_size), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, 'LED 1', (button_pos[0] + 10, button_pos[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            finger_in_button = True
        else:
            finger_in_button = False

        # Check for click (finger enters and exits button area)
        if finger_in_button != prev_finger_state and finger_in_button:
            current_time = time.time()
            if current_time - prev_click_time > click_threshold:
                prev_click_time = current_time
                led_state = not led_state  # Toggle LED state
                board.digital[led_pin].write(1 if led_state else 0)  # Write state to LED pin

                update_checkbox_color()

        prev_finger_state = finger_in_button

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
