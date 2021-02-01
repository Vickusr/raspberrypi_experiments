import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
LED = 7

GPIO.setup(LED,GPIO.OUT)

def turn_on():
    GPIO.output(LED,GPIO.HIGH)

def turn_off():
    GPIO.output(LED,GPIO.LOW)


print('on')
turn_on()
sleep(25)
print('5 left')
sleep(5)

GPIO.cleanup()
