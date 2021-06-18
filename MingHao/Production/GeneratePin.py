import random
import datetime
import mysql.connector
import os
from twilio.rest import Client
import getpass
import hashlib





#Connecting to DB
conn = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

cursor = conn.cursor()


#Asking For Menu Input Choice
isAuthorised = False
userMenuInput = 0

while userMenuInput != 2:

    print("_______________________________________")
    print("WELCOME TO REBUX LOST N FOUND")
    print("_______________________________________")
    print("1. Generate Pin For Locker Unlock")
    print("2. Exit")

    userMenuInput = int(input("Please Enter: "))
    
    if userMenuInput == 2:
        #Closing Connections/ Clean Up with corresponding message to User
        cursor.close()
        conn.commit()
        conn.close()
        
        print("Thank you for using Rebux Lost & Found System. Goodbye.")
        exit()
        
    else:
        #Authorisation Sequence (Asking User for Corresponding Login Credentials)
        #Also Checking For Validity of UserInput such as only INT for UserID, and CASE SENSITIVE Checks for Password via Hasbytes
        while isAuthorised == False:
            
            print("_______________________________________")
            print("Enter Login Credentials")
            print("_______________________________________")
            
            userInputID = input("Please Enter Your User ID: ")
	    #User's Input Password hidden via Getpass libary for increase security
            userInputPassword = getpass.getpass(prompt='Please Enter Your Password: ')
            hash_object = hashlib.sha256(userInputPassword.encode())
            hex_dig = hash_object.hexdigest()
            if any(s.isdigit() == False for s in userInputID):
                print ("** USER ID SHOULD NOT CONTAIN LETTERS OR SPECIAL CHARACTERS, PLEASE TRY AGAIN !!! **")

            else:
                 #Check if User ID and Password is Valid
                isValidUserQuery = "SELECT * FROM Users WHERE user_id = {0} AND password = '{1}';"
                fullIsValidUserQuery = isValidUserQuery.format(userInputID, hex_dig)

                cursor.execute(fullIsValidUserQuery)

                result = cursor.fetchall()
                
                #User Found
                if len(result) == 1:
                    isAuthorised = True
                
                #User Not Found
                else:
                    print("** INVALID USERNAME AND PASSWORD COMBINATION PLEASE TRY AGAIN !!! **")
        
        
        #After Authorisation is Complete
        #Ask User for Size of Locker Needed, Hence First Digit of Pin can be hardcoded to fit these requirements
        #Declaration of Public Varaiable
        pin = ""
        userInputSize = 0
        
        print("_______________________________________")
        print("Enter Desired Locker Size")
        print("_______________________________________")
        print("1. Small")
        print("2. Medium")
        print("3. Large")
        
        userInputSize = int(input("Please Enter: "))
        
        #Generating Remaning Digits via Random Function for Pin
        i = 1

        while (i < 5):
            singleRandomPinDigi = random.randint(0,9)
            
            #Hardcoding the First Digi to the respective values of 1, 2 or 3 based on Locker Size selected, Will be used later for opening algorithm
            if i == 1:
                if userInputSize == 1:
                    pin = pin + "1"
                    
                elif userInputSize == 2:
                    pin = pin + "2"
                    
                elif userInputSize == 3:
                    pin = pin + "3"
                    
                i = i + 1
                
            else:
                pin = pin + str(singleRandomPinDigi)
                i = i + 1


        #Updating Pin Table with Newly Generated Pin
        currentDateTime = datetime.datetime.now()
        stringCurrentDateTime = currentDateTime.strftime('%Y-%m-%d %H:%M:%S')

        query1 = "INSERT INTO Pin (pin_id, generate_date_time) VALUES('{0}', '{1}');"
        query2 = "INSERT INTO `Pin Session` (pinsession_id, user_id, pin_id, generate_date_time, use_date_time, status) VALUES(NULL, '{0}', '{1}', '{2}', NULL, 'Reported');"
        fullInsertQuery1 = query1.format(pin, stringCurrentDateTime)
        fullInsertQuery2 = query2.format(userInputID, pin, stringCurrentDateTime)

        cursor.execute(fullInsertQuery1)
        cursor.execute(fullInsertQuery2)


        #Send Pin to User
        twilioAccSSID = "ACf5da1645597d0798f4ff3be7c16dfeb4"
        twilioAccTOKEN = "8109477889737ed2b1e4ffce1b807b62"
        messageFormat = "REBUX: Dear Finder, Use {0} as a One-Time Password for Locker Opening (do NOT share it with anyone). This OTP expires at {1} SG Time."
        otpExpireDateTime = currentDateTime + datetime.timedelta(minutes=15)
        strOtpExpireDateTime = otpExpireDateTime.strftime('%Y-%m-%d %H:%M:%S')

        actualMessage = messageFormat.format(pin, strOtpExpireDateTime)

        client = Client(twilioAccSSID,twilioAccTOKEN)

        client.messages.create(
                body = actualMessage,
                to = "+6588159408",
                from_ = "+16314961976"
            )
        
    
