DROP database IF EXISTS timetravel;
CREATE database timetravel;
USE timetravel;

-- Users Table
CREATE TABLE Users(
    UserID INT NOT NULL auto_increment,
    UserName VARCHAR(35) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Password VARCHAR(35),
    DateOfBirth DATE NOT NULL,
    PRIMARY KEY (UserID)
);

-- Time Machines Table
CREATE TABLE TimeMachines(
    MachineID INT NOT NULL auto_increment,
    Model VARCHAR(35),
    Manufacturer VARCHAR(35) NOT NULL,
    Capacity INT NOT NULL,
    PRIMARY KEY (MachineID)
);

-- Destinations Table
CREATE TABLE Destinations(
    DestinationID INT NOT NULL auto_increment,
    Location CHAR(35) NOT NULL,
    TimePeriod VARCHAR(35) NOT NULL,
    Description TEXT NOT NULL,
    PRIMARY KEY (DestinationID)
);

-- Bookings Table
CREATE TABLE Bookings(
    BookingID INT NOT NULL auto_increment,
    UserID INT NOT NULL,
    MachineID INT NOT NULL,
    DestinationID INT NOT NULL,
    BookingDate DATE NOT NULL,
    DepartureDate DATE NOT NULL,
    ReturnDate DATE NOT NULL,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (MachineID) REFERENCES TimeMachines(MachineID),
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID)
);


-- Add Users
INSERT INTO Users(UserID, UserName, Email, Password, DateOfBirth)
VALUES
    (1, 'Babara Smith', 'b.smith2@yahoo.com', 'abcd', '1988-01-15'),
    (2, 'Jacob Lee', 'jb_lee@gmail.com', 'gia1115', '1999-05-20'),
    (3, 'Michaela Johnson', 'mjohnson98@gmail.com', '12345', '1995-09-08'),
    (4, 'Andre Thompson', 'drethompson23@gmail.com', 'Max23', '2002-03-28'),
    (5, 'David Wright', 'davidw.34@gmail.com', 'sag1998', '1998-12-09');

-- Add Time Machines
INSERT INTO TimeMachines(MachineID, Model, Manufacturer, Capacity)
VALUES
    (100, 'Master of Past 5000', 'Historic Technologies', 4),
    (101, 'Quantum Voyager', 'TimeCraft Inc.', 6),
    (102, 'Eternal Explorer', 'FutureTech Co.', 2),
    (103, 'Destination Past', 'FutureTech Co.', 10),
    (104, 'The Time Capsule', 'FutureTech Co.', 250);

-- Add Destinations
INSERT INTO Destinations(DestinationID, Location, TimePeriod, Description)
VALUES
    (1000, 'Ancient Rome', '100 BC', 'Experience the glory of the Roman Empire.'),
    (1001, 'Future', '3000', 'Explore the technological wonders of the future.'),
    (1002, 'Medieval Kingdom', '979 AD', 'Witness knights and castles in a medieval setting.'),
    (1003, 'Ancient Egypt', '44 BC', 'Witness the marvels of ancient Egypt during the Queen Cleopatra Reign.'),
    (1004, 'Victorian England', '1855', 'Experience the glamour of Victorian Era Britain.');

-- Add Bookings
INSERT INTO Bookings(BookingID, UserID, MachineID, DestinationID, BookingDate, DepartureDate, ReturnDate)
VALUES
    (3000, 1, 100, 1000, '2022-03-10', '2023-04-03', '2023-04-10'),
    (3001, 2, 101, 1001, '2022-05-15', '2023-06-01', '2023-06-10'),
    (3002, 3, 104, 1002, '2023-07-20', '2023-08-04', '2023-08-08'),
    (3003, 3, 103, 1002, '2023-10-20', '2023-02-02', '2023-02-04'),
    (3004, 3, 104, 1002, '2023-11-20', '2023-12-01', '2023-12-14');