import RPi.GPIO as GPIO
from time import sleep

#Declar mode of calling pin BCM or BOARD
GPIO.setmode(GPIO.BCM)

#Variables 
blinkCount = 3
count = 0
ledPin = 4
buttonPin = 7

#Setup the pin the LED is connected to
GPIO.setup(ledPin, GPIO.OUT)

#Setup the pin the BUTTON is connected to
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

buttonPress = True
ledState = False

try:
    while count < blinkCount:
        print("Please press button")
        buttonPress = GPIO.input(buttonPin)
        if buttonPress == False and ledState == False:
            GPIO.output(ledPin, True)
            print("LED is now turned on")
            ledState = True
            sleep(3)
        elif buttonPress == True and ledState == True:
            GPIO.output(ledPin, False)
            print("LED is now turned off")
            ledState = False
            count += 1
            sleep(0.5)
            sleep(0.1)

finally:
    #Reset the GPIO Pins to a safe state
    GPIO.cleanup()
