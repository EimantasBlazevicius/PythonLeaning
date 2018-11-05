def str_analysis(var):
    if var.isdigit():
        newVar = int(var)
        if newVar > 99:
            print("Big number")
        else:
            print("Small Number")

    else:
        newVar = str(var)
        if newVar.isalpha():
            print("Text is all Alpha")
        else:
            print("Value not all alpha, not all digits")


while True:
    print("Provide Value")
    var = input()
    if var:
        str_analysis(var)
        break
    else:
        continue