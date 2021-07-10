import RPi.GPIO as GPIO
import time
from datetime import datetime
import mysql.connector
from mysql.connector import Error

#Establish Database Connection

connection = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

                

cursor = connection.cursor()

"""
Desc: 
 Function to convert List of strings to a string with a separator
"""

def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str

#Testing functions
sensor = 4  #IR Sensor connected to GPIO4
buzzer = 21 #Positive terminal of buzzer connected to GPIO21 connect to GPIO Board
i = 0
GPIO.setmode(GPIO.BCM) #BCM Refers to the labelled pins OF THE T-cobbler connected to Rasp Pi
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,True)
print ("IR Sensor Ready...")
print (" ")

try: 
   while True:
        if (GPIO.input(sensor) == 1):
          
          GPIO.output(buzzer,False)
          GPIO.output(buzzer,GPIO.LOW)
          
          datetime_retrieved = datetime.now();
          formatted_datetime_retrieved= datetime_retrieved.strftime("%Y/%m/%d %H:%M:%S")
          
          if (i == 1):
              
              print("An item has been placed in the Chute at " + formatted_datetime_retrieved);
              # creating an empty list
              description_list = []
              seperator = ', '

              # number of elements as input
              number_of_description = int(input("Enter the number of descriptions you would like to give the item. Minimum and maximum number of descriptions is 4 and 7 respectively. : "))  
              
              while number_of_description < 4 or number_of_description > 7 :
                  print("Error occured: Number of description cannot be less than 4 or more than 7. Please try again.")
                  number_of_description = int(input("Enter the number of descriptions you would like to give the item. Minimum and maximum number of descriptions is 4 and 7 respectively. : "))
                  
                  
              
              
              # iterating till the range
              for i in range(0, number_of_description):
                    
                  item_desc = input("Please enter description: ")

                  description_list.append(item_desc) # adding the element
                        
              print(description_list)
              string_description_list = converttostr(description_list, seperator)

              sql_select_Query = "SELECT * FROM Item ORDER BY item_id DESC LIMIT 1;"
              cursor = connection.cursor()
              cursor.execute(sql_select_Query)
              
              #Item Table and Chute Table
              #Loop through result data in sql_select_Query
              for(item_id, category_id, description, dimension, weight) in cursor:
                  newest_item_id = item_id + 1
                           
              sql_insert_item_table ="INSERT INTO Item (item_id, category_id, description, dimension, weight) VALUES ({0}, {1}, '{2}', '{3}', {4});"
              sql_insert_chute_table = "INSERT INTO Chute (item_id, date_time) VALUES ({0}, '{1}');"
              
              sql_insert_item_tablevalue = sql_insert_item_table.format(newest_item_id, 9, string_description_list, 'TBC', 0)
              sql_insert_chute_tablevalue = sql_insert_chute_table.format(newest_item_id, formatted_datetime_retrieved)
              
              #print(sql_insert_chute_tablevalue)
              print(sql_insert_item_tablevalue) 
              
              cursor.execute(sql_insert_item_tablevalue)
              cursor.execute(sql_insert_chute_tablevalue)
              connection.commit()

             
          i = 1

          #These 2 lines prevent the program from running continuously 
          while GPIO.input(sensor):
              print("Detecting for item...")
              time.sleep(0.5)

        else:
          GPIO.output(buzzer,True)
          


except KeyboardInterrupt:
    GPIO.cleanup()
    
    
    

