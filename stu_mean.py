# Team Zhango - Samantha Ngo & Yuyang Zhang
# SoftDev - pd07
# hw10 - Average
# 2017-10-16

import sqlite3   #enable control of an sqlite database
import db_builder

print "--- Database Setup ------------------------------------------------------"
db_builder.run()
print "--- Database Setup Done -------------------------------------------------"
f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
   
# Commands (without the semicolon)
selectFrom = "SELECT <columns> FROM <tables>"
where = "WHERE <criteria>"
command = ""

# Create a table with id corresponding averages
try:
    c.execute("CREATE TABLE Averages(id INT, average REAL);")
    db.commit()
    print "Created Averages table in discobandit.db."
except:
    print "Averages table already created."

# Extract marks and calculate averages
x = 1
while x <= 10:
        # For each ID, do the following:
        total = 0
        numbers = 0
        
        getAverages = "SELECT mark FROM Courses WHERE id = " + str(x) + ";"
        marks = c.execute(getAverages)# marks is just the location of the object
        for singleTuple in marks:
            # singleTuple is the tuple accessed at the location
            num = singleTuple[0] # Extract the number from the tuple
            print num
            total += num
            numbers += 1

        # Calculate average
        average = total/numbers
        print "Average: ", average

        # Add the average to the table
        command = "INSERT INTO Averages(id, average) VALUES (" + str(x) + "," + str(average) + ");"
        print command
        c.execute(command)
        db.commit()
        print "++++++++++++++++++++++++++++++"
        x += 1

# Notes: TUPLES
# * Tuples are like rows in a csv file
# * A single value in a tuple looks like this: ('math',)
# * Access tuples like a string/array by using indices: tupleName[0] or tuple[1:5]

# Display
print "-------------------------------------------------- Final Data Compilation:"
x = 1
while x <= 10:
    print "  Student ID: ", x
    # Find name associated with id x
    command = "SELECT name FROM Peeps WHERE id = " + str(x) + ";"
    singleT = c.execute(command)
    for n in singleT:
        print "  Name: " + n[0]
    # Find average associated with id x
    command = "SELECT average FROM Averages WHERE id = " + str(x) + ";"
    singleT = c.execute(command)
    for a in singleT:
        print "  Average: " + str(a[0])
    print "==========================================="
    x += 1

# Close DATABASE
db.close()
print
print "Closed DATABASE"

