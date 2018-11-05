#Function to do reporting
def adding_report(value,theType): #taking in two variables, for value in the current loop and what report value is required.
    if value != "q":                #checking if value is no q, to start reporting
        theList.append(value)       #if no reporting needed, append data list
    elif value == "q":              #if we do need to start reporting
        if theType is "A":          #check if report type is A
            sumVariable = 0         #predefined variable for sum in Total
            print("Items: ")        #user interface Stuff
            for variable in theList:    #list to go thru the list of values
                print(variable)         #prints every value in the loop
                sumVariable += variable     #summing stuff up in the sum variable
            print("Total Value: " + str(sumVariable))   #Showing total value
        elif theType is "T":    #if report type is T
            sumVariable = 0     #predefine Sum variable
            for variable in theList:
                sumVariable += variable
            print("Total Value: " + str(sumVariable))


theList = []   #defined theList to collect data

print("What type of reporting will you want? 'A' for detailed, and 'T' for only total value? ")  #user interface Stuff
reportType = input()        #User input what type od report will be required
while True:     #infinite While loop while not broken
    print("Provide the numeric value sum them up, if you wish to finish write something with q as a first letter.")     #User interface Stuff
    tempValue = input()     #user input the number or Q
    if tempValue.isdigit(): #check if the value provided is digit, as it will not be Q then.
        additionalValue = int(tempValue)        #making this variable a Init
        adding_report(additionalValue, reportType)  #calling my wonderful function to take value and reporting type
    elif tempValue.startswith("q") or tempValue.startswith("Q"):   #if temp value will at least start with a q or Q
        adding_report("q", reportType)  #sending signal to my function start preping them reports.
        break           #break the loop if reporting is done
    else:                   #if client just decided to click random buttons instead of digits or quiting
        print("Invalid input, sorry mate")      #let him know is going on
        continue    #start loop over.


