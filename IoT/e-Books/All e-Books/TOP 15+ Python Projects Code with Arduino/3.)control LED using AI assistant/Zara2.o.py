import speech_recognition as sr
from pyfirmata import Arduino, util
import time
import pyttsx3

# Initialize pyttsx3
engine = pyttsx3.init()

# Adjust the speech rate (higher values make it faster)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 50)  # Increase by 50, adjust as needed

# Set up Arduino board
board = Arduino('COM12')  # Replace with your port
red_led_pin = 13
green_led_pin = 12
blue_led_pin = 11

recognizer = sr.Recognizer()

# Function to provide auditory feedback
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Wish me function in Hindi
def wishme():
    speak("नमस्ते, मिस्टर स्टार्क। सभी सिस्टम काम कर रहे हैं। मैं आपकी कैसे मदद कर सकता हूँ?")

# Function to toggle LED state
def toggle_led(led_pin, state):
    board.digital[led_pin].write(state)

# Function to listen for voice commands in Hindi
def listen_for_command():
    with sr.Microphone() as source:
        print("आदेश सुन रहा हूँ...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='hi-IN').lower()
        print("आदेश:", command)
        return command
    except sr.UnknownValueError:
        print("माफ़ कीजिये, मैं इसे समझ नहीं पाया।")
        speak("माफ़ कीजिये, मैं इसे समझ नहीं पाया।")
        return None
    except sr.RequestError as e:
        print("परिणाम अनुरोध नहीं कर सका; {0}".format(e))
        speak("परिणाम अनुरोध नहीं कर सका।")
        return None

if __name__ == "__main__":
    wishme()
    while True:
        command = listen_for_command()

        if command:
            if "लाल लाइट चालू" in command:
                toggle_led(red_led_pin, 1)
                speak("लाल एलईडी चालू हो गई है।")
            elif "लाल लाइट बंद" in command:
                toggle_led(red_led_pin, 0)
                speak("लाल एलईडी बंद हो गई है।")
            elif "हरी लाइट चालू" in command:
                toggle_led(green_led_pin, 1)
                speak("हरी एलईडी चालू हो गई है।")
            elif "हरी लाइट बंद" in command:
                toggle_led(green_led_pin, 0)
                speak("हरी एलईडी बंद हो गई है।")
            elif "नीली लाइट चालू" in command:
                toggle_led(blue_led_pin, 1)
                speak("नीली एलईडी चालू हो गई है।")
            elif "नीली लाइट बंद" in command:
                toggle_led(blue_led_pin, 0)
                speak("नीली एलईडी बंद हो गई है।")
            elif "बाहर निकलें" in command:
                speak("कार्यक्रम से बाहर निकल रहा हूँ, आपका दिन शुभ हो")
                break
            else:
                speak("आदेश मान्यता प्राप्त नहीं हुआ।")
