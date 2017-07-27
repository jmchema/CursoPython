import RPi.GPIO as GPIO
import datetime
import time

CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}
REVERSE_CODE = {v:k for k, v in CODE.items()}


class MorseReader:
    def __init__(self, button_pin):
        self.button_pin = button_pin
        self.received = []
        self.dash_time = 0.2
        self.pause_time = 1
        self.press_start = None
        self.press_released = None
        self.last_symbol = []
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=self.event)
    def event(self, channel):
        if GPIO.input(self.button_pin):
            self.press_released = datetime.datetime.now()
            if self.press_start:
                if (self.press_released - self.press_start).total_seconds() \
                        > self.dash_time:
                    print("-")
                    self.last_symbol.append('-')
                else:
                    print(".")
                    self.last_symbol.append('.')
                self.press_start = None
        else:
            self.press_start = datetime.datetime.now()
            if self.press_released and (
                (self.press_start - self.press_released).total_seconds() \
                        > self.pause_time):
                try:
                    self.received.append(REVERSE_CODE["".join(self.last_symbol)])
                    print(self.received[-1])
                    self.last_symbol = []
                except:
                    if len(self.last_symbol) > 6:
                        print("Wrong symbols, clearing buffer!")
                        self.last_symbol = []

if __name__ == "__main__":
    reader = MorseReader(16)
    time.sleep(60)
    print("".join(reader.received))