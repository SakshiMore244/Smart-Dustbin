import urllib3
from firebase import firebase
#import pyrebase
import time
#import board
import json  
import os   
from functools import partial

firebase = firebase.FirebaseApplication('https://clean-india-5ff98-default-rtdb.firebaseio.com/', None)

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 7
GPIO_ECHO = 11
#pinLed = 5

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
#GPIO.setup(pinLed, GPIO.OUT)

def update_firebase():
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
    
    data = {"Distance":distance}
    firebase.post(data)
    
while True:  
        update_firebase()  
          
        #sleepTime = int(sleepTime)  
        sleep(5)  
    
    
