import RPi.GPIO as GPIO
import time

sensor = 4  #IR Sensor connected to GPIO4
buzzer = 21 #Positive terminal of buzzer connected to GPIO21 connect to GPIO Board

GPIO.setmode(GPIO.BCM) #BCM Refers to the labelled pins OF THE T-cobbler connected to Rasp Pi
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,True)
print ("IR Sensor Ready.....")
print (" ")

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,False)
          GPIO.output(buzzer,GPIO.LOW)
          print ("Object Detected")
          while GPIO.input(sensor):
              time.sleep(0.5)
      else:
          GPIO.output(buzzer,True)


except KeyboardInterrupt:
    GPIO.cleanup()