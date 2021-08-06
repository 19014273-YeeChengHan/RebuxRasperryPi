#Official File of Bing Xian and Keen LED Light, Closing Mechanism of Locker and IR Sensor Integration
#DO NOT TOUCH

#Button switch connect to ground pin and GPIO on the same side
#LED long side connect to the GPIO and the short side connect to ground pin
import datetime
import mysql.connector
import RPi.GPIO as GPIO
import os
from time import sleep #dont have to say time.sleep(x) just to save time don't need to type out
import time

#Start of Keen's Imported Libraries
import smtplib
from email.message import EmailMessage
import mysql.connector
#End of Keen's Imported Libraries

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

# Start of Keen's Set-up for Infrared Sensor
sensor = 4
i = 0
#End of Keen's Set-up for Infrared Sensor

# set up the SPI interface pins
GPIO.setup(smallPin2,GPIO.OUT)
GPIO.setup(smallPin3,GPIO.OUT)
GPIO.setup(mediumPin2,GPIO.OUT)
GPIO.setup(mediumPin3,GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)



GPIO.setmode(GPIO.BCM) 
GPIO.setup(sensor,GPIO.IN)
GPIO.setwarnings(False)
def menu():
    print("=================LOCKER MENU=================")
    print("1. Small Locker")
    print("2. Medium Locker")
    locker = int(input("Please enter the size of the locker: "))

    if locker == 1:
        print("1. S-102")
        print("2. S-103")
        small_locker = int(input("Please enter the small locker that you used: "))
        if small_locker == 1:
            return smallPin2
        elif small_locker == 2:
            return smallPin3
        else:
            print("incorrect input, please enter again!")

    elif locker == 2:
        print("1. M-105")
        print("2. M-106")
        medium_locker = int(input("Please enter the medium locker that you used: "))
        if medium_locker == 1:
            return mediumPin2
        elif medium_locker == 2:
            return mediumPin3
        else:
            print("incorrect input, please enter again!")
    else:
        print("incorrect input, please enter again!")

x = menu()

#input for updating Locker table
lockerid = input("Please enter the locker id: ") #(ming hao pass data to me)

#input for inserting Session table 
userid = input("Please enter the user id: ")    #(ming hao pass data to me)

#Initially input(buttonPin) always True
#LED => ON , buttonswitch => Up (True)
#LED => OFF, buttonswitch => Down (False)

#Select Session table - item-id
#---------------------------------------------
select_session_query = "SELECT item_id FROM Session WHERE user_id = {0} AND status = 'In Progress'"

#sub. into the placeholder after retrieving the input
full_select_session_query = select_session_query.format(userid)

#Select Item table - weight
#---------------------------------------------
weight_query = "SELECT * FROM Item WHERE item_id = ({0})"
    
#sub. into the placeholder after retrieving the input
full_weight_query = weight_query.format(full_select_session_query)

#run the SQL statement
cursor.execute(full_weight_query)

#Retrieve weight from cursor
for(item_id, category_id, description, dimension, weight) in cursor:
    retrieve_weight = weight

#Change type tuple => float
#w, = retrieve_weight

detect = False
try:
    #Start of Keen's IR Sensor Codes
    while True:
        
        if (GPIO.input(sensor) == 1):
            #print("Item detected in locker")
            
            if (i == 1):
                print("An item has been detected in the locker");
                detect = True
                break;
            i = 1

            #These 2 lines prevent the program from running continuously 
            while GPIO.input(sensor):
                print("Detecting for item...")
                time.sleep(0.5)
                
    #End of Keen's IR Sensor Codes
    while True:
        if detect == True:
            if retrieve_weight > 0:
                if GPIO.input(buttonPin) == 0:
                    #Update locker - item-id , status (hard coded)
                    #---------------------------------------------
                    update_locker_query = "UPDATE Locker SET item_id = ({0}), status = 'occupied' WHERE locker_id = {1}"
       
                    #sub. into the placeholder after retrieving the input
                    full_locker_query = update_locker_query.format(full_select_session_query,lockerid)

                    #run the SQL statement
                    cursor.execute(full_locker_query)


                    #Create new row for session table (hard coded) (locker_id, date_time, status)
                    #---------------------------------------------
                    update_session_query = "UPDATE Session SET locker_id = {0}, date_time = '{1}', status = 'Deposited' WHERE user_id = {2} AND status = 'In Progress'"

                    #sub. into the placeholder after retrieving the input
                    full_session_query = update_session_query.format(lockerid,datetime.datetime.now(),userid)

                    #run the SQL statement
                    cursor.execute(full_session_query)

                    
                    #Start of Keen's Codes
                    
                    #Start of Keen's SQL Queries

                    sql_select_sessionid = "SELECT * FROM Session"
                    cursor = conn.cursor()
                    cursor.execute(sql_select_sessionid)

                    for(session_id, user_id, locker_id, item_id,pinsession_id ,type, date_time,status) in cursor:
                        
                        #Get locker_id
                        retreived_lockerid = str(locker_id)
                        
                        #Get user_id 
                        retreived_userid = str(user_id)
                        
                        #Get the last row of session_id
                        retreived_id = str(session_id)
                        
                        #Get the datetime when item door successfully closes
                        retreived_datetime = str(date_time)
                        
                        #Get item_id
                        retreived_itemid = str(item_id)

                    #Keen's SQL to get the users name to be placed in the email
                    sql_select_userID= "SELECT * FROM Session"
                    cursor.execute(sql_select_userID)
                    for(session_id, user_id, locker_id, item_id,pinsession_id ,type, date_time,status) in cursor:
                        getUserID = user_id
                        getItemID = item_id
                    sql_select_userName= "SELECT name FROM Users WHERE user_id = {0}"
                    sql_get_name = sql_select_userName.format(getUserID)
                    cursor.execute(sql_get_name)
                    for (name) in cursor:
                        name = name
                        
                    #Keen's code to remove bracket and comma when retreiving name from Session table
                    username, = name

                    #Keen's SQL to get category ID from Item table
                    
                    sql_select_catdesc= "SELECT category_id, description FROM Item WHERE item_id = {0}"
                    sql_get_catdesc = sql_select_catdesc.format(getItemID)
                    cursor.execute(sql_get_catdesc)
                    
                    for(category_id,description) in cursor:
                        getcatID = category_id
                        getdesc = str(description)
                        
                    sql_category_name= "SELECT name FROM Category WHERE category_id = {0}"
                    sql_get_catName = sql_category_name.format(getcatID)
                    cursor.execute(sql_get_catName)
                    for (catname) in cursor:
                        catname = catname

                    categoryname, = catname
                    
                    #End of Keen's SQL Queries
                    
                    #Start of Keen's Email Function
                    def send_email_acknowledgement(name,lockerid, datetime,category,desc):
                        
                        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        server.login("rebuxrepublicpolytechnic@gmail.com", "rebuxpassword")
                        message = """Subject: Rebux Deposit Confirmation\n
                        Dear {0},\n
                        You have successfully deposited a lost item with the following details below: \n
                        Locker Used: {1}
                        Date and Time Deposited: {2}
                        Category of deposited item: {3}
                        Item description: {4}
                        Thank you for using Rebux Locker System.\n
                        Rebux
                        Republic Polytechnic
                        """
                        server.sendmail("rebuxrepublicpolytechnic@gmail.com", "keenlovinorebux@gmail.com",
                                        message.format(username,retreived_lockerid,retreived_datetime, categoryname, getdesc))
                        server.quit()
                        print("Email Sent!")
                        
                    send_email_acknowledgement(username,retreived_lockerid, retreived_datetime,categoryname, getdesc)
                    
                    #End of Keen's Send Email Function
                    #End of Keen's Codes
                    
                    GPIO.output(x, False) 
                    sleep(.1)
                    break
           
finally:
    #GPIO.output(lightPin, False)
    GPIO.cleanup()

check_query = "SELECT status FROM Session WHERE user_id = {0} AND locker_id = {1}"
full_check_query = check_query.format(userid,lockerid)
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




