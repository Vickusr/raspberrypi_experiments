import RPi.GPIO as GPIO
import time
from statistics import median, mean

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print('in progress')

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


GPIO.output(TRIG, False)

time.sleep(2)

measurements =[]

for i in range(10):

    GPIO.output(TRIG,True)

    time.sleep(0.5)

    GPIO.output(TRIG,False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance,2)
    measurements.append(distance)
    print("Distance: ", distance," cm")

print("Best Measurement: ", round(median(measurements),2), " cm")
print("Best Measurement: ", round(mean(measurements),2)," cm")
GPIO.cleanup()
