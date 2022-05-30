import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pinLed = 5
GPIO.setup(pinLed, GPIO.OUT)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=40)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        if result.humidity >= 30:
            GPIO.output(pinLed, GPIO.HIGH)
            
        else:
            GPIO.output(pinLed, GPIO.LOW)
        time.sleep(1)

