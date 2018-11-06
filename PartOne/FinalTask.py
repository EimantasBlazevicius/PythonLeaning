#program that is letting person to enter as much digits as he wants and after a operator "q" is eneter would break
#of data entering loop, would do one of two reports
#A detailed reports with all values and total and T for only total value of everything that he has entered

#function that will sum up the values and treat them as per task, based on the values that is provided to it
def adding_report(value,theType):
    if value != "q":
        theList.append(value)
    elif value == "q":
        #detailed report stuff
        if theType is "A":
            sumVariable = 0
            print("Items: ")
            for variable in theList:
                print(variable)
                sumVariable += variable
            print("Total Value: " + str(sumVariable))
        #Total report Stuff
        elif theType is "T":
            sumVariable = 0
            for variable in theList:
                sumVariable += variable
            print("Total Value: " + str(sumVariable))

#pre defined list variable
theList = []

#prompt to select type of reporting
print("What type of reporting will you want? 'A' for detailed, and 'T' for only total value? ")
reportType = input()
#Checking report value, to avoid unexpected outcomes
if reportType == "A" or reportType == "T":
    #loop to collect data
    while True:
        print("Provide the numeric value sum them up, if you wish to finish write q or Quit")
        tempValue = input()
        #as long as value is digit it will not be a "q", therefore we just sending information to our function to add the values to list.
        if tempValue.isdigit():
            additionalValue = int(tempValue)
            adding_report(additionalValue, reportType)
        #if client chose to stop entering values, send the signal to function, stop loop once any reporting is done
        elif tempValue.startswith("q") or tempValue.startswith("Q"):
            adding_report("q", reportType)
            break
        #start loop over with prompt to person, that value he entered is not valid
        else:
            print("Invalid input, sorry mate")
            continue
else:
    print("We can not provide this type of reporting at this time, please, start over, choose from what we have")

