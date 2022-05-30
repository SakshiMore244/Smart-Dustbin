import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
pinTrigger = 7
pinEcho = 11
pinLed = 5
#pulseStartTime = 5
#pulseEndTime = 5
while True:    
    distance = 0
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinLed, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)
    GPIO.output(pinTrigger, GPIO.LOW)
    GPIO.output(pinTrigger, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, GPIO.LOW)
    while GPIO.input(pinEcho)==0:
        pulseStartTime = time.time()
    while GPIO.input(pinEcho)==1:
        pulseEndTime = time.time()
    pulseDuration = pulseEndTime - pulseStartTime
    distance = round(pulseDuration * 17150, 2)
    print("Distance: %.2f cm" % (distance))
    if distance>=15:
        GPIO.output(pinLed, GPIO.HIGH)
        
    else:
        GPIO.output(pinLed, GPIO.LOW)
    
    


   