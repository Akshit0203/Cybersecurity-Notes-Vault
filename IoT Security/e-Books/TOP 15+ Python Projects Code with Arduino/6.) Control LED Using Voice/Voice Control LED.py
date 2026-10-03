import speech_recognition as sr
from pyfirmata import Arduino, util
import time
import pyttsx3

# Set up Arduino board
board = Arduino('COM12')  # Replace with your port
red_led_pin = 13
green_led_pin = 12
blue_led_pin = 11

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to provide auditory feedback
def speak(message):
    engine.say(message)
    engine.runAndWait()

#wish me function
def wishme():
    speak("Hello, Mr Stark. All systems are operational. How can I assist you?")

# Function to toggle LED state
def toggle_led(led_pin, state):
    board.digital[led_pin].write(state)

# Function to listen for voice commands
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        speak("Could not request results.")
        return None

if __name__ == "__main__":
  wishme()
  while True:
    command = listen_for_command()

    if command:
        if "red light on" in command:
            toggle_led(red_led_pin, 1)
            speak("Red LED turned on.")
        elif "red light off" in command:
            toggle_led(red_led_pin, 0)
            speak("Red LED turned off.")
        elif "green light on" in command:
            toggle_led(green_led_pin, 1)
            speak("Green LED turned on.")
        elif "green light off" in command:
            toggle_led(green_led_pin, 0)
            speak("Green LED turned off.")
        elif "blue light on" in command:
            toggle_led(blue_led_pin, 1)
            speak("Blue LED turned on.")
        elif "blue light off" in command:
            toggle_led(blue_led_pin, 0)
            speak("Blue LED turned off.")
        elif "exit" in command:
            speak("Exiting program, have a good day sir")
            break
        else:
            speak("Command not recognized.")
