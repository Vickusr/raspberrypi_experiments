import time
import Adafruit_DHT as A

DHT_SENSOR = A.DHT11
DHT_PIN = 4

while True:
    h, t = A.read(DHT_SENSOR,DHT_PIN)
    if h is not None and t is not None:
        print(h)
        print(t)
    else:
        print('Wiring Issue')
    time.sleep(1)

    
