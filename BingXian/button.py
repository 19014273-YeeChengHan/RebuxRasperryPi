#button switch connect to ground pin and GPIO on the same side
#LED long side connect to the GPIO and the short side connect to ground pin

import mysql.connector
import RPi.GPIO as GPIO
import os
from time import sleep #dont have to say time.sleep(x) just to save time don't need to type out

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

#variable
sleepTime = .1

#GPIO Pin of the component. Can be changed as desired.
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
GPIO.output(smallPin2, False)
GPIO.output(smallPin3, False)
GPIO.output(mediumPin2, False)
GPIO.output(mediumPin3, False)

#input for updating Locker table
itemid = input("Please enter the item id: ")
lockerid = input("Please enter the locker id: ")

#input for inserting Session table
userid = input("Please enter the user id: ")

list = [smallPin2,smallPin3,mediumPin2,mediumPin3]

for i in list:
    if GPIO.outputlist[i](-----------------------------------------------------------------------------------------)
                   
try:
   while True:
       GPIO.output(lightPin, GPIO.input(buttonPin))
       
       #Update locker - item-id , status (hard coded)
       #---------------------------------------------
       locker_query = "UPDATE Locker SET item_id = {0}, status = 'occupied' WHERE locker_id = {1}"
       
       #sub. into the placeholder after retrieving the input
       full_locker_query = query.format(itemid,lockerid)
       
       #run the SQL statement
       cursor.execute(full_locker_query)	

       #Update pin session - status (dynamic)
       #---------------------------------------------
       select_pinsession_query = "SELECT pinsession_id FROM `Pin Session` ORDER BY pinsession_id DESC LIMIT 1"
       update_pinsession_query = "UPDATE `Pin Session` SET status = 'Deposited' WHERE pinsession_id = {0}"
       
       #run the SQL statement
       cursor.execute(select_pinsession_query)

       #Find the highest pinsession_id and add one 
       for(pinsession_id) in cursor:
           newest_pinsession_id = pinsession_id + 1
       
       #sub. into the placeholder after retrieving the input
       full_pinsession_query = update_pinsession_query.format(newest_pinsession_id)
       
       #run the SQL statement
       cursor.execute(full_pinsession_query)

       #Create new row for session table (hard coded)
       #---------------------------------------------
       select_session_query = "SELECT session_id FROM Session ORDER BY session_id DESC LIMIT 1"
       insert_session_query = "INSERT INTO Session (session_id, user_id, locker_id, item_id, type, date_time)
       VALUES ({0}, {1}, {2}, {3}, 'Finder',(SELECT use_date_time FROM `Pin Session` ORDER BY use_date_time DESC LIMIT 1))"
       
       #run the SQL statement
       cursor.execute(select_session_query)
    
       #Find the highest session_id and add one
       for(session_id) in cursor:
           newest_session_id = session_id + 1
       
       #sub. into the placeholder after retrieving the input
       full_session_query = insert_session_query.format(newest_session_id,userid,lockerid,itemid)
       
       #run the SQL statement
       cursor.execute(full_session_query)
       
       cursor.close()
       conn.commit()
       conn.close()

       sleep(.1)
       
finally:
    GPIO.output(lightPin, False)
    GPIO.cleanup()

'''
=======================================================================================
--------------------------------
Update locker - item-id , status (hard coded)
--------------------------------
itemid = input("Please enter the item id: ")
lockerid = input("Please enter the locker id: ")
UPDATE Locker SET item_id = itemid, status = 'occupied' WHERE locker_id = lockerid

--------------------------------
Update pin session - status (dynamic)
--------------------------------
SELECT pinsession_id FROM `Pin Session` ORDER BY pinsession_id DESC LIMIT 1
for(pinsession_id) in cursor:
    newest_pinsession_id = pinsession_id + 1

UPDATE `Pin Session` SET status = 'Deposited' WHERE pinsession_id = newest_pinsession_id

--------------------------------
Create new row for session table (hard coded)
--------------------------------
SELECT session_id FROM Session ORDER BY session_id DESC LIMIT 1
for(session_id) in cursor:
    newest_session_id = session_id + 1

userid = input("Please enter the user id: ")
INSERT INTO Session (session_id, user_id, locker_id, item_id, type, date_time)
VALUES (newest_session_id, userid, lockerid, itemid, 'Finder',(SELECT use_date_time FROM `Pin Session` ORDER BY use_date_time DESC LIMIT 1))
========================================================================================
'''

