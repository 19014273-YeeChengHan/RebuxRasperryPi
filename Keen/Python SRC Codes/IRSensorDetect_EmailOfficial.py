import RPi.GPIO as GPIO
import time
from datetime import datetime
import mysql.connector
from mysql.connector import Error
import smtplib
import schedule

#Function to convert List of strings to a string with a separator
def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str

#Establish Database Connection

connection = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

cursor = connection.cursor()


#Retrieve item id that have NULL descriptions
sql_null_description = "SELECT * FROM Item WHERE description IS NULL;"
cursor = connection.cursor()
cursor.execute(sql_null_description)

# creating an empty list
itemID_list = []


for(item_id,category_id, description, dimension, weight) in cursor:
    
    itemID_list.append(item_id)
formatted_itemID_list = str(itemID_list)[1:-1]
    
#Email

def send_email():
    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("rebuxrepublicpolytechnic@gmail.com", "rebuxpassword")
    message = """Subject: Rebux Chute Deposited Items\n

Dear User,\n

The following lost item(s) has been deposited in the Chute.The following item IDs are below: \n 
{}
    
Please go to the Chute and update the description for the mentioned items.
    """
    server.sendmail("rebuxrepublicpolytechnic@gmail.com", "keenlovinorebux@gmail.com", message.format(formatted_itemID_list))
    server.quit()
    print("email sent")
    
schedule.every(3).hours.do(send_email)
#Uncomment for Testing the frequency of email sent
#Demonstration for final evaluation
#schedule.every(10).seconds.do(send_email)

#IR Sensor connected to GPIO4
sensor = 4
#Positive terminal of buzzer connected to GPIO21 connect to GPIO Board
buzzer = 21 
i = 0
#BCM Refers to the labelled pins OF THE T-cobbler connected to Rasp Pi
GPIO.setmode(GPIO.BCM) 
GPIO.setup(sensor,GPIO.IN)
GPIO.setwarnings(False)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,True)
print ("IR Sensor Ready To Detect")
print (" ")

while True:
    
    if (GPIO.input(sensor) == 1):
          
        GPIO.output(buzzer,False)
        GPIO.output(buzzer,GPIO.LOW)
          
        datetime_retrieved = datetime.now();
        formatted_datetime_retrieved= datetime_retrieved.strftime("%Y/%m/%d %H:%M:%S")
          
        if (i == 1):
            
            print("\n");
            print("Rebux Chute")
            print("An item has been deposited in the Chute at " + formatted_datetime_retrieved);
        
            
            sql_select_Query = "SELECT * FROM Item ORDER BY item_id DESC LIMIT 1;"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
              
            #Item Table and Chute Table
            #Loop through result data in sql_select_Query
            for(item_id, category_id, description, dimension, weight) in cursor:
                newest_item_id = item_id + 1
                           
            sql_insert_item_table ="INSERT INTO Item (item_id, category_id, dimension, weight) VALUES ({0}, {1}, '{2}', {3});"
            sql_insert_chute_table = "INSERT INTO Chute (item_id, date_time) VALUES ({0}, '{1}');"
              
            sql_insert_item_tablevalue = sql_insert_item_table.format(newest_item_id, 9,'TBC', 0)
            sql_insert_chute_tablevalue = sql_insert_chute_table.format(newest_item_id, formatted_datetime_retrieved)
              
              
            cursor.execute(sql_insert_item_tablevalue)
            cursor.execute(sql_insert_chute_tablevalue)
            connection.commit()
              
            if (cursor.rowcount == 1):
         
                #Used string.format to neatly print out the lost item details inserted to database
                lost_item_details = "An item with the following details: \n\nItem ID: {} \nItem Date & Time Deposited: {}\n\nHas been successfully added to the database.".format(newest_item_id,formatted_datetime_retrieved)
                print("_____________________________________________")
                print(lost_item_details)
                print("_____________________________________________")
                  
            else:
                print("Could not be added to database.")
          
        i = 1

        #IR Sensor always looping to check when lost item has been deposited
        while GPIO.input(sensor):
            print("Detecting for item...")
            time.sleep(0.5)
            
            #Call the automatic sending of email function
            schedule.run_pending()
            time.sleep(1)

    else:
         GPIO.output(buzzer,True)


GPIO.cleanup()

