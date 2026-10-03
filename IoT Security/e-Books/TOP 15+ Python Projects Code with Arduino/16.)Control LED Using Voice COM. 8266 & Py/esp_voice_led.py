import speech_recognition as sr
import pyttsx3
import urllib.request

# ESP8266 Web Server IP Address (Replace with your ESP's IP)
ESP8266_IP = "http://192.168.0.104"  # Replace with your actual IP address

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_voice():
    with sr.Microphone() as source:
        print("Listening for commands...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Could not request results from Google Speech Recognition service.")
        return ""

def control_led(command):
    if "on" in command:
        speak("Turning LED on")
        urllib.request.urlopen(f"{ESP8266_IP}/on")
    elif "off" in command:
        speak("Turning LED off")
        urllib.request.urlopen(f"{ESP8266_IP}/off")
    else:
        speak("Command not recognized")

# Main loop
while True:
    command = recognize_voice()
    control_led(command)
