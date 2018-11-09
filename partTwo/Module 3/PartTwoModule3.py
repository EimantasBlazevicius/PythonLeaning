'''
in this program we will loop thru entire orginalText, will make short words to lowercase long words to uppercase
write all modified words to new list, then will get into the function that will
pop words on each loop cycle to the new list based on some rules, and will output there words in they new
artistic nature.

CopyText:

Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me? Little fly,Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?

'''

#function that will pop elements from old list and puth them to new one, in a more fun way.
def word_mixer(tempList):
    returnValue = []
    internalList = sorted(tempList)
    while len(internalList) > 5:
        returnValue.append(internalList.pop(-5))
        returnValue.append(internalList.pop(0))
        returnValue.append(internalList.pop())
    #return list value
    return returnValue

#templorarty list to store upper/lower cased words.
tempList = []
#input of the original string
originalString = input("Please provide you text, for us to make very artistic, in a weird way: ").lower()
wordsList = originalString.split(" ")
howMuchWords = len(wordsList)
for var in range(howMuchWords):
    if len(wordsList[var]) <= 3:
        tempList.append(wordsList[var].lower())
    elif len(wordsList[var]) >= 7:
        tempList.append(wordsList[var].upper())
    else:
        pass  #will pass all values that did not fit lenght of the string a parameter, and numeric values
print(word_mixer(tempList))
