import RPi.GPIO as GPIO
from time import sleep 
import time

# Start of Keen's Set-up for Infrared Sensor
sensor = 4
i = 0
#End of Keen's Set-up for Infrared Sensor

GPIO.setmode(GPIO.BCM) 
GPIO.setup(sensor,GPIO.IN)
GPIO.setwarnings(False)

#Start of Keen's IR Sensor Codes
while True:
    
    if (GPIO.input(sensor) == 1):
        
        if (i == 1):
            print("An item has been detected in the locker");
            detect = True
            break;
        i = 1

        #These 2 lines prevent the program from running continuously 
        while GPIO.input(sensor):
            print("Detecting for item...")
            time.sleep(0.5)
            
