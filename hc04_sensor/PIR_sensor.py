import RPi.GPIO as GPIO
import time

sensor = 38
buzzer = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("Initialzing PIR Sensor......")
time.sleep(1)
print ("PIR Ready...")


try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print ("Motion Detected")
          time.sleep(3)
          GPIO.output(buzzer,False)
          while GPIO.input(sensor):
              time.sleep(1)
      else:
          GPIO.output(buzzer,False)


except KeyboardInterrupt:
    GPIO.cleanup()
