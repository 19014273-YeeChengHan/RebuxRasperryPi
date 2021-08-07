import smtplib
from email.message import EmailMessage
import mysql.connector
from mysql.connector import Error
from datetime import datetime

#Establish Database Connection

connection = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

#SQL Queries
sql_select_sessionid = "SELECT * FROM Session"
cursor = connection.cursor()
cursor.execute(sql_select_sessionid)

#session_id = cursor.fetchone()

for(session_id, user_id, locker_id, item_id,pinsession_id ,type, date_time,status) in cursor:
    
    #Get locker_id
    retreived_lockerid = str(locker_id)
    
    #Get user_id 
    retreived_userid = str(user_id)
    
    #Get the last row of session_id
    retreived_id = str(session_id)
    
    #Get the retrieved date time when locker door has been successfully closed
    retreived_datetime = str(date_time)
    #Get item_id
    retreived_itemid = str(item_id)

#SQL to get the user's name to be placed in the email
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
#Remove bracket and comman when retreive name from Session table
username, = name

#SQL to get category ID from Item table
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

#Email Variables
def send_email_acknowledgement(name,lockerid, datetime,category,desc):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("rebuxrepublicpolytechnic@gmail.com", "rebuxpassword")
    message = """Subject: Rebux Deposit Confirmation\n
    Dear {0},\n
    You have successfully deposited a lost item with the following details below:\n
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


