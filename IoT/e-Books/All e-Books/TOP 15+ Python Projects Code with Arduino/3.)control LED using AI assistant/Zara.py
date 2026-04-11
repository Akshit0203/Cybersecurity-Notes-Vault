import speech_recognition as sr
from pyfirmata import Arduino, util
import time
from gtts import gTTS
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Set up Arduino board
board = Arduino('COM5')  # Replace with your port
red_led_pin = 13
green_led_pin = 12
blue_led_pin = 11

recognizer = sr.Recognizer()

# Function to provide auditory feedback in Hindi
def speak(message):
    tts = gTTS(text=message, lang='hi')
    audio_file = "response.mp3"
    tts.save(audio_file)
    
    # Play the audio file using pygame
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    
    # Ensure the mixer is stopped and the file is released
    pygame.mixer.music.unload()
    os.remove(audio_file)

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
        #speak("माफ़ कीजिये, मैं इसे समझ नहीं पाया।")
        return None
    except sr.RequestError as e:
        print("परिणाम अनुरोध नहीं कर सका; {0}".format(e))
        #speak("परिणाम अनुरोध नहीं कर सका।")
        return None

if __name__ == "__main__":
    wishme()
    while True:
        command = listen_for_command()

        if command:
            if "लाइट ऑन करो" in command:
                toggle_led(red_led_pin, 1)
                speak("बॉस लाइट चालू हो गई")
            elif "लाइट ऑफ करो" in command:
                speak("हाँ बॉस आपकी पसंद के अनुसार मैं लाइट बंद कर देता हूँ")
                toggle_led(red_led_pin, 0)
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
            elif "अपने आप को बंद करो" in command:
                speak("कार्यक्रम से बाहर निकल रहा हूँ, आपका दिन शुभ हो")
                break
            elif "गाना" in command:
                music_dir = "C:\\Users\\SUBRATA SASMAL\\Music"
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("आदेश मान्यता प्राप्त नहीं हुआ।")
