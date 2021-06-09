

import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "rebuxphpdbadmin",
    password = "rebuxphpdbadminpassword",
    database = "RebuxDB"
)

cursor = conn.cursor()

query = "SELECT * FROM Pin;"

cursor.execute(query)

for(pin_id, date_time) in cursor:
    print(pin_id, date_time)

cursor.close()
conn.close()


