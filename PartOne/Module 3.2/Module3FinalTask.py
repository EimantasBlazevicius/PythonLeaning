#code will check if the ammount provided is in the ranges of what the stode can offer
#if yet then will count how much this order will cost
#if no will jet let person know, that it is not expected ofhim to order this much/few

#describing constants
fullStock =  737
minimumOrder = 5
unitPrice = 7.37

#take the amount of cheese that is needed
howMuch = input()
#converting value to numeric/ int
howMuchInt = int(howMuch)

#if statment  to check what can be done based on person requested ammount of cheese
if howMuchInt > fullStock:
    print("You want too much my friend")
elif howMuchInt < minimumOrder:
    print("We dot sell our wonderful cheese in so small portions")
else:
    print("Yes, Ok, so " + howMuch + " kg of cheese would cost " + str(howMuchInt * unitPrice) + ".")
