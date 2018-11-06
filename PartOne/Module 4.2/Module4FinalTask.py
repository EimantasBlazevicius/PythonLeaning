#infinite loop is just waiting for a break statment, inside of it we check if variable is present
#if yes we start str_analysis function that is checking if it is a digit and if it is big or small then, prints that
#if it is not a digit, but present, it will check if all values are string or not, prints results
#if value is not provided loop will start over asking to enter a value

#function that evaluates the provided values
def str_analysis(var):
#digit part
    if var.isdigit():
        newVar = int(var)
        if newVar > 99:
            print("Big number")
        else:
            print("Small Number")
#string part
    else:
        newVar = str(var)
        if newVar.isalpha():
            print("Text is all Alpha")
        else:
            print("Value not all alpha, not all digits")

#loop that only checks if value is placed in, and acts if there is a value, repeats if there is none
while True:
    print("Provide Value")
    var = input()
    if var or var == 0:
        str_analysis(var)
        break
    else:
        continue