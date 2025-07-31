# Name: Liam Washburn
# Class: CSC 110 - Fall 2023
# Assignment:  Programming Project Implementation
# Due Date: December 8th, 2023

# Program Title: Movie Data
 

def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ") #Gets the entered data file of movies
        try:
            inFile = open(fname, 'r') #Opens the file and reads it
            goodFile = True
        except IOError: #If the requested file is not found it prints a statement
            print("Invalid file name try again ... ")
    return inFile #Returns the file, names it inFile


def getData(inFile):#
    #Line 23-28 Creates empty lists for the data from the file
    titleList = []
    genreList = []
    directorList = []
    yearList = []
    run_timeList = []
    revenueList = []
    #Line 30 Skips the first line in the file which is the header
    next(inFile)
    #This for loop reads all lines in the file
    for line in inFile:
        line = line.strip()
        title, genre, director, year, run_time, revenue = line.split(",") #This line.split takes away all commas in between the variables
        #Line 36-41 appends all data to the its specified list
        titleList.append(title)
        genreList.append(genre)
        directorList.append(director)
        yearList.append(int(year))
        run_timeList.append(int(run_time))
        revenueList.append(float(revenue))
    inFile.close()
    return titleList, genreList, directorList, yearList, run_timeList, revenueList #Returns all the lists

def getChoice():
    choiceStatement = False #Sets choiceStatement eqaul to False 
    #Line 48-56 displays the options the user can select
    print("")
    print("Please choose one of the following options:")
    print("1 -- Find all films made by a specified director")
    print("2 -- Find the highest grossing film made in a specific year")
    print("3 -- Find all films made in a given year range in a specified genre")
    print("4 -- Search for a film by title")
    print("5 -- Find average runtime of films with higher revenue than specified value")
    print("6 -- Sort all lists by revenue and write the results to a new file")
    print("7 -- Quit")
    while choiceStatement == False: #This loop will run until choiceStatement is no longer eqaul to False
        try:
            choice = int(input("Choice ==> ")) #Allows the user to enter a choice
            if choice >= 1 and choice <= 7 : #Looks to see if the users entry was between 1 and 7
                choiceStatement = True
            else:
                print("Choice must be between 1 and 7") #This statement is printed if 
        except ValueError: #Line 64-65, if the entry is not a number than a ValueError will occur causing "Invalid entry - Try again" to be printed
            print("Invalid entry - Try again")
            
    print("")
    return choice #Returns the users choice

#Finds all films made by a certain director and returns the films with the corresponding data 
def findDirectorFilms(directorList, directorSearched): #Takes in a list from the data file along with directorSearched, which is the specified director entered by the user
    directorIndexList = [] #Initializes an empty list called directorIndexList, this will store the index of the directors movies and information to go along with them
    
    for i in range(len(directorList)): #Loops through the length of the directorList
        if directorList[i] == directorSearched: #If the specified director that the user entered is in the directorList, the index is appened to the list
           directorIndexList.append(i)
           
    return directorIndexList #Returns the directorIndexList

#Takes in the year that the user wants to search for
#Seach through the movie list and revenue list to find the highest grossing film
def findhighestGrossFilm(revenueList, yearList, yearSearched): #Takes in lists from the data file along with yearSearched, which is the specified year entered by the user
    foundYearList = [] #Initializes foundYearList to an empty set
    highestRevenue = 0 #Initializes highestRevenue to zero
    highestIndex = 0 #Initializes highestIndex to zero, will store the highest grossing film
    
    for i in range(len(yearList)): #Loops through the length of the yearList
        if yearList[i] == yearSearched: #Checks if the year searched by the user is in the yearList, all movies indexes that are in the year are added to the foundYearList
            foundYearList.append(i)
                
    for j in range(len(foundYearList)): #Loops through the foundYearList
        if float(revenueList[foundYearList[j]]) > highestRevenue: #compares the revenue if the foundYearList[j] movie to the highest revenue to 
            highestRevenue = float(revenueList[foundYearList[j]]) #Sets highestRevenue to revenueList and index foundYearList[j]
            highestIndex = foundYearList[j] #Sets foundYearList[j] to highestIndex
                
    return highestIndex #Returns the highestIndex

# Get the genre from the user
# Get the range of years from the user
# return a list of movies from those years and the genre
def findFilmsGenre(genreList, yearList, year1, year2, genreSpecified): #Takes in lists from the data file along with year1, year2, genreSpecified, which is the specified years entered by the user and the genre entered
    yearRangeList = [] #Intializes yearRangeList to empty set
    specifiedList = [] #Intializes specifiedList to empty set
    
    for i in range(len(yearList)): #Loops through the yearList
        if yearList[i] >= year1 and  yearList[i] <= year2: #Finds the movies in those 2 specified years and the movies in between them
            yearRangeList.append(i) #Appends i to yearRangeList

    
    for j in range(len(yearRangeList)):#Loops through year range list
        index = yearRangeList[j] #Sets index eqaul to yearRangeList at postion [j]
        genre = genreList[index].split(";") #Getting all the genres of the movie 
        for k in range(len(genre)): #Checking to see if the movie has specified genre
            if genre[k] == genreSpecified: #looks for all movies that the user entered
                specifiedList.append(index) #Appends the index to the specifiedList
    
    
    return specifiedList #Returns the specifiedList

# Allows the user to search by a specific Title
# Returns details of that movie
def searchFilmTitle(titleList, filmSearched): #Takes in a list from the data file along with filmSearched, which is the specified film entered by the user
    foundFilm = [] #Intializes foundFilm to empty set

    for i in range(len(titleList)): #Loops through for the length of titleList
        if titleList[i] == filmSearched: #Finds the specified film in the titleList
            foundFilm.append(i) #Appends i to foundFilm
    
    return foundFilm #Returns the foundFilm

# Takes in the run times for all movies in the set and finds the average run times
# The function also gets the revenue threshold and will ask for re entry if it is not valid
def findAvgRunwithRev(run_timeList, revenueList, revLimit): #Takes in lists from the data file along with revLimit, which is the specified limit of revenue entered by the user
    newRuntimeList = [] #Intializes newRuntimeList to empty set
    
    for i in range(len(revenueList)): #Loops for the length of revenueList
        if revenueList[i] > revLimit: #Checks to see which movies revenue are greater that the revLimit
            newRuntimeList.append(run_timeList[i]) #Appends the run_timeList at index i 
    
    
    theSum = sum(newRuntimeList) #Gets the sum of the newRuntimeList
    averageRun = (theSum / (len(newRuntimeList))) #Gets the average runtime of the specified movies 
    averageRuntimeR = round(averageRun, 2) #Rounds the average runtime of the movies to the second decimal place
    
    return  averageRuntimeR #Returns the averageRuntimeR

# Takes in all lists
# Uses a sorting method to take every list and put them in acending order from least to greatest 
# returns all lists in new order
def sortListRev(titleList, genreList, directorList, yearList, run_timeList, revenueList): #Takes in all lists from the original data file
    newRevenueList = revenueList.copy() #Makes copy of revenueList
    revenueIndexList = [] #Intializes revenueIndexList to empty set
    for i in range(len(newRevenueList)): #Loops through for the length of newRevenueList 
        revenueIndexList.append(i) #Appends i to the revenueIndexList

    #Line 156-166 uses Insertion Sort to sort the two lists at the same time
    n = len(newRevenueList)
    for i in range(1, n):
        save = newRevenueList[i]
        save2 = revenueIndexList[i]
        j = i-1
        while j >= 0 and save < newRevenueList[j]:
            newRevenueList[j+1] = newRevenueList[j]
            revenueIndexList[j+1] = revenueIndexList[j]
            j= j - 1
        newRevenueList[j+1] = save
        revenueIndexList[j+1] = save2
        
            
    
    
    outFile = open("movies-sorted-rev.csv", 'w') #Opens/Makes a new file called "movies-sorted-rev.csv" and writes to it
    for k in range(len(revenueIndexList)): #Loops through for the length of revenueIndexList
        index = revenueIndexList[k] #Sets index eqaul to revenueIndexList[k]
        outFile.write(titleList[index] +  "," +  genreList[index] +  "," +  directorList[index] + "," + str(yearList[index]) + "," + str(run_timeList[index]) + "," + str(revenueList[index]) + "\n") #Writes this statement to the file
    outFile.close() #Closes the file
    return 

def printResults(titleList, genreList, directorList, yearList, run_timeList, revenueList, choice, directorIndexList, highestIndex, specifiedList, foundFilm, revLimit, averageRuntimeR):
    if choice == 1:
        #Prints these statements of choice 1 is chosen
        print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12)) #This is the header
        for j in range(len(directorIndexList)): #Loops for the length of the directorIndexList
            print(titleList[directorIndexList[j]].ljust(45), genreList[directorIndexList[j]].ljust(35), directorList[directorIndexList[j]].ljust(24), str(yearList[directorIndexList[j]]).ljust(8), str(run_timeList[directorIndexList[j]]).ljust(8), ("$"+str(revenueList[directorIndexList[j]])).rjust(12))
            
    elif choice == 2:
        #Prints these statements of choice 2 is chosen
        print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12)) #This is the header
        print(titleList[highestIndex].ljust(45), genreList[highestIndex].ljust(35), directorList[highestIndex].ljust(24), str(yearList[highestIndex]).ljust(8), str(run_timeList[highestIndex]).ljust(8), ("$"+str(revenueList[highestIndex])).rjust(12))

    elif choice == 3:
        #Prints these statements of choice 3 is chosen
        print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12)) #This is the header
        for k in range(len(specifiedList)): #Loops for the length of the specifiedList
            print(titleList[specifiedList[k]].ljust(45), genreList[specifiedList[k]].ljust(35), directorList[specifiedList[k]].ljust(24), str(yearList[specifiedList[k]]).ljust(8), str(run_timeList[specifiedList[k]]).ljust(8), ("$"+str(revenueList[specifiedList[k]])).rjust(12))       

    elif choice == 4:
        #Prints these statements of choice 4 is chosen
        print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12)) #This is the header
        print(titleList[foundFilm[0]].ljust(45), genreList[foundFilm[0]].ljust(35), directorList[foundFilm[0]].ljust(24), str(yearList[foundFilm[0]]).ljust(8), str(run_timeList[foundFilm[0]]).ljust(8), ("$"+str(revenueList[foundFilm[0]])).rjust(12))

    elif choice == 5:
        #Prints this statement if choice 5 is chosen
        print("The average runtime for films with revenue higher than $", f"{revLimit:.2f}", "million is ", averageRuntimeR, "minutes.") 

    elif choice == 6:
        #Prints this statement if choice 6 is chosen
        print("Sorted data has been written to the file: movies-sorted-rev.csv.")
    return

# The main function implements the pseudocode by using the functions defined above.
def main():
    inFile = openFile() #Calls the function openFile
    titleList, genreList, directorList, yearList, run_timeList, revenueList = getData(inFile) #Calls the function getData
    choice = getChoice() #Calls the function getChoice
    while choice != 7: #Keeps looping till choice eqauls 7
        if choice == 1: #Runs if choice eqauls 1
            directorSearched = input("Enter director: ") #Asks the user to enter a director
            if directorSearched not in directorList: #If the director is not in the directorList then a message is outputed
                print("Invalid entry - Try again")
            else:
                print("\nThe films that meet your criteria are: ") 
                directorIndexList = findDirectorFilms(directorList, directorSearched) #Calls the function findDirectorFilms
                highestIndex = 0 #Initializes highestIndex to zero
                foundFilm = [] #Initializes foundFilm to an empty set
                specifiedList = [] #Initializes specifiedList to an empty set
                averageRuntimeR = 0 #Initializes averageRuntimeR to zero
                revLimit = 0 #Initializes revLimit to zero
                
                printResults(titleList, genreList, directorList, yearList, run_timeList, revenueList, choice, directorIndexList, highestIndex, specifiedList, foundFilm, revLimit, averageRuntimeR)#Calls the printResults fuction
                choice = getChoice() #Calls the function getChoice
                
        elif choice == 2: #Runs if choice eqauls 2
            
            try:
                yearSearched = int(input("Enter year: ")) #Asks the user to enter a year
                if yearSearched > 2016 or yearSearched < 2006: #Checks if year entered is between 2006 and 2016, if it is not a message is displayed
                    print("Year out of range, must be between 2006 and 2016")
                else:
                    print("The film that meets your criteria is: ") 
                    highestIndex = findhighestGrossFilm(revenueList, yearList, yearSearched) #Calls the function findhighestGrossFilm
                    directorIndexList = [] #Initializes directorIndexList to an empty set
                    foundFilm = [] #Initializes foundFilm to an empty set
                    specifiedList = [] #Initializes specifiedList to an empty set
                    averageRuntimeR = 0 #Initializes averageRuntimeR to zero
                    revLimit = 0 #Initializes revLimit to zero
                    
                    printResults(titleList, genreList, directorList, yearList, run_timeList, revenueList, choice, directorIndexList, highestIndex, specifiedList, foundFilm, revLimit, averageRuntimeR) #Calls the printResults fuction
                    choice = getChoice() #Calls the function getChoice
            except ValueError:
                    print("Invalid entry - Try again")
                    
        elif choice == 3: #Runs if choice eqauls 3
            year1Statement = False #Sets Statement to False
            year2Statement = False #Sets Statement to False
            genreStatement = False #Sets Statement to False
            year1 = 0 #Sets year1 to 0
            year2 = -1 #Sets year2 to -1
            print("Enter year range to search (oldest year first)") #Shows the user what order to enter the years in
            while year2 < year1:  # this will run while year2 is greater than year 1
                year1Statement = False #Sets Statement to False
                year2Statement = False #Sets Statement to False
                
                while year1Statement == False: #Runs while the statement is still false
                    try:
                        year1 = int(input("Year1: ")) #Asks user to put in year1
                        if year1 < 2006 or year1 > 2016: #If year1 is not between 2006 and 2016 a message is outputed
                            print("Year out of range, must be between 2006 and 2016")
                            year1Statement = False #Sets Statement to False
                        else:
                            year1Statement = True #Sets Statement to True
                    except ValueError:#Runs if entry is not a number
                        print("Invalid entry - Try again")
                    
                   
                while year2Statement == False: #Runs while condition is False
                    try:
                        year2 = int(input("Year2: ")) #Asks user to put in year2
                        if year2 < 2006 or year2 > 2016: #If year1 is not between 2006 and 2016 a message is outputed
                            print("Year out of range, must be between 2006 and 2016")
                            year2Statement = False #Sets Statement to False
                        elif year1 > year2: #If year 1 is greater than year 2 a message is outputed
                            print("Second year should be after first year - try again")
                            year2Statement = True #Sets Statement to True
                            year1Statement = True #Sets Statement to True
                        else:
                            year2Statement = True #Sets Statement to True
                    except ValueError: #Runs if entry is not a number
                        print("Invalid entry - Try again")
                    
            while genreStatement == False: #Runs while condition is False
                genreSpecified = input("Enter genre: ") #Asks user to enter a genre
                if genreSpecified not in genreList: #If the genre is not in the list a message is outputed
                    print("Invalid entry - Try again")
                    genreStatement = False #Sets Statement to False
                else:
                    print("The films that meet your criteria are: ")
                    specifiedList = findFilmsGenre(genreList, yearList, year1, year2, genreSpecified) #Calls the findFilmsGenre function
                    directorIndexList = [] #Initializes directorIndexList to an empty set
                    foundFilm = [] #Initializes foundFilm to an empty set
                    highestIndex = 0 #Initializes highestIndex to zero
                    averageRuntimeR = 0 #Initialzes averageRuntimeR to zero
                    revLimit = 0 #Initializes revLimit to zero
                    
                    printResults(titleList, genreList, directorList, yearList, run_timeList, revenueList, choice, directorIndexList, highestIndex, specifiedList, foundFilm, revLimit, averageRuntimeR) #Calls the printResults fuction
                    choice = getChoice() #Calls the getChoice function
                    genreStatement = True #Sets Statement to True
                
        elif choice == 4: #Runs if choice eqauls 4
            filmSearched = input("Enter title: ") #Asks user to enter title
            if filmSearched not in titleList: #Checks if filmSearched is in the title list, if not it displays a message
                print("\nNo such film exists.")
                choice = getChoice() #Calls the getChoice function
            else:
                print("\nThe film that meets your criteria is: \n")
                #***
                foundFilm = searchFilmTitle(titleList, filmSearched)
                directorIndexList = [] #Initializes directorIndexList to an empty set
                highestIndex = 0 #Initializes highestIndex to zero
                specifiedList = [] #Initializes specifiedList to an empty set
                averageRuntimeR = 0 #Initialzes averageRuntimeR to zero
                revLimit = 0 #Initializes revLimit to zero
                
                printResults(titleList, genreList, directorList, yearList, run_timeList, revenueList, choice, directorIndexList, highestIndex, specifiedList, foundFilm, revLimit, averageRuntimeR) #Calls the printResults fuction
                choice = getChoice() #Calls the getChoice function
                
        elif choice == 5: #Runs if choice eqauls 5
            revLimit = float(input("Enter revenue limit (millions): $")) #Asks for the user input for revuenue limit
            higherRevList = [] #Initializes higherRevList to an empty set
            for i in range(len(revenueList)): #Loops for the length of revenueList
                if float(revenueList[i]) > float(revLimit): #Checks if revenueList is greater than revLimit
                    higherRevList.append(i) #appends i to higherRevList
            
            if (len(higherRevList)) == 0: #If there is nothing in the higherRevList then it prints a statement
                print("No films have revenue higher than $", f"{revLimit:.2f}", "million.")
                choice = getChoice() #Calls the function getChoice
            else:
                averageRuntimeR = findAvgRunwithRev(run_timeList, revenueList, revLimit) #Calls averageRuntimeR function
                directorIndexList = [] #Initializes directorIndexList to an empty set
                highestIndex = 0 #Initializes highestIndex to zero
                specifiedList = [] #Initializes specifiedList to an empty set
                foundFilm = [] #Initializes foundFilm to an empty set
                
                printResults(titleList, genreList, directorList, yearList, run_timeList, revenueList, choice, directorIndexList, highestIndex, specifiedList, foundFilm, revLimit, averageRuntimeR) #Calls the printResults fuction
                choice = getChoice()#Calls the function getChoice
                    
        elif choice == 6: #Runs if choice eqauls 6
            sortListRev(titleList, genreList, directorList, yearList, run_timeList, revenueList) #Calls sortListRev function
            directorIndexList = [] #Initializes directorIndexList to an empty set
            highestIndex = 0 #Initializes highestIndex to zero
            specifiedList = [] #Initializes specifiedList to an empty set
            foundFilm = [] #Initializes foundFilm to an empty set
            revLimit = 0 #Initializes revLimit to zero
            averageRuntimeR = 0 #Initializes averageRuntimeR zero
            
            printResults(titleList, genreList, directorList, yearList, run_timeList, revenueList, choice, directorIndexList, highestIndex, specifiedList, foundFilm, revLimit, averageRuntimeR) #Calls the printResults fuction
            choice = getChoice() #Calls the function getChoice
            
        
            
    print("Good-bye") #Prints when choice is equal to 7
            
