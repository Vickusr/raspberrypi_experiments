import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
LED = 7

GPIO.setup(LED,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def turn_on():
    GPIO.output(LED,GPIO.HIGH)

def turn_off():
    GPIO.output(LED,GPIO.LOW)

while True:
    if GPIO.input(LED) == GPIO.HIGH:
        print('push')
    else:
        print('not pushed')




#GPIO.cleanup()
