
    Title: pysports_queries.py
    Author: Heather Maynard
    Date: 5 February 2023
    Description: Query MySQL Database Tables

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "hmayna",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards');

INSERT INTO team(team_name, mascot)
    VALUES('Team Sauron', 'Orcs');

-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Thorin', 'Oakenshield', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Bilbo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Frodo', 'Baggins', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Saruman', 'The White', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Angmar', 'Witch-king', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Azog', 'The Defiler', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));
   
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    teams = cursor.fetchall()

    print("\n  -- TEAM RECORDS --")
     
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))
 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    players = cursor.fetchall()

    print ("\n  -- PLAYER RECORDS --")

    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Please Press Any Key To Continue On. ")

except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid Username and/or Password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  This database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
    db.close()
