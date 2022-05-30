import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

sensor = 38
buzzer = 5


GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("IR Sensor Ready.....")
print (" ")

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,False)
          print ("Object Not detected")
          time.sleep(1)
          GPIO.output(buzzer,False)
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          print ("Object Detected")
          GPIO.output(buzzer,True)

except KeyboardInterrupt:
    GPIO.cleanup()