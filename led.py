import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
LED = 7

GPIO.setup(LED,GPIO.OUT)

def turn_on():
    GPIO.output(LED,GPIO.HIGH)

def turn_off():
    GPIO.output(LED,GPIO.LOW)

for i in range(3):
    
    turn_on()
    sleep(1)
    turn_off()
    sleep(1)


GPIO.cleanup()