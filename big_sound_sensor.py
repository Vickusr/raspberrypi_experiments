import RPi.GPIO as GPIO
import time

SOUND_SENSOR = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(SOUND_SENSOR,GPIO.IN,GPIO.PUD_DOWN)

def DETECT(channel):
    if GPIO.input(channel):
        print('sound - low')
    else:
        print('sound - high')
        
GPIO.add_event_detect(SOUND_SENSOR,GPIO.FALLING,callback = DETECT)
#GPIO.add_event_callback(SOUND_SENSOR, callback)

while True:
    time.sleep(1)

#while True:
    
#    if GPIO.input(SOUND_SENSOR) == GPIO.LOW:
       
#       print('Nothing')
#    else:
#        print(GPIO.input(SOUND_SENSOR))
#        print('sound')