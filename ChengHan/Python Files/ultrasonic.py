import RPi.GPIO as GPIO
import time
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

cursor = conn.cursor()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

#Declare Variable for GPIO Pins
TRIG=23
ECHO=24

#Declare GLobal Variables
i2 = 0
i = 0
box_length = 20.5
final_list = []

#Ask User for Number of Sides Item has
user_input =int(input('Please enter number of sides, needed to be recorded: '))
if user_input  >3   :
    print("Please do not input more than 3 sides   ");




while i < user_input and user_input <=3 :
    print ("Measuring Side "  + str((i+1)) + "........")

    #Initalise Varaiables for inner loop use.
    inner_i = 0
    reading_list = []
   
    while inner_i < 10:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG,False)

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
        distance=round(distance,5)

        #additional of 2.5 cm added to reading to compensate inaccuracy of sensor caused by physical height of sensor.
        distance = distance + 2.4
        
        #// Commenting this distance out since this data is redundant
        #print (distance)
        reading_list.append(distance)
        
        if (inner_i == 9):
            avg_value = round(sum(reading_list) / len(reading_list),1)
            
            #minus off the reading based on the physical environment length, to find out length of object side we are measuring
            final_side_length = box_length - avg_value
            final_list.append(round(final_side_length,1))
        
        inner_i = inner_i + 1
        
        if (inner_i == 9 and i != int(user_input-1)):    
            print("**PLEASE SWITCH TO NEW SIDE FOR MEASUREMENT NOW**")
        
        #sleep required here to ensure data accuracy of reading. As we capturing 10 seconds and 10 data per reading of side
        time.sleep(1)

    
    time.sleep(5)  

    i = i + 1

#print (*final_list)

'''
________________________
ACTUAL BOX MEASUREMENTS
________________________

             (L)    x (B)    x (H)

Small Box  : 11.5cm x 9.5cm  x 8.5cm
Medium Box : 14.5cm x 12.5cm x 14.5cm
Large Box  : 20.5cm x 14.5cm x 14.5cm

________________________
ACTUAL BOX VOLUME
________________________

Small Box  : 928.6  cm^3
Medium Box : 2628.1 cm^3
Large Box  : 4310.1 cm^3

'''

small_box_area = 928.6
medium_box_area = 2628.1
large_box_area = 4310.1

area_of_item_scanned = multiplyList(final_list)

if (area_of_item_scanned < small_box_area and user_input <=3):
    print('─' * 20)
    print("Dimension")
    print('─' * 20)
    count = 1
    i_final_list = len(final_list)
    while count < i_final_list:
        for x in final_list:
            print( "Side " +  str(count)  +": "  +  str(x) + " cm")
            count = count + 1
    print('─' * 20)
    print("Category")
    print('─' * 20) 
    print("Item Category: Small")

elif (area_of_item_scanned <  medium_box_area and user_input <=3):
    print('─' * 20)
    print("Dimension")
    print('─' * 20)
    count = 1
    i_final_list = len(final_list)
    while count < i_final_list:
        for x in final_list:
            print( "Side " +  str(count)  +": "  +  str(x) + " cm")
            count = count + 1
    print('─' * 20)
    print("Category")
    print('─' * 20) 
    print("Item Category: Medium")

elif (area_of_item_scanned < large_box_area and user_input<=3):
    print('─' * 20)
    print("Dimension")
    print('─' * 20)
    count = 1
    i_final_list = len(final_list)
    while count < i_final_list:
        for x in final_list:
            print( "Side " +  str(count)  +": "  +  str(x) + " cm")
            count = count + 1
    print('─' * 20)
    print("Category")
    print('─' * 20)
    print("Item Category: Large")

elif (user_input <=3 ):
    print ("Item Category is Extra-Large, Please Kindly Proceed to General Chute for Deposit Instead")



    full_str = ' '.join([str(elem) for elem in final_list])



    itemId = input("Please enter the item id: ")

    query = "UPDATE Item SET dimension = '{0}'  WHERE item_id  = {1}"
    full_query = str(query.format(full_str, itemId))

    cursor.execute(full_query)


    cursor.close()
    conn.commit()
    conn.close()
