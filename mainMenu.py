import readFilms, addFilms, updateFilms, deleteFilms, theReportsMenuV2 

def menuFiles():
    with open("optionsMenu.txt") as mainMenu:
        userMenu = mainMenu.read()
    return userMenu

# songs menu function
def songsMenu():
    options = 0 # create option variable and initialise it with integer value 0
    optionsList = ["1","2","3","4","5","6"]
    # call/invoke the menuFiles function and assign/initialise with the userChoice variable
    userChoices = menuFiles()

    while options not in optionsList: # This will always be true 
        print(userChoices)

        # re-assign the options variable with the input function(which has a default string data type)
        options = input("Enter an option from the songs main menu choices above: ")

        # check to see if the re-assigned options variable(value) is not in the optionsList
        if options not in optionsList:
            print(f"{options} is not a valid choice in the songs menu! ")
    return options

# create a boolean variable and assign with a True value
mainProgram = True
while mainProgram: # same as While True
    mainMenu = songsMenu() # assign songsMenu function to the mainMenu variable
    # call/invoke the respective modules with their functions
    if mainMenu == "1":
        readFilms.read_data()
    elif mainMenu == "2":
        addFilms.insert_data()
    elif mainMenu == "3":
        updateFilms.update_data()
    elif mainMenu == "4":
        deleteFilms.delete_data()
    elif mainMenu == "5":
        theReportsMenuV2.theSubReport()
    else: 
        #reassign the mainProgram boolean variable with a false value
        mainProgram = False
input("Press Enter to exit the songs app.")