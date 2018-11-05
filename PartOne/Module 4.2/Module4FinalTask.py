#ciklas laukia ne tuščios reikšmės ir ją radus iš esmės įvertina ar tai skaičius ar stringas, tada skaičių palygina ar didelis ar ne
# ir parašo žmogui ką suprato, o jeigu stringas tai įvertina ar vien tik simboliai ar ir skaiciu yra
def str_analysis(var):  #funkcija pasiimanti input reiksme
    if var.isdigit():       #patikrinam ar skaicius
        newVar = int(var)       #jeigu skaicius paverciam i tikra skaiciu
        if newVar > 99:     #patikrinam ar didelis skaicius
            print("Big number")
        else:           #patikrinam ar mazas skaicius
            print("Small Number")

    else:           #jeigu stringas
        newVar = str(var)       #tik kad buciau 100% tikras kad stringas
        if newVar.isalpha():        #ar tik stringai
            print("Text is all Alpha")
        else:               #nei stringas, nei skaicius
            print("Value not all alpha, not all digits")


while True:     #infinite loop while not break
    print("Provide Value")      #user interface
    var = input()           #zmogus įveda skaiciu
    if var or var == 0:         #jeigu reiksme ira ivesta, su mazu buffu, nes 0 butu irgi bool false, tai uzdejau dar ir ta
        str_analysis(var)       #paleidziam funkcija viskam nusprest
        break       #stabdom cikla
    else:
        continue   #tesiam cikla