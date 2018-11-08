'''

Task will collect data from the user input and will compare that to the file
elements.txt and will return a score based on amount of values that matched
between user input and values that are in the file

'''


# read file and collect data from there
def readafile():
    allValues = []
    rFile = open('elements.txt', 'r')
    rFile.seek(0)
    for line in rFile.readlines():
        allValues.append(line.rstrip('\n').lower())
    return allValues


# Collect user input values
def getuservalues():
    theGuesses = []
    while len(theGuesses) <= 4:
        print("Guess 5 atomic elements of first 20 elements from the table: ")
        userinput = input("Enter the name of the element: ").lower()
        if userinput == "":
            print("Error: No empty values are allowed")
            continue
        elif userinput in theGuesses:
            print("Error: No Duplicate values are allowed")
            continue
        else:
            theGuesses.append(userinput)
    return theGuesses


# function to compare lists
def compare_answer(data_list, user_list):
    correct = []
    wrong = []
    for name in user_list:
        if name in data_list:
            correct.append(name)
        elif name not in data_list:
            wrong.append(name)
        else:
            pass
    # all the printing happens in this block
    print(str(len(correct * 20)) + "% is correct!")
    print("Found: ", end=" ")
    print(*correct, sep=" ")
    print("Not found: ", end=" ")
    print(*wrong, sep=" ")


# Actual code.. Feels good

compare_answer(readafile(), getuservalues())

# it was surprise for me, that functions do still do all their job, even though it is just passed as variables
# to the third function
