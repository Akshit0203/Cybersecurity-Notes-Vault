import pyfirmata
import time

# Specify the port to which your Arduino is connected
board = pyfirmata.Arduino('COM12')

# Define the pin where the LED is connected
led_pin = 13

# Set up the pin as an OUTPUT
board.digital[led_pin].mode = pyfirmata.OUTPUT

def led_on():
    board.digital[led_pin].write(1)

def led_off():
    board.digital[led_pin].write(0)

def main():
    while True:
        command = input("Enter: ").strip().lower()
        if command == 'on':
            led_on()
        elif command == 'off':
            led_off()
        elif command == 'exit':
            break
        else:
            print("Invalid command. Please enter 'on', 'off', or 'exit'.")

    # Clean up and close the connection
    board.exit()

if __name__ == '__main__':
    main()
