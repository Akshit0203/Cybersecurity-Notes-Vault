import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from pyfirmata import Arduino, util
import time

# Initialize Arduino
board = Arduino('COM10')  # Replace 'COM10' with your Arduino's port
led_pins = [13, 12, 11]  # Pins for three LEDs (adjust as per your setup)
for pin in led_pins:
    board.digital[pin].mode = 1  # Set pins as OUTPUT

# Initialize camera
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Virtual button coordinates and size for three LEDs
button_pos = [(50, 100), (200, 100), (350, 100)]  # X, Y coordinates for each button
button_size = 100  # Width and height of each button

led_states = [False, False, False]  # Initially, all LEDs are off
finger_in_buttons = [False, False, False]  # To track if finger is in button areas
prev_finger_states = [False, False, False]  # To track previous states of fingers in button areas
prev_click_times = [0, 0, 0]
click_threshold = 0.5  # Minimum time between two clicks (in seconds)

checkbox_colors = [(0, 255, 0), (0, 255, 0), (0, 255, 0)]  # Colors for checkboxes (initially green)

def update_checkbox_colors():
    global checkbox_colors, led_states
    for i in range(len(led_pins)):
        if led_states[i]:
            checkbox_colors[i] = (0, 0, 255)  # Red if LED is on
        else:
            checkbox_colors[i] = (0, 255, 0)  # Green if LED is off

# Create a named window and set it to full screen
cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip the image horizontally

    hands, img = detector.findHands(img)
    
    # Draw virtual buttons and checkboxes
    for i, pos in enumerate(button_pos):
        cv2.rectangle(img, pos, (pos[0] + button_size, pos[1] + button_size), checkbox_colors[i], cv2.FILLED)
        cv2.putText(img, f'LED {i+1}', (pos[0] + 10, pos[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    if hands:
        hand = hands[0]
        lmList = hand['lmList']  # List of 21 landmarks points
        for i, pos in enumerate(button_pos):
            cursor = lmList[8]  # Index finger tip position

            # Check if cursor is inside the button region for each LED
            if pos[0] < cursor[0] < pos[0] + button_size and pos[1] < cursor[1] < pos[1] + button_size:
                cv2.rectangle(img, pos, (pos[0] + button_size, pos[1] + button_size), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, f'LED {i+1}', (pos[0] + 10, pos[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                finger_in_buttons[i] = True
            else:
                finger_in_buttons[i] = False

            # Check for click (finger enters and exits button area)
            if finger_in_buttons[i] != prev_finger_states[i] and finger_in_buttons[i]:
                current_time = time.time()
                if current_time - prev_click_times[i] > click_threshold:
                    prev_click_times[i] = current_time
                    led_states[i] = not led_states[i]  # Toggle LED state
                    board.digital[led_pins[i]].write(1 if led_states[i] else 0)  # Write state to LED pin

                    update_checkbox_colors()

            prev_finger_states[i] = finger_in_buttons[i]

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
