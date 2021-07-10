import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Declare Variable for GPIO Pins
TRIG=23
ECHO=24

#Declare Other Variables
i = 0

#Ask User for Number of Sides Item has
user_input = int(input('Please enter number of sides, needed to be recorded: '))

while i < user_input:
    print ("Measuring....")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print ("Waiting...")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        
        
    pulse_duration=pulse_end - pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print ("DISTANCE :" , distance,"cm" )
    time.sleep(2)  
    i = i + 1
