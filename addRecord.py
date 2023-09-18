from connection import db # import the connect.py module hm


# create a function
def insert_data():

    #Note : SongID is set to autoincrement, input/data is not required
    # ask for the user input Title, Artist, Genre
    filmTitle = input("Enter the film's title: ")
    yearReleased = int(input("Enter the year the film was released: "))
    rating = input("Enter the film's rating: ")
    duration = int(input("Enter the film's duration: "))
    genre = input("Enter the film's genre: ")

    dbCursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)", (filmTitle, yearReleased, rating, duration, genre))
    dbCon.commit() # permanently write this record to the table in the database
    print(f"{filmTitle} inserted into database")


if __name__ =="__main__": # if __name__ == "addSongs.py"
    insert_data()