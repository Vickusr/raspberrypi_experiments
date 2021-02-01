import RPi.GPIO as GPIO
import time

RelayPin = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.LOW)


for i in range(5):
    GPIO.output(RelayPin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(RelayPin, GPIO.LOW)
    time.sleep(0.1)
    
GPIO.cleanup()