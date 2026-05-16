from pyfirmata import Arduino, util
import keyboard
import time
import pyfirmata

arduino_port = 'COM5'

board = Arduino(arduino_port)

led_pin = 8

board.digital[led_pin].mode = pyfirmata.OUTPUT

led_state = 0

def toggle_led():
    global led_state
    if led_state == 0:
        board.digital[led_pin].write(1)
        led_state = 1
        print("LED turned ON")
    else:
        board.digital[led_pin].write(0)
        led_state = 0
        print("LED turned OFF")

try:
    while True:
        if keyboard.is_pressed('t'):
            toggle_led()
            time.sleep(0.5)

except KeyboardInterrupt:
    board.exit()
