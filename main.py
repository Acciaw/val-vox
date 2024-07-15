import os
import json
import pyaudio
import numpy as np
from pynput.keyboard import Controller, Listener, Key
import time
import sys
from colorama import init, Fore, Style

# Hides the "Hello from the pygame community" message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

#Allows the program to run as an exe with the data passed while compiling
if getattr(sys, 'frozen', False):
    # Running in a PyInstaller bundle
    ASSETS_DIR = os.path.join(sys._MEIPASS, 'assets')
else:
    # Running in a normal Python environment
    ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')

os.system('color')

# Initialize pygame mixer
pygame.mixer.init()
# Load sound files
mute_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'mute.wav'))
unmute_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'unmute.wav'))

# Default settings
default_settings = {
    "keys": {
        "mute": "f8"
    },
    "microphone": None,
    "threshold": 300,
    "silence_duration": 0.5,
    "muted_by_default": False
}

# Check if settings.txt exists, if not create it with default settings
settings_file = 'settings.txt'
if not os.path.exists(settings_file):
    with open(settings_file, 'w') as file:
        json.dump(default_settings, file, indent=4)

# Load settings
with open(settings_file, 'r') as file:
    settings = json.load(file) 

# Function to list available microphones
def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')
    print("Available microphones:")
    time.sleep(0.3)
    for i in range(0, num_devices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        if device_info.get('maxInputChannels') > 0:
            print(f"  [{i}] {device_info.get('name')}")
            time.sleep(0.3)
    p.terminate()
    
print(f"{Fore.MAGENTA}----------[ WELCOME TO VAL-VOX ]----------{Style.RESET_ALL}")
time.sleep(0.3)

# Check if microphone setting is None
if settings["microphone"] is None:
    list_microphones()
    print("Please set the 'microphone' setting in settings.txt and run the program again.")
    time.sleep(0.3)
    print(f"{Fore.MAGENTA}----------[ WELCOME TO VAL-VOX ]----------{Style.RESET_ALL}")
    time.sleep(0.3)
    input(f"{Fore.LIGHTBLACK_EX}Press enter to exit...{Style.RESET_ALL}")
    sys.exit()
    
# Print selected microphone name if available
microphone_index = settings["microphone"]
if microphone_index is not None:
    p = pyaudio.PyAudio()
    device_info = p.get_device_info_by_index(microphone_index)
    print(f"- Selected microphone: {device_info['name']}")
    time.sleep(0.3)
    print(f"- Mute Key: {settings['keys']['mute'].upper()}")
    time.sleep(0.3)
    print(f"- Threshold: {settings['threshold']}")
    time.sleep(0.3)
    print(f"- Silence Duration: {settings['silence_duration']}")
    time.sleep(0.3)
    if settings['muted_by_default']:
        print("- Muted by Default: Yes")
    else:
        print("- Muted by Default: No")
    time.sleep(0.3)
    print(f"{Fore.MAGENTA}----------[ WELCOME TO VAL-VOX ]----------{Style.RESET_ALL}")
    time.sleep(0.3)
    p.terminate()

# Global variables
mute = settings["muted_by_default"]

# Delay for 0.5 second before displaying "Listening..." or "Muted"
time.sleep(0.5)

# Print Muted by default if muted upon starting the program
if mute:
    print(f"{Fore.RED}Muted{Style.RESET_ALL}")
    mute_sound.play()  # Play mute sound
else:
    print(f"{Fore.GREEN}Listening...{Style.RESET_ALL}")
    unmute_sound.play()
last_sound_time = 0
SILENCE_DURATION = settings["silence_duration"]  # Duration in seconds to confirm silence before releasing the key
THRESHOLD = settings["threshold"]  # Use threshold from settings

# Set up audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Get the microphone index from settings
microphone_index = settings["microphone"]

# Open the microphone stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=microphone_index,
                frames_per_buffer=CHUNK)

# Initialize keyboard controller
keyboard = Controller()
key_pressed = False

def detect_sound(data):
    # Convert the byte data to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)
    # Compute the average volume
    volume = np.average(np.abs(audio_data))
    return volume > THRESHOLD

def on_press(key):
    global mute
    mute_key = settings["keys"]["mute"]

    try:
        # Check if the key is a special key
        if hasattr(key, 'char'):
            key_char = key.char
        else:
            key_char = key.name
        
        if key_char == mute_key:
            mute = not mute
            if mute:
                print(f"{Fore.RED}Muted{Style.RESET_ALL}")
                mute_sound.play()  # Play mute sound
            else:
                print(f"{Fore.GREEN}Unmuted{Style.RESET_ALL}")
                unmute_sound.play()  # Play unmute sound
    except AttributeError:
        # Key does not have a 'char' or 'name' attribute (it is a special key)
        pass

# Set up the keyboard listener for mute/unmute functionality
listener = Listener(on_press=on_press)
listener.start()

try:
    while True:
        if not mute:
            # Read data from the microphone
            data = stream.read(CHUNK, exception_on_overflow=False)

            if detect_sound(data):
                last_sound_time = time.time()
                if not key_pressed:
                    print(f"{Fore.LIGHTBLACK_EX}Sound detected, holding key down{Style.RESET_ALL}")
                    keyboard.press(Key.scroll_lock)  # Press and hold the scroll lock key
                    key_pressed = True
            else:
                if key_pressed and time.time() - last_sound_time > SILENCE_DURATION:
                    print(f"{Fore.LIGHTBLACK_EX}No sound detected, releasing key{Style.RESET_ALL}")
                    keyboard.release(Key.scroll_lock)  # Release the scroll lock key
                    key_pressed = False
        else:
            if key_pressed:
                print(f"{Fore.LIGHTBLACK_EX}Muted, releasing key{Style.RESET_ALL}")
                keyboard.release(Key.scroll_lock)
                key_pressed = False

        # Sleep for a short duration to avoid high CPU usage
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up
    stream.stop_stream()
    stream.close()
    p.terminate()
    listener.stop()
    pygame.mixer.quit()