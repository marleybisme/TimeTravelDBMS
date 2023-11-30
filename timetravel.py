import mysql.connector

# Execute:
# python3 timetravel.py
#

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="timetravel"
)


#FUNCTIONS

# FUNCTIONS FOR USERS

def showallUsers():
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM Users")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
    
  return;

def findUserbyID():
    
    id = input("Traveler ID: ")

    mycursor = mydb.cursor()
    sql = "SELECT UserID, UserName, Email, DateOfBirth FROM Users WHERE UserID = %s"
    arg = (id, )

    mycursor.execute(sql, arg)

    myresult = mycursor.fetchall()

    for x in myresult:
       print(x)
    
    return;

def findUserbyName():
  name = input("Name: ")

  mycursor = mydb.cursor()

  sql = "SELECT UserID, UserName, Email, DateOfBirth "\
        "FROM Users "\
        "WHERE UserName LIKE %s"
      
  arg = (name, )

  mycursor.execute(sql, arg)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

  return;

def insertTraveler():
  name = input("Traveler Name: ")
  email = input("Email: ")
  pw = input("Password: ")
  dob = input("DOB (YYYY-MM-DD): ")

  

  mycursor = mydb.cursor()

  sql = "INSERT INTO Users(UserName, email, Password, DateOfBirth) " \
                                    "VALUES(%s,%s,%s,%s)"
    
  arg = (name, email, pw, dob, )

  mycursor.execute(sql, arg)

  mydb.commit()
  return;

# FUNCTIONS FOR MACHINES

def showallMachines():
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM TimeMachines")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
    
  return;

def findMachinebyID():
    
    id = input("Time Machine ID: ")

    mycursor = mydb.cursor()
    sql = "SELECT * FROM TimeMachines WHERE MachineID = %s"
    arg = (id, )

    mycursor.execute(sql, arg)

    myresult = mycursor.fetchall()

    for x in myresult:
       print(x)
    
    return;

def findMachinebyManu():
  manu = input("Manufacturer Name: ")

  mycursor = mydb.cursor()

  sql = "SELECT * " \
        "FROM TimeMachines " \
        "WHERE Manufacturer = %s"
      
  arg = (manu, )

  mycursor.execute(sql, arg)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

  return;

def insertMachine():
  manu = input("Machine Manufacturer: ")
  Model = input("Machine Model: ")
  Capacity = input("Machine Capacity: ")

  

  mycursor = mydb.cursor()

  sql = "INSERT INTO TimeMachines (Model, Manufacturer, Capacity) " \
                                    "VALUES(%s,%s,%s)"
    
  arg = (Model, manu, Capacity, )

  mycursor.execute(sql, arg)

  mydb.commit()
  return;

#FUNCTIONS FOR BOOKINGS

def showallBookings():
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM Bookings")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
    
  return;

def findBookingbyID():
    
  id = input("Booking ID: ")

  mycursor = mydb.cursor()
  sql = "SELECT * FROM Bookings WHERE BookingID = %s"
  arg = (id, )

  mycursor.execute(sql, arg)

  myresult = mycursor.fetchall()

  for x in myresult:
      print(x)
  
  return;

def insertBooking():

  UserID = input("Traveler ID: ")
  mach_id = input("Machine ID: ")
  dest_id = input("Destination ID: ")
  book = input("Booking Date (YYYY-MM-DD): ")
  dept = input("Departure Date (YYYY-MM-DD): ")
  ret = input("Return Date (YYYY-MM-DD): ")


  mycursor = mydb.cursor()

  sql = "INSERT INTO Bookings (UserID, MachineID, DestinationID, BookingDate, DepartureDate, ReturnDate) " \
                                    "VALUES(%s, %s, %s, %s, %s, %s)"
    
  arg = (UserID, mach_id, dest_id, book, dept, ret, )

  mycursor.execute(sql, arg)

  mydb.commit()
  return;

#FUNCTIONS FOR DESTINATIONS

def showallDestinations():
  
  mycursor = mydb.cursor()

  mycursor.execute("SELECT * FROM Destinations")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
    
  return;

def findDestbyID():
    
    id = input("Destination ID: ")

    mycursor = mydb.cursor()
    sql = "SELECT * FROM Destinations WHERE DestinationID = %s"
    arg = (id, )

    mycursor.execute(sql, arg)

    myresult = mycursor.fetchall()

    for x in myresult:
       print(x)
    
    return;

def findDestbyName():
  dest = input("Country Name: ")

  mycursor = mydb.cursor()

  sql = "SELECT * " \
        "FROM Destinations " \
        "WHERE Location = %s"
      
  arg = (dest, )

  mycursor.execute(sql, arg)

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)

  return;

def insertDestination():
  Location = input("Destination Location: ")
  TimePeriod = input("Time Period: ")
  Description = input("Description: ")

  mycursor = mydb.cursor()

  sql = "INSERT INTO Destinations (Location, TimePeriod, Description) " \
                                    "VALUES(%s, %s, %s)"
    
  arg = (Location, TimePeriod, Description, )

  mycursor.execute(sql, arg)

  mydb.commit()
  return;


option = 0;

while option != 16: 
    #TODO: edit to fit new database
    print("")
    print("1. Add a time traveler")
    print("2. Find a traveler by id")
    print("3. Find a traveler by name")
    print("4. Show all time travelers")
    print("---------------------------")
    print("5. Add a time machine")
    print("6. Find a time machine by id")
    print("7. Find a time machine by Manufacturer")
    print("8. Show all time machines")
    print("---------------------------")
    print("9. Add a booking")
    print("10. Find a booking by id")
    print("11. Show all bookings")
    print("---------------------------")
    print("12. Add a destination")
    print("13. Find a destination by id")
    print("14. Find a destination by Location")
    print("15. Show all destinations")

    print("16. Exit")
    
    option = int(input("Choice: "))
    print (option)
    if option == 1:
        insertTraveler()
    elif option == 2:
        findUserbyID()
    elif option == 3:
        findUserbyName()
    elif option == 4:
        showallUsers()
    elif option == 5:
        insertMachine()
    elif option == 6:
        findMachinebyID()
    elif option == 7:
        findMachinebyManu()
    elif option == 8:
        showallMachines()
    elif option == 9:
        insertBooking()
    elif option == 10:
        findBookingbyID()
    elif option == 11:
        showallBookings()
    elif option == 12:
        insertDestination()
    elif option == 13:
        findDestbyID()
    elif option == 14:
        findDestbyName()
    elif option == 15:
        showallDestinations()

