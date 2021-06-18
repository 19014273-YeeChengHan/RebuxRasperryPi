#!/usr/bin/env python

import mysql.connector
import time
import os
import RPi.GPIO as GPIO

#Connecting to DB
conn = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

cursor = conn.cursor()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #BCM refers to the labelled pin of the T-cobbler connected to Rasp Pi
DEBUG = 1

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)
    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)
    
    adcout >>= 1       # first bit is 'null' so drop it
    return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# 10k trim pot connected to adc #0
potentiometer_adc = 0;

last_read = 0       # this keeps track of the last potentiometer value
tolerance = 5       # to keep from being jittery we'll only change
                    # volume when the pot has moved more than 5 'counts'

forcelist = []
second = int(input("Enter the time in seconds: "))

while second > 0:
    # we'll assume that the pot didn't move
    trim_pot_changed = False

    # read the analog pin
    trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
    # how much has it changed since the last read?
    pot_adjust = abs(trim_pot - last_read)

    if DEBUG:
        print ("\nForce:", trim_pot)
        print ("Force Changed:", pot_adjust)
        print ("Last Force Read: ", last_read)

    if ( pot_adjust > tolerance ):
        trim_pot_changed = True

   #if DEBUG:
          #print ("Force Changed"), trim_pot_changed

    if ( trim_pot_changed ):
        set_volume = trim_pot / 10.24           # convert 10bit adc0 (0-1024) trim pot read into 0-100 volume level
        set_volume = round(set_volume)          # round out decimal value
        set_volume = int(set_volume)            # cast volume as integer


        set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = set_volume)
        os.system(set_vol_cmd)  # set volume


        # save the potentiometer reading for the next loop
        last_read = trim_pot
        
        #Add the force inside the list
        forcelist.append(trim_pot)
        
    f = int(0) #setting initial force
#Doing a loop to check and find the highest force
    for i in range(len(forcelist)):
        if forcelist[i] > f:
            f= forcelist[i]

    # time function here
    mins = second // 60
    secs = second % 60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print("Time: " + timer + "\n")
    time.sleep(1)
    second -= 1

itemId = input("Please enter the item id: ")

query = "UPDATE Item SET weight = {0} WHERE item_id = {1};"
full_query = query.format(f,itemId) 

cursor.execute(full_query)

cursor.close()
conn.commit()
conn.close()