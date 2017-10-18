# Team Zhango - Samantha Ngo & Yuyang Zhang
# SoftDev - pd07
# hw10 - Average
# 2017-10-18

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
    c.execute("CREATE TABLE peeps_avg(id INT, average REAL);")
    db.commit()
    print "Created peeps_avg table in discobandit.db."
except:
    print "peeps_avg table already created."

# Extract marks and calculate averages
def calculateAverages():
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
        command = "INSERT INTO peeps_avg(id, average) VALUES (" + str(x) + "," + str(average) + ");"
        print command
        c.execute(command)
        db.commit()
        print "++++++++++++++++++++++++++++++"
        x += 1

# Notes: TUPLES
# * Tuples are like rows in a csv file
# * A single value in a tuple looks like this: ('math',)
# * Access tuples like a string/array by using indices: tupleName[0] or tuple[1:5]

# Fill peeps_avg
calculateAverages()

def overallGrade(id):
    command = "SELECT average FROM peeps_avg WHERE id=" + str(id) + ";"
    singleTuple = c.execute(command)
    for a in singleTuple:
        return a[0]

def courseGrade(code,id):
    command = "SELECT mark FROM Courses WHERE code = '" + code + "' AND Courses.id = " + str(id) + ";"
    # print "COMMAND: " + command
    mark = c.execute(command)
    for m in mark:
        try:
            return m[0]
        except:
            return "This student is not taking this course."

print "------------- Testing Getting Grades stuff -----------------------------"
print "A: ", overallGrade(3)
print "B: ", courseGrade("greatbooks",3)
print "C: ", overallGrade(7)
print "D: ", courseGrade("ceramics", 3)
print "------------------------------------------------------------------------"

# Display
def displayAverages():
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
        command = "SELECT average FROM peeps_avg WHERE id = " + str(x) + ";"
        singleT = c.execute(command)
        for a in singleT:
            print "  Average: " + str(a[0])
            print "==========================================="
        x += 1

'''       
def update_average(id, avg):
    command = "UPDATE peeps_avg SET average = " + str(avg) + " WHERE id = " + str(id) + ";"
    update_avg = c.execute(command)
    command = "SELECT average FROM peeps_avg WHERE id = " + str(id) + ";"
    show_avg = c.execute(command)
    for a in show_avg:
        return a[0]
'''


def add_row(code, mark, stu_id, average):
     command = "INSERT INTO courses VALUES(\"" + str(code) + "\" , " + str(mark) + ", " + str(stu_id) + ", " + str(average) + ");"
     c.execute(command)
     calculateAverages()
     x = 1
     while x <= 10:
        print "  Student ID: ", x
        # Find name associated with id x
        command = "SELECT name FROM Peeps WHERE id = " + str(x) + ";"
        singleT = c.execute(command)
        for n in singleT:
            print "  Name: " + n[0]
            # Find average associated with id x
        command = "SELECT average FROM peeps_avg WHERE id = " + str(x) + ";"
        singleT = c.execute(command)
        for a in singleT:
            print "  Average: " + str(a[0])
        x += 1

        
# Functions being run:
displayAverages()
#uprint(update_average(1, 100))
add_row("drafting", 100, 1, -1)

# Close DATABASE
db.close()
print
print "Closed DATABASE"

