#person writes a value
#if value in the list, remove first instance of this item
#if value is no in the list append the list with this value
#if empty string pop last value from the list
#if list is empty end the program
#if quit provided as value end the program

#TheFunction to give value to return variable based on what is passed
def list_o_matic(word, list):
    prompt = ""
    #Checking if word is in the list and making sure that word is empty, if we allow empty words in first two IFs
    #third one never gets reached.
    if word in list and word != "":
        list.remove(word)
        prompt = "first instance of the word " + word + " was removed"
    elif word not in list and word != "":
        list.append(word)
        prompt = "This word: " + word + " was added to the names list"
    elif word == "":
        list.pop()
        prompt = "The last value of this list was removed"
    else:
        pass
    #function return value
    return prompt

#predefined list
theList = ["Homer", "Marge", "Bart", "Lisa", "Ned"]
#Loops while list is not empty, prompts person to input name, if Quit found, stops the program, if not send information to the function
#and keeps moving forward
while theList:
    print("This is the list of names we have at the moment: " + str(theList))
    theWord = input("enter the name: ")
    if theWord == "Quit":
        break
    else:
        print(list_o_matic(theWord, theList))
print("Goodbye!")