Dedsert technical test
========================

File listing:
-------------
fizzbuzz.py
dedsert_DB_connector.py
lotto.py
dedsertgame.py


File Descriptions:
------------------

fizzbuzz.py
-----------
This application prints the numbers replacing multiples of 3 with fizz, multiples of 5 with buzz and multiples of both with fizzbuzz.

dedsert_DB_Connector.py
-----------------------

This is a python script that connected to a MYSQL DB (InnoDB) and allows you to view and create records in a table called dedsert test. you can create an object that can connect to different servers and databases, and would be used as such:

import dedsert
db = dedsertDB('ip', '3306', 'user', 'password' 'database')
db.create_user('Adam Marc Jeanes', 22, 'Server Developer')
db.list_users()

lotto.py
--------
Calculates the next Irish lotto draw or the next Irish lotto on the given date as an arguement:

Usage(nearest lotto draw): python lotto.py
Usage (specified date): python lotto.py 2013-06-21


dedsertgame.py
--------------
This is a game simulation that places 10 random players on a 100x100 pitch and they move in a random direction and if any of the players comes within two blocks of the player that enters the radius first is given a yellow card and teleported to a random location on the board, if the player gets a second yellow card, they are taken out of the game for 10 'ticks' and they ask to enter the game, once they enter another players radius they are removed from the game and the last play left is the winner.

I was asked to make each tick one second, but would take forever to run in regards to the ammount of moves required in the game.

Recently added added a realtme hook so that each move lasts 1 second, causing games that will go on for hours if your willing to watch.