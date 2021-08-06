#button switch connect to ground pin and GPIO on the same side
#LED long side connect to the GPIO and the short side connect to ground pin

import subprocess
import datetime
import mysql.connector
import RPi.GPIO as GPIO
import os
from time import sleep #dont have to say time.sleep(x) just to save time don't $
import sys

fetchedDataPHP = sys.argv[1]
fetchedUserId = fetchedDataPHP[0:8]
fetchedLockerId = fetchedDataPHP[-3:]

# fetchedDataPHP = sys.argv[1]
#fetchedUserId = 19012079
#fetchedLockerId = 102

#Connecting to DB
conn = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

cursor = conn.cursor()

#BCM refers to the labelled pin of the T-cobbler connected to Rasp Pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#variable
sleepTime = .1

#GPIO Pin of the component
#GPIO 26 => S-102
#GPIO 19 => S-103
#GPIO 6 => M-105
#GPIO 13 => M-106

smallPin2 = 26
smallPin3 = 19

mediumPin2 = 6
mediumPin3 = 13

buttonPin = 17

# set up the SPI interface pins
GPIO.setup(smallPin2,GPIO.OUT)
GPIO.setup(smallPin3,GPIO.OUT)
GPIO.setup(mediumPin2,GPIO.OUT)
GPIO.setup(mediumPin3,GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)



#Initially input(buttonPin) always True
#LED => ON , buttonswitch => Up (True)
#LED => OFF, buttonswitch => Down (False)

#Select Session table - item-id
#---------------------------------------------
select_session_query = "SELECT item_id FROM Session WHERE user_id = {0} AND status = 'In Progress'"

#sub. into the placeholder after retrieving the input
full_select_session_query = select_session_query.format(fetchedUserId)

#Select Item table - weight
#---------------------------------------------
weight_query = "SELECT weight FROM Item WHERE item_id = ({0})"

#sub. into the placeholder after retrieving the input
full_weight_query = weight_query.format(full_select_session_query)

#run the SQL statement
cursor.execute(full_weight_query)

#Retrieve weight from cursor
for(weight) in cursor:
    retrieved_weight = weight

#Change type tuple => float
w, = retrieved_weight

try:

    while True:
        if w > 0:
            if GPIO.input(buttonPin) == 0:
                #Update locker - item-id , status (hard coded)
                #---------------------------------------------
                update_locker_query = "UPDATE Locker SET item_id = ({0}), status = 'occupied' WHERE locker_id = {1}"
             
                #sub. into the placeholder after retrieving the input
                full_locker_query = update_locker_query.format(full_select_session_query,fetchedLockerId)
       
                #run the SQL statement
                cursor.execute(full_locker_query)
                
                #Create new row for session table (hard coded) (locker_id, date_time,status)
                #---------------------------------------------
                update_session_query = "UPDATE Session SET locker_id = {0}, date_time = '{1}', status = 'Deposited' WHERE user_id = {2} AND status= 'In Progress'"

                #sub. into the placeholder after retrieving the input
                full_session_query = update_session_query.format(fetchedLockerId,datetime.datetime.now(),fetchedUserId)

                #run the SQL statement
                cursor.execute(full_session_query)
                
                if fetchedLockerId == 102:
                    GPIO.output(smallPin2, False)
                if fetchedLockerId == 103:
                    GPIO.output(smallPin3, False)
                if fetchedLockerId == 105:
                    GPIO.output(mediumPin2, False)
                if fetchedLockerId == 106:
                    GPIO.output(mediumPin3, False)
                sleep(.1)
                break

finally:
    #GPIO.output(lightPin, False)
    GPIO.cleanup()

check_query = "SELECT status FROM Session WHERE user_id = {0} AND locker_id = {1}"
full_check_query = check_query.format(fetchedUserId,fetchedLockerId)
cursor.execute(full_check_query)

for (status) in cursor:
    new_status = status

s, = new_status

if s == "Deposited":
    print("Locked")

else:
    print("Unlocked")
    
cursor.close()
conn.commit()
conn.close()
            




