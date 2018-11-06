'''

Task will collect data from the user input and will compare that to the file
elements.txt and will return a score based on amount of values that matched
between user input and values that are in the file

'''


def readafile():

    allValues = []
    rFile = open('elements.txt','r')
    rFile.seek(0)
    for line in rFile.readlines():
        allValues.append(line.rstrip('\n').lower())
    return allValues


def getuservalues():

    theGuesses = []
    while True:
        print("Guess 5 atomic elements of first 20 elements from the table: ")
        userInput = input("Enter the name of the element: ").lower()
        if userInput == "":
            print("Error: No empty values are allowed")
            continue
        elif userInput in theGuesses:
            print("Error: No Duplicate values are allowed")
        else:
            theGuesses.append(userInput)
