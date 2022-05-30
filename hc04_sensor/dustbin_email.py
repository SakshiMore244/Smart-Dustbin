import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 7
GPIO_ECHO = 11
pinBuz = 5
pinLed = 13

half_email_sent = 0
eighty_email_sent = 0

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(pinBuz, GPIO.OUT)
GPIO.setup(pinLed, GPIO.OUT)

def send_email():
    if half_email_sent == 0:
        me = "raspi.iot33@gmail.com"
        my_password = r"raspberryPi33"
        you = "bigchungussobig@gmail.com"
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Hello"
        msg['From'] = me
        msg['To'] = you

        html = '<html><body><p>Hello. Dustbin half full.</p></body></html>'
        part2 = MIMEText(html, 'html')
        
        msg.attach(part2)

        # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
        s = smtplib.SMTP_SSL('smtp.gmail.com')
    # uncomment if interested in the actual smtp conversation
    # s.set_debuglevel(1)
    # do the smtp auth; sends ehlo if it hasn't been sent already
        s.login(me, my_password)

        s.sendmail(me, you, msg.as_string())
        s.quit()
        print("Email sent")
    else:
        print("Email sent")
        
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
                
                print("ALERT GARBAGE HALF FULL!!")
                print ("Garbage Distance = %.1f cm" % dist)
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
            
            print ("Garbage Distance = %.1f cm" % dist)
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()