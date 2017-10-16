# Team Zhango - Samantha Ngo & Yuyang Zhang
# SoftDev - pd07
# hw10 - Average
# 2017-10-16

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

command = "CREATE TABLE avg_table(name TEXT, stu_id INTEGER, avg NUMBERIC);" #creates new table for avg
c.execute(command)


 
for row in peeps: #goes through each row
    command = "SELECT mark FROM courses WHERE peeps.id = courses.id;" #finds all the marks for person with id X
    marks = c.execute(command) #places everything into a list
    for x in marks: #for each mark in the list
        total_sum += x #add them up
    avg = total_sum / (len(marks)) #divide by the number of marks and you get the average
    name = '"' + row['name'] + '"' #name on each row
    stu_id = int(row["id"]) #id on each row
   
    command = "INSERT INTO avg_table VALUES(%s, %d, %d);" %(name, stu_id, avg)
    c.execute(command)
   
