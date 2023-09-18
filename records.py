from connect import *
 # create a function to read records in the songs table hm
def reports():

    # select data from the table songs
    # dbCursor.execute("SELECT * FROM songs ORDER BY SongID DESC")
    # dbCursor.execute("SELECT Artist, Genre FROM songs")
    # dbCursor.execute("SELECT * FROM songs WHERE Genre = 'Dance' or Genre  = 'Pop'")
    dbCursor.execute("SELECT * FROM tblFilms ORDER BY title ASC")
    # dbCursor.execute("SELECT Artist, Genre FROM songs ORDER BY Artist ASC")
    # dbCursor.execute("SELECT * FROM songs WHERE Genre LIKE 's%' or Genre Like 'D%'")
    # dbCursor.execute("SELECT Genre FROM songs WHERE Genre LIKE 's%' or Genre Like 'D%'")
    # dbCursor.execute("SELECT * FROM songs WHERE Title NOT LIKE 't%'")
    # dbCursor.execute("SELECT Title FROM songs WHERE Title NOT LIKE 't%'")

    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)


def reports_search():
    # searchField = input("Enter the name of the field you want to search: ").title()
    # searchValue = input()
    # dbCursor.execute(f"SELECT * FROM songs WHERE {searchField} = ")

    titleValue = input("Enter the film title you want to search for: ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Title = '{titleValue}'")

    allRecords = dbCursor.fetchall()
    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__":
    reports()
    reports_search()