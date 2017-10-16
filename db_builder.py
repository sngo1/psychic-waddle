# Samantha Ngo
# SoftDev - pd 7
# hw09 - sqlite
# 2017-10-15

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
#==========================================================
createTable = "CREATE TABLE <table name> (<values>)"
newRow = "INSERT INTO <table name> (<columns>) VALUES (<values>)"
tableName = ""
values = ""
command = ""

def coursesCSV():
    # Courses csv file
    tableName = "Courses"
    columns = "code TEXT, mark INT, id INT"
    command = createTable.replace("<table name>", tableName)
    command = command.replace("<values>", columns)
    print "CREATE TABLE COMMAND: ", command
    try:
        c.execute(command)
    except:
        print "Table already created."
        
    columns = "code, mark, id"

    # Read through csv file
    with open('courses.csv') as csvfile:
        print "OPEN COURSES: ", open("courses.csv")
        # Note: uses first row in csv as fieldnames in form of keys
        reader = csv.DictReader(csvfile) # Creates INSTANCE of DictReader
        for row in reader:
            command = newRow.replace("<table name>", tableName).replace("<columns>", columns)
            print "ROW DATA: ", row
            values =  '"' + row["code"] + '"' + "," + row["mark"] + "," + row["id"]
            command = command.replace("<values>",values)
            print "NEW ROW COMMAND: ", command
            c.execute(command)
        
        db.commit() #save changes
    print
    print "Created COURSES csv table. ======================================="
    return "Created COURSES csv table."

# -------------------------------------------------COURSES TESTS--------------
coursesCSV()

# Check that global variables have not been changed by coursesCSV():
print "CREATE TABLE VAR: " + createTable
print "NEW ROW VAR: " + newRow
print "TABLE NAME VAR: " + tableName
print "VALUES VAR: " + values
print "COMMAND VAR: " + command
print "======================================================================="
print 

# ----------------------------------------------------------------------------
def peepsCSV():
    # Peeps csv file
    tableName = "Peeps"
    columns = "name TEXT, age INT, id INT"
    
    command = createTable.replace("<table name>", tableName)
    command = command.replace("<values>", columns)
    print "CREATE TABLE COMMAND: ", command
    try:
        c.execute(command)
    except:
        print "Table already created."

    # Adjust column values for INSERT commands
    columns = "name, age, id"

    # Read through csv file
    with open('peeps.csv') as csvfile:
        print "OPEN PEEPS FILE: ", open("peeps.csv")
        # Note: uses first row in csv as fieldnames in form of keys
        reader = csv.DictReader(csvfile) # Creates INSTANCE of DictReader
        for row in reader:
            command = newRow.replace("<table name>", tableName).replace("<columns>", columns)
            print "ROW DATA: ", row
            values =  '"' + row["name"] + '"' + "," + row["age"] + "," + row["id"]
            command = command.replace("<values>",values)
            print "NEW ROW COMMAND: ", command
            c.execute(command)
        
        db.commit() #save changes
    print
    print "Created PEEPS csv table. ======================================="
    return "Created PEEPS csv table."

# Testing PEEPS TABLE ======================================================
peepsCSV()

# Close DATABASE
db.close()
print
print "Closed DATABASE"

