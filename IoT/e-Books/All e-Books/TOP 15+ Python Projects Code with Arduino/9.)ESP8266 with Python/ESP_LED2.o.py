import urllib.request

ESP_IP = '192.168.0.106'  # Change this to the IP of your ESP8266

def send_command(command):
    url = f'http://{ESP_IP}/{command}'
    urllib.request.urlopen(url)

while True:
    command = input("Enter 'on' to turn the LED on or 'off' to turn it off: ")
    if command == 'on':
        send_command('led/on')
    elif command == 'off':
        send_command('led/off')
    else:
        print("Invalid command. Please enter 'on' or 'off'.")
