#Task 4.2

class Person:
    def __init__(self, full_name, date_of_birth):
        self.name = full_name
        self.dob = date_of_birth

    #Get set
    def getName(self):
        return self.name

    def getDOB(self):
        return self.dob

    def setName(self, name):
        self.name = name

    def setDOB(self, dob):
        self.dob = dob

    #Qn functions
    def is_adult(self):
        year, month, day = self.dob.split("-") #Seperate them all

        age = 2026 - int(year)

        if age > 18:
            return True
        else:
            return False

    def screen_name(self):
        output = ""

        for i in self.name:
            if i.isalpha():
                output += i
        #print(output) #Checking

        year, month, day = self.dob.split("-") #Seperate them all
        output += month
        output += day
        return output


class Staff(Person):
    def screen_name(self):
        output = super().screen_name()
        output += "Staff"
        return output

    def is_adult(self):
        return True

class Student(Person):
    def is_adult(self):
        return False




#Reading segment
file = open("people.txt", 'r')

data = []
for line in file:
    line = line.strip().split(",")
    data.append(line)

file.close()

#print(data)

#DB
import sqlite3
conn = sqlite3.connect("school.db")
conn.execute("DROP TABLE IF EXISTS People")
conn.execute("""CREATE TABLE People(
                PersonID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                FullName TEXT NOT NULL,
                DateOfBirth TEXT NOT NULL,
                ScreenName TEXT NOT NULL,
                IsAdult INTEGER NOT NULL)""")


for i in data:
    #print(i[-1])
    Class = i[2]
    name = i[0]
    dob = i[1]

    #Create class
    if Class == "Person":
        temp = Person(name, dob)
    elif Class == "Staff":
        temp = Staff(name, dob)
    elif Class == "Student":
        temp = Student(name, dob)

    #Get all values
    screenName = temp.screen_name()
    
    adult = temp.is_adult()
    if adult == True: #Change boolean to integers
        adult = 1
    else:
        adult = 0

    print(name)
    print(dob)
    print(screenName)
    print(adult)

    conn.execute("""insert into People(FullName, DateOfBirth,
                    ScreenName, IsAdult) values (?,?,?,?)""",
                    (name, dob, screenName, adult))


conn.commit()
conn.close()
