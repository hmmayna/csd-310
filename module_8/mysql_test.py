    Title: pysports_test
    Author: Heather Maynard
    Date: 5 February 2023
    Description: pytesting database 

'import statements'

import mysql.connector
from mysql.connector import errorcode

'database config object'

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
  'potential MySQL database errors try/catch block' 

    db = mysql.connector.connect(**config)
    
    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Please press any key to continue on")

except mysql.connector.Error as err:
      
    'error code'

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Invalid Username and/or Password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("This does not exist")

    else:
        print(err)

finally:
    
    'connection close'

    db.close()
