from connect import * 

# create a function to read records in the songs table
def read_data():

    #select all records in the song table
    dbCursor.execute("SELECT * FROM tblFilms")

    # fetch the selected songs using the fetchall() method
    allRecords = dbCursor.fetchall()

    #loop through the fetched records
    for eachRecord in allRecords:
        # and display each record in the terminal
        print(eachRecord)

if __name__ == "__main__":
    read_data()