#ultrasonic sensor with thingspeak and distance alarm 

import RPi.GPIO as GPIO
import urllib3
import time

# Enter Your API key here
myAPI = 'IUQ1NDVXIVA6ENZY'
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 7
GPIO_ECHO = 11
pinLed = 5
channel = 40
servoPIN = 36

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(channel, GPIO.IN)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

def distance():
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

if __name__ == '__main__':
    try:
        
            
        while True:
            dist = distance()
            http = urllib3.PoolManager()
            response = http.request('GET', baseURL + '&field1=%f' % (dist))
            if dist<=15:
                GPIO.output(pinLed, GPIO.HIGH)
        
            else:
                GPIO.output(pinLed, GPIO.LOW)
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            
            if GPIO.input(channel):
                print ("water not detected!")
                p.ChangeDutyCycle(7.5)
                time.sleep(0.5)
                p.ChangeDutyCycle(2)
                time.sleep(0.5)
                p.ChangeDutyCycle(7.5)
                time.sleep(0.5)
            else:
                print ("Water detected!")
                
            
                p.ChangeDutyCycle(7.5)
                time.sleep(0.5)
                p.ChangeDutyCycle(12.5)
                time.sleep(0.5)
                p.ChangeDutyCycle(7.5)
                time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()        
