from time import sleep
import RPi.GPIO as GPIO

number_map = {
    "0": [1, 1, 1, 1, 1, 1, 0],
    "1": [0, 1, 1, 0, 0, 0, 0],
    "2": [1, 1, 0, 1, 1, 0, 1],
    "3": [1, 1, 1, 1, 0, 0, 1],
    "4": [0, 1, 1, 0, 0, 1, 1],
    "5": [1, 0, 1, 1, 0, 1, 1],
    "6": [1, 0, 1, 1, 1, 1, 1],
    "7": [1, 1, 1, 0, 0, 0, 0],
    "8": [1, 1, 1, 1, 1, 1, 1],
    "9": [1, 1, 1, 1, 0, 1, 1],
    "A": [1, 1, 1, 0, 1, 1, 1],
    "b": [0, 0, 1, 1, 1, 1, 1],
    "c": [1, 0, 0, 1, 1, 1, 0],
    "d": [0, 1, 1, 1, 1, 0, 1],
    "E": [1, 0, 0, 1, 1, 1, 1],
    "F": [1, 0, 0, 0, 1, 1, 1],   
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pin_list = [17, 27, 22, 5, 6, 13, 19, 26]

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, 1)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, 1)

GPIO.setup(5, GPIO.OUT)
GPIO.output(5, 1)

GPIO.setup(6, GPIO.OUT)
GPIO.output(6, 1)

GPIO.setup(13, GPIO.OUT)
GPIO.output(13, 1)

GPIO.setup(19, GPIO.OUT)
GPIO.output(19, 1)
    
while True:
    for number in number_map.keys():
        print("Key:", number)
        for i, high in enumerate(number_map[number]):
            print(number)
            GPIO.output(pin_list[i], not high)
        sleep(1)
