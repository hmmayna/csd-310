"""
    Title: pysports_update_and_delete.py
    Author: Heather Maynard
    Date: February 12, 2023
    Description: Pysports database updating, deleting, and inserting
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

def show_players(cursor, title):

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #results
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    cursor = db.cursor()

    #player insert
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"

    #player data
    player_data = ("Smeagol", "Shire Folk", 1)

    #insert player
    cursor.execute(add_player, player_data)
 
    db.commit()

    #show records
    show_players(cursor, "DISPLAYING PLAYERS")

    #update
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    
    cursor.execute(update_player)

    #show records
    show_players(cursor, "DISPLAYING PLAYERS")

    #delete
    delete_player = ("DELETE FROM player WHERE first_name = 'Smeagol'")

    cursor.execute(delete_player)

    #show records
    show_players(cursor, "DISPLAYING PLAYERS")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  invalid username and/or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  Database does not exist")

    else:
        print(err)

finally:
    """ close connection """

    db.close()
