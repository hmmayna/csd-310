""" 
    Title: pysports_join_queries.py
    Author: Heather Maynard
    Date: February 12, 2023
    Description: Player and Team Table Joins
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #results
    players = cursor.fetchall()

    print("\n  -- PLAYER RECORDS --")
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Invalid Username and/or Password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The Database Does Not Exist")

    else:
        print(err)

finally:
    """ Connection Close """

    db.close()
