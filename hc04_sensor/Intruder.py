import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 7
GPIO_ECHO = 11
pinBuz = 5
pinLed = 13

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(pinBuz, GPIO.OUT)
GPIO.setup(pinLed, GPIO.OUT)

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
            
            if dist>=15:
                GPIO.output(pinBuz, GPIO.LOW)
                GPIO.output(pinLed, GPIO.LOW)
                half_email_sent = 0
                eighty_email_sent = 0
                
            if dist<=15 and dist>=10 and half_email_sent != 1:
                
                x = input("ALERT GIVE PASSWORD!! = ")
                if x == "Rpi":
                    print("Correct")
                else:
                    print("ALERT WRONG PASS")
                    time.sleep(1)
                    GPIO.output(pinBuz, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.LOW)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinBuz, GPIO.LOW)
                #send_email()
                half_email_sent = 1
                
                
            if dist<=10 and dist>=2 and eighty_email_sent != 1:
                GPIO.output(pinLed, GPIO.HIGH)
                GPIO.output(pinBuz, GPIO.LOW)
                eighty_email_sent = 1
                
            if dist<=2 and dist>=0:
                GPIO.output(pinBuz, GPIO.HIGH)
                GPIO.output(pinLed, GPIO.HIGH)
                
        
            else:
                GPIO.output(pinLed, GPIO.LOW)
            
            print ("Person Distance = %.1f cm" % dist)
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
