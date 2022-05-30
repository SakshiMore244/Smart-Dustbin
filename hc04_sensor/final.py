import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 7
GPIO_ECHO = 11
pinLed = 5
channel = 40

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(channel, GPIO.IN)

def distance():
    GPIO.setup(GPIO_TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.setup(GPIO_TRIGGER, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO)==0:
        StartTime = time.time()
    
    while GPIO.input(GPIO_ECHO)==1:
        StopTime = time.time()
    
    TimeElasped = StopTime-StartTime
    distance = (TimeElasped*34300)/2
    return distance

if __name__ == '__main__':
    try:
        
        dist = distance()
        if dist<=15:
            GPIO.output(pinLed, GPIO.HIGH)
        else:
            GPIO.output(pinLed, GPIO.LOW)
        print("Measured Distance = %.1fcm"%dist)
        time.sleep(1)
            
        while True:
            if GPIO.input(channel):
                print ("water not detected!")
                print("1")
            else:
                print ("Water detected!")
                print("0")
            
            
    except KeyboardInterrupt:
            print("Measurement stopped by User")
            GPIO.cleanup()
                






