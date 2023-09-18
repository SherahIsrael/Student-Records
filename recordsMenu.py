import reports

def menuFiles():
        with open(r"reportOptions.txt") as reportsMenu:
             userReport = reportsMenu.read()
        return userReport # return it as a tuple[str, str]

#reports sub Menu
def reportsMenu():
    options = 0
    optionsList = ["1","2","3"]
    reportChoices = menuFiles() # call the menuFiles() function and assigned it to reportChoices variable
    while options not in optionsList:
        print(reportChoices)

        options = input("Enter an options from the reports sub menu above: ")

        if options not in optionsList:
            print(f"{options} is not a valid choice in reports menu!")
    return options      

# The report Sub report menu 
def theSubReport():
     
     reportsProgram = True # create a boolean variable and assign with a True value hm
     while reportsProgram: # same as While True

        #call reportsMenu()
        reportSubMenu = reportsMenu()
        if reportSubMenu == "1":
            reports.reports()
        elif reportSubMenu == "2":
            reports.reports_search()
        else:
            #re-assign the value held in the boolean reportsProgram variable to False
            reportsProgram = False
            input("Press Enter to quit the report sub menu") 
     return reportsProgram

if __name__=="__main__":
     theSubReport()