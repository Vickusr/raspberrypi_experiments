import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT


#GPIO.setmode(GPIO.BOARD)
#HT_sensor = 27

hum, temp = Adafruit_DHT.read_retry(11,4)