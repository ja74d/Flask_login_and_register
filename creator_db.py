#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="javad",
        password="40517780"

        )

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE blog_db")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
