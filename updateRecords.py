from connect import * 

#create a function
def update_data():
    # use primary key to update a record
    idField = input("Enter the filmID of the record to be updated: ")

    # field to be updated: Title, YearReleased, Rating, Duration, Genre
    fieldName = input("Enter Title, YearReleased, Rating, Duration, Genre as field name: ").lower()

    #field Value: ask for the value for the field(Title, YearReleased, Rating, Duration, Genre) to be updated
    fieldValue = input(f"Enter the value for {fieldName} field: ")
    print(fieldValue)

    fieldValue = "'"+fieldValue+"'" # add single quotes on either side of the field value(string)
    print(fieldValue)


    # update a record in the songs table
    "UPDATE tblFilms SET title or yearReleased or rating or duration or genre = TitleValue or YearReleasedValue or RatingValue or DurationValue or GenreValue WHERE filmID = 1/2/3/4..."
    dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
    dbCon.commit()

if __name__ == "__main__":
    update_data() # call or invoke the subroutine or function
    