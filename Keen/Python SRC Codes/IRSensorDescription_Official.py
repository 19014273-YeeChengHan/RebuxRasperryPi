#Completed on 26 July 2021, Finalized
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

#Function to convert List of strings to a string with a separator
def converttostr(input_seq, seperator):
    # Join all the strings in list
    final_str = seperator.join(input_seq)
    return final_str

 
def view_null_itemID():
    
    sql_select_nulldesc = "SELECT * FROM Item WHERE description IS NULL;"
    cursor = connection.cursor()
    cursor.execute(sql_select_nulldesc)
    print("The following Item IDs have null description: \n")
    for (item_id, category_id, description, dimension, weight) in cursor:
        item_id = item_id
        print(str(item_id))


def menu():
    
    print ("__________________________________________")
    print ("Welcome to Rebux Chute System")
    print("Option 1: View ID(s) with null desciptions")
    print("Option 2: Enter description for Item ID")
    print ("__________________________________________")

   
try:
    
    menu()
    option = int(input("Enter Option: "))

    while option != 0:
        
        
        if (option == 1):
            
            view_null_itemID()
            menu()
            option = int(input("Enter Option: "))
        
        
        elif (option == 2):
            
            
            user_choice_itemID = int(input("Item ID you would like to enter the description for: "))
            
            #Check for user input of Item ID validity
            sql_select_ID = "SELECT * FROM Item WHERE item_id ={0};"
            sql_select_IDQuery = sql_select_ID.format(user_choice_itemID)
            cursor = connection.cursor()
            cursor.execute(sql_select_IDQuery)
              
            for(item_id, category_id, description, dimension, weight) in cursor:
                if (user_choice_itemID == item_id):
                    print("ID exits.")
            #Check for user input of Item ID validity

            
                    while True:
                        # creating an empty list
                        description_list = []
                        seperator = ', '
                        
                        try:                
                            #Number of descriptions refers to how many item descriptions the One Stop Employee would like to enter for the lost item
                            print("\n__________________________________________________________")
                            print("Instructions:")
                            print("\nNumber of descriptions cannot exceed 8")
                            print("\nNumber of descriptions cannot be less than or equal to 0")
                            print("__________________________________________________________")
                            number_of_description = int(input("Enter the number of descriptions you would like to give the item: "))
                            
                        except ValueError:
                            print("---------------------------------------------------------------------")
                            print("Error occured: You cannot enter a non-number value. Please try again.")
                            print("---------------------------------------------------------------------")
                            continue
                        
                        if number_of_description < 0 or number_of_description == 0:
                            print("----------------------------------------------------------------------------------")
                            print("Error occured: You cannot put a number less than or equal to 0. Please try again. ")
                            print("----------------------------------------------------------------------------------")
                            continue
                        
                        elif number_of_description > 8:
                            print("----------------------------------------------------------------------------------")
                            print("Error occured: You cannot enter a value more than 8. Please try again. ")
                            print("----------------------------------------------------------------------------------")
                            continue
                            
                        
                        else:
                            break
                      
                    print("_______________________________________________________________________________")
                    print("\nInstructions: \nPlease ensure that item descriptions are\n-Unique\n-Specific to the item\n-One worded or a phrase format")
                    print("_______________________________________________________________________________")
                    
                    #Loop based on the number of descriptions entered by One Stop Centre Employee
                    for i in range(0, number_of_description):
                        
                        item_desc = input("Please enter description: ")

                        description_list.append(item_desc) #Adding the element in the array
                    
                    string_description_list = converttostr(description_list, seperator)            
                    sql_insert_item_table ="UPDATE Item SET description ='{0}' WHERE item_id = {1};"
                    

                    sql_insert_item_tablevalue = sql_insert_item_table.format(string_description_list, user_choice_itemID)
                    
                    cursor.execute(sql_insert_item_tablevalue)

                    
                    connection.commit()
                      
                    if (cursor.rowcount == 1):
                        #Used string.format to neatly print out the lost item details inserted to database
                        lost_item_details = "An item with the following details: \n\nItem ID: {} \nItem details: {} \n\nHas been successfully added to the database.".format(item_id, string_description_list)
                        print("_____________________________________________")
                        print(lost_item_details)
                        print("_____________________________________________")
                          
                    else:
                        print("Could not be added to database.")
                        
                elif (user_choice_itemID != item_id):
                    print("Item ID does not exist, please enter Item ID again: ")
                    
                    
            #Show menu again after user finishes insertion            
            menu()
            option = int(input("Enter Option: "))
            
        elif (option!=1 or option!=2):
            
            print("Invalid option entered.")
            menu()
            option = int(input("Enter Option: "))
            continue
        else:
            break
        
#Catch exception if user enteres non-numeric option
except ValueError:
    
    print("Error occured, letters are not allowed.")
    menu()
    option = int(input("Enter Option: "))
    
    


