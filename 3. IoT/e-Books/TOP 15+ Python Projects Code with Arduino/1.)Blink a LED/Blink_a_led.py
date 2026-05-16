import time
from pyfirmata import Arduino, util, OUTPUT

# Specify the port where the Arduino is connected (adjust accordingly)
board = Arduino('/dev/ttyACM0')  # For Windows, it might be 'COM3', 'COM4', etc.

# Define the pin where the LED is connected
led_pin = 13

# Start an iterator thread to read analog inputs
it = util.Iterator(board)
it.start()

# Setup the LED pin as OUTPUT
board.digital[led_pin].mode = OUTPUT

# Blink the LED
while True:
    board.digital[led_pin].write(1)  # Turn LED on
    time.sleep(1)                    # Wait for 1 second
    board.digital[led_pin].write(0)  # Turn LED off
    time.sleep(1)                    # Wait for 1 second
