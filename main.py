
import sqlite3
conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()

# Initial Menu:
def displayMenu():
    choice = 0
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Options menu: ")
        print("    1. Create/Add a record")
        print("    2. Update/Amend a record")
        print("    3. Delete a record")
        print("    4. Print all records")
        print("    5. Exit")
        choice = input("Which option do you want to choose? ")
        if choice not in ["1", "2", "3", "4", "5"]:
            print("INVALID OPTION, please choose from the below: ")
    return choice

####################
# Options Functions:
####################

# Add Film:
def addFilm():
    film = []
    filmID = input("Enter a new Film ID: ")
    title = input("Enter the film Title: ")
    yearReleased = input("Enter the Year of Release: ")
    rating = input("Enter the rating (G, PG or R): ")
    duration = input("Enter the duration: ")
    genre = input("Enter the genre (Action, Fantasy, Comedy, Crime or Animation): ")
    film.append(filmID)
    film.append(title)
    film.append(yearReleased)
    film.append(rating)
    film.append(duration)
    film.append(genre)
    try:
        cursor.execute("INSERT INTO tblFilms VALUES (?,?,?,?,?,?)", film)
        print("New record added: ")
        for row in cursor.execute("Select * from  tblFilms"):
            print(row)
    except:
        print("""A MATCHING record already exists.
        Record not added
        """)
    conn.commit()
    return addFilm

# addFilm()

# Update Film:
def update():
    cursor = conn.cursor()
    idQuestion = input("Enter the record ID you want to update: ")
    fieldQ = input("What field would you like to update (title, yearReleased, rating, duration, genre)? ")
    newValue = input("Enter the new value for this field: ")
    newValue = "'" + newValue + "'"
    print(newValue)
    try:
        cursor.execute(f"UPDATE tblFilms SET {fieldQ}={newValue} WHERE fildID={idQuestion}")
        conn.commit()
        print("Record updated")
    except:
        print("Invalid data entered")
    return update


# Delete Film:
def delete():
    delEntry = input("Enter the ID of the record you want to delete: ")
    try:
        cursor.execute("DELETE FROM tblFilms WHERE filmID =" + delEntry)                            

        print("\nRecord deleted")        
    except:
        print("\nNo record with this ID  exists")
    conn.commit()
# delete()

def printAll():
    for row in cursor.execute("SELECT * FROM tblFilms"):
        print (row)
# printAll()


def exit():
    conn.close()
    print("Program closed")


# Menu Control Statement:
menu = True
while menu == True:
    choice = displayMenu()
    if choice == "1":
        addFilm()
    elif choice == "2":
        update()
    elif choice == "3":
        delete()
    elif choice == "4":
        printAll()
    elif choice == "5":
        exit()
    else:
        menu = False
input("Press enter to exit the program")