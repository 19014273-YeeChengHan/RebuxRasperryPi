import datetime
import mysql.connector
import os





#Connecting to DB
conn = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

cursor = conn.cursor()


#Retrival of all Generated Pin Records (Status = Generated, != Used or Expired (as already tried on the kiosk)
selectUnExpiredQuery = "SELECT * FROM `Pin Session` WHERE use_date_time IS NULL AND status = 'Generated';"

cursor.execute(selectUnExpiredQuery)
results = cursor.fetchall()

#while (i < len(results)):

#    aft24hrs_generate_date_time = generate_date_time + timedelta(hours=24)
#    print (aft24hrs_generate_date_time)

for row in results:
    now = datetime.datetime.now()
    retrived_date_time = row[3]
    retrived_date_time_for_check = retrived_date_time + datetime.timedelta(hours=24)

    if(now > retrived_date_time_for_check):
        updateExpiredQuery = "UPDATE `Pin Session` SET status = 'Expired'  WHERE user_id = '{0}' AND pin_id = '{1}' AND status = 'Generated';"
        fullUpdateExpiredQuery = updateExpiredQuery.format(row[1],row[2])

        cursor.execute(fullUpdateExpiredQuery)


cursor.close()
conn.commit()
conn.close()
